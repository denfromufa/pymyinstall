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
    import pyquickhelper
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
    import pyquickhelper


from src.pymyinstall.installhelper.module_install import ModuleInstall
from pyquickhelper import fLOG


class TestRegex (unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()