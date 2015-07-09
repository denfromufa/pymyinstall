"""
@file
@brief Patch the distribution to make it portable
"""
from __future__ import print_function

import os


def win_patch_paths(folder, python_path, path_to_python="", fLOG=print):
    """
    path are absolute when they are installed,
    see `Create a portable Python with Pip on Windows <http://www.clemens-sielaff.com/create-a-portable-python-with-pip-on-windows/>`_

    @param      folder          folder when to find the executable
    @param      python_path     python path (string to replace)
    @param      path_to_python  new python path (replace by)
    @param      fLOG            logging function
    @return                     list of tuple ('exe or py', 'modified file')

    The first three parameter can be environment variables.
    They will be replaced by their values.
    """
    if folder in os.environ:
        folder = os.environ[folder]
    if python_path in os.environ:
        python_path = os.environ[python_path]
    if path_to_python in os.environ:
        path_to_python = os.environ[path_to_python]

    files = os.listdir(folder)

    if len(python_path) > 0 and not python_path.endswith("\\"):
        python_path += "\\"
    if len(path_to_python) > 0 and not path_to_python.endswith("\\"):
        path_to_python += "\\"

    shebang = "#!" + python_path + "python.exe"
    bshebang = bytes(shebang, encoding="ascii")
    into = "#!" + path_to_python + "python.exe"
    binto = bytes(into, encoding="ascii")

    operations = []
    for file in files:
        full = os.path.join(folder, file)
        if os.path.isfile(full):
            ext = os.path.splitext(full)[-1]

            if ext in {".py", ""}:
                with open(full, "r") as f:
                    content = f.read()
                if shebang in content:
                    content = content.replace(shebang, into)
                    fLOG("update ", full)
                    operations.append(("update", full))
                    with open(full, "w") as f:
                        f.write(content)
            elif ext == ".exe":
                with open(full, "rb") as f:
                    content = f.read()
                if bshebang in content:
                    content = content.replace(bshebang, binto)
                    fLOG("update ", full)
                    operations.append(("update", full))
                    with open(full, "wb") as f:
                        f.write(content)
            else:
                pass

    return operations
