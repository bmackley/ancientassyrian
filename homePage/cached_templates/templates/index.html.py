# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455063700.615159
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/homePage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'nav']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def nav():
            return render_nav(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer('\n ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  this is content\n  <br>\n  <br>\n  <br>\n  <br>\n  <br>\n  <br>\n  this is even more content\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\n <link rel="stylesheet" href="/static/homePage/css/base.css" type="text/css" />\n    <br>\n    <div class="row">\n      <div class="col s2 offset-s8 m2 offset-m10 l2 offset-l10"><a class="waves-effect waves-light btn-flat white-text modal-trigger" href="#modal1">Login</a></div>\n    </div>\n    <div class="row">\n    </div>\n    <div class="row">\n    </div>\n    <div class="row">\n    </div>\n    <div class="row">\n    </div>\n     <div class="row">\n    </div>\n    <div class="row">\n    </div>\n\n    <div class="row">\n      <div class="col s8 offset-s2"><h1 class="valign"><center>Tablet Ninjas<center></h1></div>\n    </div>\n        <div class="row">\n    </div>\n    <div class="row">\n    </div>\n    <div class="row">\n    </div><div class="row">\n    </div>\n    <div class="row">\n    </div>\n    <div class="row">\n    </div>\n    <div>\n     <center>\n        <a class="waves-effect waves-light btn-large" href = "/homePage/index/about">Tell Me About It</a> &nbsp; &nbsp; <a class="waves-effect waves-light btn-large modal-trigger" href="#modal2">Create Account</a>\n      </center>\n    <div> \n\n    <!-- Create Account MODAL --> \n    <div id="modal2" class="modal">\n     <div class="modal-content">\n      <h1 style ="color: black;"> Create Account </h1>\n        <form method ="POST" id="create_account" action = "/homePage/create_user">\n          <span class="black-text">\n             <div class="input-field col s12">\n              <tr><th><label for="id_username">Username:</label></th><td><input class="form-control" id="id_create_username" name="username" type="text" /></td></tr>\n            </div>\n             <div class="input-field col s12">\n    <tr><th><label for="id_email">Email:</label></th><td><input class="form-control" id="id_email" name="email" type="text" /></td></tr>\n            </div>\n             <div class="input-field col s12">\n    <tr><th><label for="id_password">Password:</label></th><td><input class="form-control" id="id_create_password" name="password" type="password" /></td></tr>\n            </div>\n             <div class="input-field col s12">\n    <tr><th><label for="id_retypepassword">Re-Enter Password:</label></th><td><input class="form-control" id="id_retypepassword" name="retypepassword" type="password" /></td></tr>\n            </div>\n          </span>\n          <button class="btn waves-effect waves-light" id="create_user_submit" type="submit" name="action">Submit\n         </button> \n        </form>\n      </div>\n    </div>\n    <!--Sign In MODAL --> \n    <div id="modal1" class="modal">\n     <div class="modal-content">\n     <h1 style ="color: black;"> Login to Your Account </h1>\n        <form method ="POST" action = "/homePage/login">\n          <span class="black-text">\n          <div class="row">\n            <div class="input-field col s12">\n              <label for="id_username">Username:</label><input id="id_username" name="username" type="text" />\n            </div>\n            <div class="input-field col s12">\n              <label for="id_password">Password:</label><input id="id_password" name="password" type="password" />\n            </div>\n          </div>\n           <button class="btn waves-effect waves-light grey darken-1" type="submit" value ="submit" name="action">Submit\n                    </button> \n          </span>\n        </form>\n      </div>\n    </div>\n    <!--Not Logged IN notice --> \n    <div id="modal3" class="modal">\n     <div class="modal-content">\n     <h1 style ="color: black;"> You are not logged in. Would you like to log in now? </h1>\n    </div> <!--not logged in-->\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/history/homePage/templates/index.html", "source_encoding": "ascii", "line_map": {"65": 2, "59": 91, "37": 1, "38": 1, "71": 2, "43": 90, "28": 0, "77": 71, "53": 91}, "uri": "index.html"}
__M_END_METADATA
"""
