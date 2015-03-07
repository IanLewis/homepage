#:coding=utf-8:

from distutils.core import Command
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist


class BuildStatic(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Run the collectstatic django command.
        import os
        # NOTE: Enable debug mode so it doesn't complain about required
        #       settings like SECRET_KEY.
        os.environ['DEBUG'] = 'True'
        os.environ['DJANGO_SETTINGS_MODULE'] = 'homepage.settings'
        from django.core.management import call_command
        call_command('collectstatic', interactive=False)


class SdistWithBuildStatic(sdist):
    def run(self):
        self.run_command('build_static')
        return sdist.run(self)


install_requires = [
    'Django==1.4.17',
    'South==0.7.6',

    # For rendering blog posts
    'docutils>=0.5',
    'pygments>=1.0',
    'html2text==3.200.3',

    # For thumbnails
    'Pillow==2.5.1',
    'sorl-thumbnail==11.12',

    # Filebrowser admin.
    'django-filebrowser-no-grappelli==3.5.7',

    # Pagination
    'django-pagination==1.0.7',

    # Not sure where the code is being maintained because
    # the google code repo is old.
    # TODO: Replace.
    'django-tagging==0.3.2',

    # Comments
    'django-disqus==0.4.3',

    # Static file compression.
    'django-compressor==1.4',

    # Production
    'gunicorn==0.14.2',
    'MySQL-python==1.2.3',
    'pylibmc==1.4.1',
]

setup(
    name="homepage",
    version="0.0.8",
    author="Ian Lewis",
    author_email="ianmlewis@gmail.com",
    description="Ian Lewis' homepage at www.ianlewis.org",
    license="MIT",
    keywords="django homepage blog",
    url="http://www.ianlewis.org/",
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=install_requires,
    include_package_data=True,  # Include static files, templates, etc.
    cmdclass={
        'build_static': BuildStatic,
        'sdist': SdistWithBuildStatic,
    },
    entry_points={
        'console_scripts': [
            'homepage = homepage.runner:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
    ],
)