# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389308004.184105
_enable_loop = True
_template_filename = 'C:\\myStuff\\calculator\\styles/calc.cssm'
_template_uri = 'calc.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('/* Nothing here yet */')
        return ''
    finally:
        context.caller_stack._pop_frame()


