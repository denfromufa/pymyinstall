#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import re

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from src.pymyinstall.installhelper.module_install_page_wheel import extract_all_links, enumerate_links_module
from src.pymyinstall.installhelper.install_cmd_helper import python_version

if sys.version_info[0] == 2:
    from codecs import open


class TestRegex (unittest.TestCase):

    def test_links(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "data", "page1.html"))
        with open(data, "r", encoding="utf8") as f:
            content = f.read()

        links = extract_all_links(content)
        for l in links:
            if "heatmap" in l[0]:
                fLOG(l)
        assert len(links) > 0

        if not sys.platform.startswith("win"):
            return

        version = python_version()
        fLOG(version)
        plat = version[0] if version[0] == "win32" else version[1]
        if version[1] == '64bit' and version[0] == 'win32':
            plat = "amd64"
        version = sys.version_info

        ll = list(enumerate_links_module("heatmap", links, version, plat))
        fLOG(ll)
        if len(ll) != 1:
            raise Exception(str(ll))

    def test_1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = 'onclick=.javascript:dl[(]([,\[\]0-9]+) *, *.([0-9&;@?=:A-Zgtl]+).[)].' + \
                  ' title(.+)?.>(.+?-((cp34)|(py3)|(py2[.]py3)|(py33[.]py34))-none-((win_amd64)|(any)).whl)</a>'
        raw = """<li><a id='networkx'></a><strong><a href='http://networkx.lanl.gov/'>NetworkX</a></strong>, a package for complex networks.
                <ul>
                <li><a href='javascript:;' onclick='javascript:dl([97,46,45,116,111,57,50,114,101,112,120,49,53,104,51,107,121,106,119,110,55,108,47], "7D34&lt;?&gt;AFC83B47?:2;151;29@619@&gt;2C4C820C@1B=E")' title='[1.2&#160;MB] [Dec 24, 2014]'>networkx&#8209;1.9.1&#8209;py2.py3&#8209;none&#8209;any.whl</a></li>
                </ul>""".replace("&#8209;", "-")
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False

    def test_2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = '''onclick=.javascript:dl[(]([,\[\]0-9]+) *, *.([0-9&;@?=:A-Zgtl#]+).[)]. title(.+)?.>''' + \
                  '''(.+?-((cp34)|(py3)|(py2[.]py3)|(py34))-none-((win_amd64)|(any)).whl)</a>'''
        raw = """<li><a href='javascript:;' onclick='javascript:dl([45,111,46,119,109,108,112,104,105,50,51,120,110,118,48,47,52,99,53,102,121,101],""" + \
              """ "A7CD=&lt;@&lt;?5;450:2B2&#62;0A6:@0&lt;1&lt;E038&lt;:92375")' """ + \
              """title='[1.4&#160;MB] [Nov 30, 2015]'>lxml-3.5.0-cp34-none-win_amd64.whl</a></li>"""
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False

    def test_3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = '''onclick=.javascript:dl[(]([,\[\]0-9]+) *, *.([0-9&;@?=:A-Zgtl#]+).[)]. title(.+)?.>''' + \
                  '''(.+?-((cp34)|(py3)|(py2[.]py3)|(py34))(-none)?-((win_amd64)|(any))(.whl)?)</a>'''
        raw = """<li><a href='javascript:;' onclick='javascript:dl([120,53,99,109,95,100,122,51,46,97,119,117,110,57,54,104,47,106,52,48,105,101,108,111,116,45,112], "6;H;BA1=@F03FI7818CI2J7BI&lt;G&lt;EI:D&lt;4935&#62;B8:?F")' """ + \
              """title='[1.6&#160;MB] [Nov 30, 2015]'>lxml-3.5.0-cp34-win_amd64</a></li>"""
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False

    def test_4(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = "[-]([0-9]+[.][abc0-9]+([.][0-9])?([.][0-9abdevcr]+)?)([+][a-z]+)?" + \
                  "([+]cuda[0-9]{2,5})?([+]sdl[0-9])?([+]numpy[0-9]{1,2})?([+.]post[0-9]{1,2})?([.][0-9])?[-]"
        raw = """<li><a href='javascript:;' onclick='&nbsp;javascript:dl([111,86,99,110,98,105,57,52,54,109,100,102,53,116,104,106,45,112,88,119,51,97,95,46,67,50,108,48,47], """ + \
              """"=&#62;7?43;6LH1B2E303@KGKGIDG7@2AD&lt;@2AD&lt;9@C53FE9:87GC&#62;J")' title='[165&#160;KB] [Apr 21, 2016]'>CVXcanon-0.0.23.4-cp35-cp35m-win_amd64.whl</a></li>"""
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
