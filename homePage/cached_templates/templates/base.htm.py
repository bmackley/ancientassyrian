# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455050976.627365
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/homePage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'head', 'nav', 'content']


import datetime 

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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def nav():
            return render_nav(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        __M_writer('\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n<!--\n<footer class="page-footer">\n  <div class="container">\n    <div class="row">\n      <div class="col l6 s12">\n        <h5 class="white-text">Footer Content</h5>\n        <p class="grey-text text-lighten-4">You can use rows and columns here to organize your footer content.</p>\n      </div>\n      <div class="col l4 offset-l2 s12">\n        <h5 class="white-text">Links</h5>\n        <ul>\n          <li><a class="grey-text text-lighten-3" href="#!">Link 1</a></li>\n          <li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>\n          <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>\n          <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li>\n        </ul>\n      </div>\n    </div>\n  </div>\n  <div class="footer-copyright">\n    <div class="container">\n    ')
        __M_writer('\n      &copy; ')
        __M_writer(str(datetime.datetime.year))
        __M_writer(' AssyrianProject\n    <a class="grey-text text-lighten-4 right" href="#!">More Links</a>\n    </div>\n  </div>\n</footer>\n-->\n <script src="/static/homePage/js/lib/modernizr-2.min.js"> </script>\n  <script src="/static/homePage/js/materialize.js"> </script>\n   <script src="/static/homePage/js/tipped.js"> </script>\n   <script src="/static/homePage/js/jquery.qtip.js"> </script>\n   <script src="/static/homePage/js/login-check.js"></script>\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def head():
            return render_head(context)
        def nav():
            return render_nav(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<head>\n  <meta charset="UTF-8" />\n\n  <title>Hotspot</title>\n\n  <meta name="description" content="" />\n  <meta name="keywords" value="" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n \t<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n  <link rel="stylesheet" href="/static/homePage/css/layout.css" type="text/css" />\n  <link rel="stylesheet" href="/static/homePage/css/hotspot-map-editor.css" type="text/css" />\n  <!--<link rel="stylesheet" href="/static/homePage/css/hotspot-map.min.css" type="text/css" />-->\n  <link rel="stylesheet" href="/static/homePage/css/materialize.css" type="text/css" />\n  <link rel="stylesheet" href="/static/homePage/css/tipped.css" type="text/css" />\n  <link rel="stylesheet" href="/static/homePage/css/jquery.qtip.css" type="text/css" />\n  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">\n   <link rel="stylesheet" href="/static/homePage/css/screen.css" type="text/css" />\n     <style>\n#draggable1, #draggable2, #draggable3 { width: 100px; height: 100px; padding: 0.5em; float: left; margin: 10px 10px 10px 0; }\n#droppable { width: 300px; height: 300px; padding: 0.5em; float: left; margin: 10px; }\n</style>\n<script>\n\n</script>\n  <body>\n</head>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def nav():
            return render_nav(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- Dropdown Structure -->\n  <ul id="dropdown1" class="dropdown-content">\n    <li><a href="/homePage/profile">Profile</a></li>\n    <li><a href="/homePage/index/logout">Logout</a></li>\n    <li><a href="/homePage/hotspots">Hotspots</a></li>\n  </ul>\n  <nav>\n   <div class="nav-wrapper black">\n     <div class="row">\n        <div class="col s3 offset-s1 m3 offset-m3 l3 offset-l1 grid-example"><a href="/" class="brand-logo">Tablet Ninjas</a></div>\n         <div class="col s2 offset-s10 m3 offset-m8 l3 offset-l8 grid-example">  \n          <ul id="nav-mobile" class="right">\n')
        if request.user.is_authenticated():
            __M_writer('              <li><a class="dropdown-button" href="#!" data-activates="dropdown1">')
            __M_writer(str(user))
            __M_writer('<i class="fa fa-user fa-lg material-icons left"></i><i class="material-icons right">arrow_drop_down</i></a></li>\n')
        else:
            __M_writer('                <li><a class="waves-effect waves-light btn-flat white-text modal-trigger" href="#modal2">Sign Up</a></li>\n               <li><a class="modal-trigger" href="#modal4">Login</a></li>\n')
        __M_writer('            <li></li>\n          </ul>\n        </div>\n      </div>\n    </div>\n  </nav>\n  <!--Sign In MODAL --> \n    <div id="modal4" class="modal">\n     <div class="modal-content">\n     <h1 style ="color: black;"> Login to Your Account </h1>\n        <form method ="POST" action = "/homePage/login">\n        <div class="row">\n          <div class="input-field col s12">\n            <label for="id_username">Username:</label><input class="form-control" id="id_username" name="username" type="text" />\n          </div>\n          <div class="input-field col s12">\n            <label for="id_password">Password:</label><input class="form-control" id="id_password" name="password" type="password" />\n          </div>\n        </div>\n         <button class="btn waves-effect waves-light grey darken-1" id="login_submit" type="submit" value ="submit" name="action">Submit\n                  </button> \n        </form>\n      </div>\n    </div>\n\n  <!-- Create Account MODAL --> \n    <div id="modal2" class="modal">\n     <div class="modal-content">\n      <h1 style ="color: black;"> Create Account </h1>\n        <form method ="POST" id="create_form" action = "/homePage/create_user">\n         <div class="input-field col s12">\n          <tr><th><label for="id_username">Username:</label></th><td><input class="form-control" id="id_create_username" name="username" type="text" /></td></tr>\n        </div>\n         <div class="input-field col s12">\n<tr><th><label for="id_email">Email:</label></th><td><input class="form-control" id="id_email" name="email" type="text" /></td></tr>\n        </div>\n         <div class="input-field col s12">\n\n<tr><th><label for="id_password">Password:</label></th><td><input class="form-control" id="id_create_password" name="password" type="password" /></td></tr>\n        </div>\n         <div class="input-field col s12">\n<tr><th><label for="id_retypepassword">Re-Enter Password:</label></th><td><input class="form-control" id="id_retypepassword" name="retypepassword" type="password" /></td></tr>\n        </div>\n          <button class="btn waves-effect waves-light grey darken-1" id="create_user_submit" type="submit" name="action">Submit\n         </button> \n        </form>\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n \n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"51": 102, "66": 108, "129": 104, "72": 108, "73": 130, "74": 131, "75": 131, "81": 6, "110": 34, "91": 6, "30": 0, "96": 101, "102": 34, "17": 130, "135": 129, "45": 1, "46": 3, "111": 47, "112": 48, "113": 48, "114": 48, "115": 49, "116": 50, "117": 53, "56": 106, "123": 104}, "source_encoding": "ascii", "filename": "/Users/benmackley/Projects/history/homePage/templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
