# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blog.proto',
  package='blog',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nblog.proto\x12\x04\x62log\"\x9b\x02\n\x08\x42logPost\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04lead\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12.\n\x0bmarkup_type\x18\x05 \x01(\x0e\x32\x19.blog.BlogPost.MarkupType\x12\x0e\n\x06locale\x18\x06 \x01(\t\x12\x17\n\x04tags\x18\x07 \x03(\x0b\x32\t.blog.Tag\x12\x0e\n\x06\x61\x63tive\x18\x08 \x01(\x08\x12\x10\n\x08pub_date\x18\t \x01(\x03\x12\x13\n\x0b\x63reate_date\x18\n \x01(\x03\x12\x13\n\x0bupdate_date\x18\x0b \x01(\x03\".\n\nMarkupType\x12\x0c\n\x08MARKDOWN\x10\x00\x12\x08\n\x04REST\x10\x01\x12\x08\n\x04HTML\x10\x02\"\x13\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\x0eGetPostRequest\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0c\n\x04slug\x18\x02 \x01(\t\",\n\x0cGetPostReply\x12\x1c\n\x04post\x18\x01 \x01(\x0b\x32\x0e.blog.BlogPost\"\x9a\x01\n\x0eGetPageRequest\x12\x10\n\x08pub_date\x18\x01 \x01(\x03\x12\x0e\n\x06locale\x18\x02 \x01(\t\x12\x16\n\x03tag\x18\x03 \x01(\x0b\x32\t.blog.Tag\x12 \n\x06\x61\x63tive\x18\x04 \x01(\x0e\x32\x10.blog.ActiveType\x12\x13\n\x0bpage_number\x18\x05 \x01(\r\x12\x17\n\x0fresult_per_page\x18\x06 \x01(\r\"-\n\x0cGetPageReply\x12\x1d\n\x05posts\x18\x01 \x03(\x0b\x32\x0e.blog.BlogPost\"\x89\x01\n\x12GetNumPagesRequest\x12\x10\n\x08pub_date\x18\x01 \x01(\x03\x12\x0e\n\x06locale\x18\x02 \x01(\t\x12\x16\n\x03tag\x18\x03 \x01(\x0b\x32\t.blog.Tag\x12 \n\x06\x61\x63tive\x18\x04 \x01(\x0e\x32\x10.blog.ActiveType\x12\x17\n\x0fresult_per_page\x18\x05 \x01(\r\"%\n\x10GetNumPagesReply\x12\x11\n\tnum_pages\x18\x01 \x01(\x04*7\n\nActiveType\x12\x07\n\x03\x41LL\x10\x00\x12\r\n\tPUBLISHED\x10\x01\x12\x11\n\rNOT_PUBLISHED\x10\x02\x32\xb7\x01\n\x04\x42log\x12\x35\n\x07GetPost\x12\x14.blog.GetPostRequest\x1a\x12.blog.GetPostReply\"\x00\x12\x35\n\x07GetPage\x12\x14.blog.GetPageRequest\x1a\x12.blog.GetPageReply\"\x00\x12\x41\n\x0bGetNumPages\x12\x18.blog.GetNumPagesRequest\x1a\x16.blog.GetNumPagesReply\"\x00\x62\x06proto3')
)

_ACTIVETYPE = _descriptor.EnumDescriptor(
  name='ActiveType',
  full_name='blog.ActiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLISHED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_PUBLISHED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=804,
  serialized_end=859,
)
_sym_db.RegisterEnumDescriptor(_ACTIVETYPE)

ActiveType = enum_type_wrapper.EnumTypeWrapper(_ACTIVETYPE)
ALL = 0
PUBLISHED = 1
NOT_PUBLISHED = 2


_BLOGPOST_MARKUPTYPE = _descriptor.EnumDescriptor(
  name='MarkupType',
  full_name='blog.BlogPost.MarkupType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MARKDOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=258,
  serialized_end=304,
)
_sym_db.RegisterEnumDescriptor(_BLOGPOST_MARKUPTYPE)


_BLOGPOST = _descriptor.Descriptor(
  name='BlogPost',
  full_name='blog.BlogPost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slug', full_name='blog.BlogPost.slug', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='blog.BlogPost.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lead', full_name='blog.BlogPost.lead', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='blog.BlogPost.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='markup_type', full_name='blog.BlogPost.markup_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locale', full_name='blog.BlogPost.locale', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='blog.BlogPost.tags', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='blog.BlogPost.active', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_date', full_name='blog.BlogPost.pub_date', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_date', full_name='blog.BlogPost.create_date', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_date', full_name='blog.BlogPost.update_date', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BLOGPOST_MARKUPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=304,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='blog.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='blog.Tag.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=325,
)


_GETPOSTREQUEST = _descriptor.Descriptor(
  name='GetPostRequest',
  full_name='blog.GetPostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locale', full_name='blog.GetPostRequest.locale', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slug', full_name='blog.GetPostRequest.slug', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=373,
)


_GETPOSTREPLY = _descriptor.Descriptor(
  name='GetPostReply',
  full_name='blog.GetPostReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='post', full_name='blog.GetPostReply.post', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=419,
)


_GETPAGEREQUEST = _descriptor.Descriptor(
  name='GetPageRequest',
  full_name='blog.GetPageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_date', full_name='blog.GetPageRequest.pub_date', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locale', full_name='blog.GetPageRequest.locale', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='blog.GetPageRequest.tag', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='blog.GetPageRequest.active', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_number', full_name='blog.GetPageRequest.page_number', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_per_page', full_name='blog.GetPageRequest.result_per_page', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=576,
)


_GETPAGEREPLY = _descriptor.Descriptor(
  name='GetPageReply',
  full_name='blog.GetPageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='posts', full_name='blog.GetPageReply.posts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=623,
)


_GETNUMPAGESREQUEST = _descriptor.Descriptor(
  name='GetNumPagesRequest',
  full_name='blog.GetNumPagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_date', full_name='blog.GetNumPagesRequest.pub_date', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locale', full_name='blog.GetNumPagesRequest.locale', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='blog.GetNumPagesRequest.tag', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='blog.GetNumPagesRequest.active', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_per_page', full_name='blog.GetNumPagesRequest.result_per_page', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=626,
  serialized_end=763,
)


_GETNUMPAGESREPLY = _descriptor.Descriptor(
  name='GetNumPagesReply',
  full_name='blog.GetNumPagesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_pages', full_name='blog.GetNumPagesReply.num_pages', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=802,
)

_BLOGPOST.fields_by_name['markup_type'].enum_type = _BLOGPOST_MARKUPTYPE
_BLOGPOST.fields_by_name['tags'].message_type = _TAG
_BLOGPOST_MARKUPTYPE.containing_type = _BLOGPOST
_GETPOSTREPLY.fields_by_name['post'].message_type = _BLOGPOST
_GETPAGEREQUEST.fields_by_name['tag'].message_type = _TAG
_GETPAGEREQUEST.fields_by_name['active'].enum_type = _ACTIVETYPE
_GETPAGEREPLY.fields_by_name['posts'].message_type = _BLOGPOST
_GETNUMPAGESREQUEST.fields_by_name['tag'].message_type = _TAG
_GETNUMPAGESREQUEST.fields_by_name['active'].enum_type = _ACTIVETYPE
DESCRIPTOR.message_types_by_name['BlogPost'] = _BLOGPOST
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['GetPostRequest'] = _GETPOSTREQUEST
DESCRIPTOR.message_types_by_name['GetPostReply'] = _GETPOSTREPLY
DESCRIPTOR.message_types_by_name['GetPageRequest'] = _GETPAGEREQUEST
DESCRIPTOR.message_types_by_name['GetPageReply'] = _GETPAGEREPLY
DESCRIPTOR.message_types_by_name['GetNumPagesRequest'] = _GETNUMPAGESREQUEST
DESCRIPTOR.message_types_by_name['GetNumPagesReply'] = _GETNUMPAGESREPLY
DESCRIPTOR.enum_types_by_name['ActiveType'] = _ACTIVETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlogPost = _reflection.GeneratedProtocolMessageType('BlogPost', (_message.Message,), dict(
  DESCRIPTOR = _BLOGPOST,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.BlogPost)
  ))
_sym_db.RegisterMessage(BlogPost)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), dict(
  DESCRIPTOR = _TAG,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.Tag)
  ))
_sym_db.RegisterMessage(Tag)

GetPostRequest = _reflection.GeneratedProtocolMessageType('GetPostRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPOSTREQUEST,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetPostRequest)
  ))
_sym_db.RegisterMessage(GetPostRequest)

GetPostReply = _reflection.GeneratedProtocolMessageType('GetPostReply', (_message.Message,), dict(
  DESCRIPTOR = _GETPOSTREPLY,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetPostReply)
  ))
_sym_db.RegisterMessage(GetPostReply)

GetPageRequest = _reflection.GeneratedProtocolMessageType('GetPageRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPAGEREQUEST,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetPageRequest)
  ))
_sym_db.RegisterMessage(GetPageRequest)

GetPageReply = _reflection.GeneratedProtocolMessageType('GetPageReply', (_message.Message,), dict(
  DESCRIPTOR = _GETPAGEREPLY,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetPageReply)
  ))
_sym_db.RegisterMessage(GetPageReply)

GetNumPagesRequest = _reflection.GeneratedProtocolMessageType('GetNumPagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNUMPAGESREQUEST,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetNumPagesRequest)
  ))
_sym_db.RegisterMessage(GetNumPagesRequest)

GetNumPagesReply = _reflection.GeneratedProtocolMessageType('GetNumPagesReply', (_message.Message,), dict(
  DESCRIPTOR = _GETNUMPAGESREPLY,
  __module__ = 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetNumPagesReply)
  ))
_sym_db.RegisterMessage(GetNumPagesReply)



_BLOG = _descriptor.ServiceDescriptor(
  name='Blog',
  full_name='blog.Blog',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=862,
  serialized_end=1045,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPost',
    full_name='blog.Blog.GetPost',
    index=0,
    containing_service=None,
    input_type=_GETPOSTREQUEST,
    output_type=_GETPOSTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPage',
    full_name='blog.Blog.GetPage',
    index=1,
    containing_service=None,
    input_type=_GETPAGEREQUEST,
    output_type=_GETPAGEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNumPages',
    full_name='blog.Blog.GetNumPages',
    index=2,
    containing_service=None,
    input_type=_GETNUMPAGESREQUEST,
    output_type=_GETNUMPAGESREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BLOG)

DESCRIPTOR.services_by_name['Blog'] = _BLOG

# @@protoc_insertion_point(module_scope)