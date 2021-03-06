#-*- coding: utf-8 -*-
import sys
import os
import datetime
import re
import sphinx_readable_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables

set_sphinx_variables(__file__, "pymyinstall", "Xavier Dupré", 2016,
                     "readable", sphinx_readable_theme.get_html_theme_path(),
                     locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pymyinstall/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/"
