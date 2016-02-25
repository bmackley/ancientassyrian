# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455054072.774258
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/homePage/templates/create_chars.html'
_template_uri = 'create_chars.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'nav']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        charForm = context.get('charForm', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def nav():
            return render_nav(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
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
        charForm = context.get('charForm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="container">\n        <center>\n         <div class="row">\n          <form class="col s12" action="/homePage/create_chars" method="post">\n            <div class="row">\n                ')
        __M_writer(str( charForm ))
        __M_writer('\n                <input type="submit" value="Submit" />\n            </div>\n          </form>\n        </div>\n        </center>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\n  <!-- Dropdown Structure -->\n  <ul id="dropdown1" class="dropdown-content">\n    <li><a href="/homePage/profile">Profile</a></li>\n    <li><a href="/homePage/index/logout">Logout</a></li>\n    <li><a href="/homePage/hotspots">Hotspots</a></li>\n  </ul>\n  <nav>\n   <div class="nav-wrapper black">\n     <div class="row">\n        <div class="col s3 offset-s1 m3 offset-m3 l3 offset-l1 grid-example"><a href="/" class="brand-logo">Assyrian Project</a></div>\n         <div class="col s2 offset-s10 m3 offset-m8 l3 offset-l8 grid-example">  \n          <ul id="nav-mobile" class="right">\n')
        if request.user.is_authenticated():
            __M_writer('              <li><a class="dropdown-button" href="#!" data-activates="dropdown1">')
            __M_writer(str(user))
            __M_writer('<i class="fa fa-user fa-lg material-icons left"></i><i class="material-icons right">arrow_drop_down</i></a></li>\n')
        else:
            __M_writer('               <li><a class="modal-trigger" href="#modal4">Login</a></li>\n')
        __M_writer('            <li></li>\n          </ul>\n        </div>\n      </div>\n    </div>\n  </nav>\n  <!--Sign In MODAL --> \n    <div id="modal4" class="modal">\n     <div class="modal-content">\n     <h1 style ="color: black;"> Login to Your Account </h1>\n        <form method ="POST" id="sign_in" action = "/homePage/login">\n        <div class="row">\n          <div class="input-field col s12">\n            <label for="id_username">Username:</label><input class="form-control" id="id_username" name="username" type="text" />\n          </div>\n          <div class="input-field col s12">\n            <label for="id_password">Password:</label><input class="form-control" id="id_password" name="password" type="password" />\n          </div>\n        </div>\n         <button class="btn waves-effect waves-light grey darken-1" id="login_submit" type="submit" value ="submit" name="action">Submit\n                  </button> \n        </form>\n      </div>\n    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/history/homePage/templates/create_chars.html", "uri": "create_chars.html", "line_map": {"34": 45, "67": 2, "68": 15, "69": 16, "70": 16, "71": 16, "72": 17, "73": 18, "74": 20, "44": 46, "80": 74, "17": 0, "51": 46, "52": 53, "53": 53, "59": 2, "29": 1}, "source_encoding": "ascii"}
__M_END_METADATA
"""
