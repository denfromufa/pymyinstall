#-*- coding: utf-8 -*-
"""
@file
@brief Run some checkings about the distribution

.. versionadded:: 1.3
"""
from __future__ import print_function

import os
import sys

from .win_exception import WinInstallDistributionError

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def distribution_checkings(python_path, tools_path, fLOG=print):
    """
    checks a distribution was properly executed

    @param      python_path     path for python
    @param      tools_path      path for tools
    @param      fLOG            logging function

    The function raises @see cl WinInstallDistributionError if an issue is detected.

    If *python_path* is None, it is replace by ``os.path.dirname(sys.executable)``.

    .. versionadded:: 1.3
    """
    exceptions = []
    files_to_check = ["jupyter-console.exe", "jupyter-qtconsole.exe",
                      "jupyter-notebook.exe", "jupyter.exe"]

    if python_path is None:
        python_path = os.path.dirname(sys.executable)
    pip = os.path.join(python_path, "pip.exe")
    if not os.path.exists(pip):
        scripts = os.path.join(python_path, "Scripts")
        files_to_check.extend(
            ["rodeo.exe", "spyder.exe", "pip.exe", "autopep8.exe"])
    else:
        scripts = python_path

    #############################################
    # check Jupyter, Rodeo, numpy works properly
    #############################################
    if sys.platform.startswith("win"):
        for file in files_to_check:
            f = os.path.join(scripts, file)
            if not os.path.exists(f):
                try:
                    raise FileNotFoundError(f)
                except Exception as e:
                    exceptions.append(e)

    ########
    # final
    ########
    if len(exceptions) > 0:
        typstr = str  # unicode#
        errors = "\n----\n".join("{0}\n{1}".format(type(_), typstr(_))
                                 for _ in exceptions)
        raise WinInstallDistributionError("\n" + errors)
