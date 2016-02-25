# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426736039.850134
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/base_app/styles/base_template.cssm'
_template_uri = 'base_template.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('/* \n  Dynamic CSS for the base.html page goes here.  In other words, Python code can be placed here.\n  \n  Since base.html is the common ancestor of all templates of all apps on our site,\n  CSS included here will be placed on *every* page of the site.\n*/\n')

  # just a silly example of embedding Python/Mako code within the .cssm file.
        import random
        font_color = ''.join([ random.choice('0123456789ABCDEF') for i in range(6) ])
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['random','font_color','i'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n#site_header {\n  display: inline-block;\n  margin-left: 12px;\n  font-size: 36px; \n  color: #')
        __M_writer(str( font_color ))
        __M_writer('; \n  vertical-align: top;\n}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "base_template.cssm", "filename": "/Users/benmackley/Projects/compfitition-2.1/base_app/styles/base_template.cssm", "line_map": {"16": 0, "32": 17, "33": 17, "22": 1, "23": 7, "39": 33, "31": 11}}
__M_END_METADATA
"""
