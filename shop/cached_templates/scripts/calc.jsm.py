# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389308004.208106
_enable_loop = True
_template_filename = 'C:\\myStuff\\calculator\\scripts/calc.jsm'
_template_uri = 'calc.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('// enable the buttons\n$(function() {\n  // load log click\n  $(\'#load-calculator-log\').click(function() {\n    $(\'#calculator-log\').load(\'/calculator/calc__loadlog/\');\n  });//click\n\n  // delete log click\n  $(\'#delete-calculator-log\').click(function() {\n    $(\'#calculator-log\').load(\'/calculator/calc__deletelog/\');\n  });//click\n\n\n  // note the embedded Python here\n  console.log("Hello from calc.jsm: 2 + 2 = ')
        # SOURCE LINE 15
        __M_writer(str( 2 + 2 ))
        __M_writer('");\n\n});//func\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


