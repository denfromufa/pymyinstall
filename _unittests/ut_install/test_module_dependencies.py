"""
@brief      test log(time=1s)
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
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper


from pyquickhelper import fLOG, get_temp_folder
from src.pymyinstall.installhelper import get_module_dependencies, get_module_metadata, version_consensus
from src.pymyinstall.installhelper.module_install_exceptions import WrongVersionError


class TestModuleDependencies (unittest.TestCase):

    def common_function(self, name, use_pip=False):
        res = get_module_dependencies(name, deep=True, use_pip=use_pip)
        for k, v in sorted(res.items()):
            assert isinstance(v, tuple)
            fLOG(k, "-->", v)
        if len(res) < 3:
            from pip import get_installed_distributions
            pkgs = get_installed_distributions(
                local_only=False, skip=[], use_pip=use_pip)
            req_map = dict((p.key, (p, p.requires())) for p in pkgs)
            mat = req_map.get(name, None)
            raise Exception(str(res) + "\n" +
                            str(get_module_metadata(name)) + "\n" + str(mat))

    def test_dependencies_matplotlib(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        self.common_function("matplotlib")

    def test_dependencies_ggplot(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        self.common_function("ggplot")

    def test_dependencies_ggplot_pip(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        self.common_function("ggplot", use_pip=True)

    def test_version_consensus(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertEqual(version_consensus('>=2.3', '>=2.4'), '>=2.4')
        self.assertEqual(version_consensus('>=2.5', '>=2.4'), '>=2.5')
        self.assertEqual(version_consensus('>2.3', '>2.4'), '>2.4')
        self.assertEqual(version_consensus('>2.5', '>2.4'), '>2.5')
        self.assertEqual(version_consensus('>=2.3', '>2.4'), '>2.4')
        self.assertEqual(version_consensus('>2.3', '>=2.4'), '>=2.4')
        self.assertEqual(version_consensus('>2.5', '>2.4'), '>2.5')
        self.assertEqual(version_consensus('>=2.5', '>2.4'), '>=2.5')
        self.assertEqual(version_consensus('>2.5', '>=2.4'), '>2.5')

        self.assertEqual(version_consensus('<=2.3', '<=2.4'), '<=2.3')
        self.assertEqual(version_consensus('<=2.5', '<=2.4'), '<=2.4')
        self.assertEqual(version_consensus('<2.3', '<2.4'), '<2.3')
        self.assertEqual(version_consensus('<2.5', '<2.4'), '<2.4')
        self.assertEqual(version_consensus('<=2.3', '<2.4'), '<=2.3')
        self.assertEqual(version_consensus('<2.3', '<=2.4'), '<2.3')
        self.assertEqual(version_consensus('<2.5', '<2.4'), '<2.4')
        self.assertEqual(version_consensus('<=2.5', '<2.4'), '<2.4')
        self.assertEqual(version_consensus('<2.5', '<=2.4'), '<=2.4')

        self.assertEqual(version_consensus('==2.3', '<=2.4'), '==2.3')
        self.assertEqual(version_consensus('<=2.5', '==2.4'), '==2.4')
        self.assertEqual(version_consensus('==2.3', '<2.4'), '==2.3')
        self.assertEqual(version_consensus('<2.5', '==2.4'), '==2.4')
        self.assertEqual(version_consensus('>2.3', '==2.4'), '==2.4')
        self.assertEqual(version_consensus('==2.5', '>2.4'), '==2.5')
        self.assertEqual(version_consensus('==2.5', '>2.4'), '==2.5')
        self.assertEqual(version_consensus('==2.5', '>=2.4'), '==2.5')

        try:
            version_consensus('<=2.3', '>=2.4')
        except WrongVersionError:
            pass

        try:
            version_consensus('<=2.3', '==2.4')
        except WrongVersionError:
            pass


if __name__ == "__main__":
    unittest.main()
