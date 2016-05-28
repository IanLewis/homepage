#!/bin/bash

# Renews the Let's Encrypt certificate for the website
# and automatically updates the HTTP Load Balancer with
# the new cert.

set -e

# Required environment variables
# GCE_PROJECT: GCP Project id
# EMAIL: Let's Encrypt account email address
# ZONE: The Cloud DNS Zone name
# DOMAINS: Space delimited list of domains to renew (e.g. www.example.com www.example2.com test.example.com)
# NAMESPACE: The kubernetes namespace

# Required:
# md5sum

export GOOGLE_APPLICATION_CREDENTIALS=/etc/secrets/key.json
export LEGOPATH=/etc/lego/.lego

echo "Authenticating Google SDK"
gcloud auth activate-service-account `cat /etc/secrets/service-account` --key-file /etc/secrets/key.json
gcloud config set project ${GCE_PROJECT}

# Cleanup.
EXE_TRANS=""
gcloud dns record-sets transaction start --zone=${ZONE}
for DOMAIN in ${DOMAINS}
do
    gcloud dns record-sets transaction start --zone=${ZONE}
    TEMP=`gcloud dns record-sets list --zone ianlewis-org --type=TXT --name=_acme-challenge.${DOMAIN} | grep _acme-challenge.${DOMAIN}`
    if [ ${TEMP} != "" ]; then
        gcloud dns record-sets remove --zone=${ZONE} --type=TXT --name=_acme-challenge.${DOMAIN}
        EXE_TRANS=1
    fi
done
if [ ${EXE_TRANS} != "" ]; then
    gcloud dns record-sets transaction execute --zone=${ZONE}
else 
    gcloud dns record-sets transaction abort --zone=${ZONE}
fi

DOMAIN_OPTS=""
for DOMAIN in ${DOMAINS}
do
    DOMAIN_OPTS=${DOMAIN_OPTS}+" -d ${DOMAIN}"
done

# Renew the certificates
echo "Renewing certificates..."
if [ -d "${LEGOPATH}" ]; then
    /lego --path=${LEGOPATH} --email=${EMAIL} ${DOMAIN_OPTS} --dns="gcloud" --accept-tos renew
else
    /lego --path=${LEGOPATH} --email=${EMAIL} ${DOMAIN_OPTS} --dns="gcloud" --accept-tos run
fi
echo "Renewal successful."

# Get old cert name
echo "Getting current cert"
OLDCERT=`gcloud compute target-https-proxies describe ${NAMESPACE}-https | grep https://www.googleapis.com/compute/v1/projects/ianlewis-org/global/sslCertificates/ | awk '{print $2}'`
if [ "${OLDCERT}" != "" ]; then
    echo "Got current cert: ${OLDCERT}..."
else
    echo "No current cert."
fi

# Determine a certificate name based on a hash of the content.
CERTNAME=homepage-`md5sum -b ${LEGOPATH}/certificates/*.crt | awk '{print $1}'`

echo "Creating new cert: ${CERTNAME}..."
# Create the a new ssl certificate using gcloud
gcloud compute ssl-certificates create ${CERTNAME} --certificate ${LEGOPATH}/certificates/*.crt --private-key ${LEGOPATH}/certificates/*.key

echo "Updating target-https-proxies..."
# Update target-https-proxies to use the new certificate
gcloud compute target-https-proxies update ${NAMESPACE}-https --ssl-certificate ${CERTNAME}
echo "target-https-proxies updated."

# Wait a bit to allow it to propagate.
echo "Waiting 60s for new cert to propagate..."
sleep 60

# Delete the old certificate.
if [ "${OLDCERT}" != "" ]; then
    echo "Deleting old certificate: ${OLDCERT}..."
    gcloud -q compute ssl-certificates delete ${OLDCERT}
fi

echo "Done."