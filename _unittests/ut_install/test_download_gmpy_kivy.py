"""
@brief      test log(time=60s)

skip this test for regular run
"""

import sys
import os
import unittest

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
    import pyquickhelper


from src.pymyinstall.installhelper.module_install import ModuleInstall
from pyquickhelper import fLOG, get_temp_folder


class TestDownload2 (unittest.TestCase):

    def test_install_gmpy2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_gmpy2")

        if sys.platform.startswith("win"):
            m = ModuleInstall("gmpy2", "wheel", fLOG=fLOG)
            whl = m.download(temp_folder=temp)
            assert os.path.exists(whl)

    def test_install_kivy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = get_temp_folder(__file__, "temp_download_kivy")

        if sys.platform.startswith("win"):
            m = ModuleInstall("Kivy", "wheel", mname="kivy", fLOG=fLOG)
            whl = m.download(temp_folder=temp)
            assert os.path.exists(whl)


if __name__ == "__main__":
    unittest.main()