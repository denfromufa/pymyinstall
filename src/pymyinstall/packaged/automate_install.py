"""
@file
@brief Install or update all packages.
"""
import os
from ..installhelper import ModuleInstall, has_pip, update_pip
from .packaged_config_full_set import ensae_fullset


def _build_reverse_index():
    """
    builds a reverse index of the module,
    """
    res = {}
    mods = ensae_fullset()
    for m in mods:
        res[m.name] = m
        if m.mname is not None:
            res[m.mname] = m
    return res


_reverse_module_index = _build_reverse_index()


def find_module_install(name):
    """
    checks if there are specific instructions to run before installing module *name*,
    on Windows, some modules requires compilation, if not uses default option with *pip*

    @param      name        module name, the name can include a specific version number with '=='
    @return                 @see cl ModuleInstall
    """
    if '=' in name:
        spl = name.split('==')
        if len(spl) != 2:
            raise ValueError("unable to interpret " + name)
        name = spl[0]
        version = spl[1]
    else:
        version = None

    if name in _reverse_module_index:
        mod = _reverse_module_index[name]
    else:
        mod = ModuleInstall(name, "pip")

    if version is not None:
        mod.version = version
    return mod


def reorder_module_list(list_module):
    """
    reorder a list of modules to install, a module at position *p*
    should not depend not module at position *p+1*

    @param      list_module     list of module (@see cl ModuleInstall)
    @return                     list of modules

    The function uses modules stored in :mod:`pyminstall.packaged.packaged_config`,
    it does not go to pypi. If a module was not registered, it will be placed
    at the end in the order it was given to this function.
    """
    inset = {m.name: m for m in list_module}
    res = []
    for mod in ensae_fullset():
        if mod.name in inset:
            res.append(mod.copy(version=inset[mod.name].version))
            inset[mod.name] = None
    for mod in list_module:
        if inset[mod.name] is not None:
            res.append(mod)
    return res


def update_all(temp_folder=".", fLOG=print, verbose=True,
               list_module=None, reorder=True,
               skip_module=None):
    """
    update modules in *list_module*
    if None, this list will be returned by @see fn ensae_fullset,
    the function starts by updating pip.

    @param  temp_folder     temporary folder
    @param  verbose         more display
    @param  list_module     None or of list of str or @see cl ModuleInstall
    @param  fLOG            logging function
    @param  reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param  skip_module     module to skip (list of str)
    """
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        from .get_pip import main
        main()

    if skip_module is None:
        skip_module = []

    if list_module is None:
        from ..packaged import ensae_fullset
        list_module = ensae_fullset()
    else:
        list_module = [find_module_install(mod) if isinstance(
            mod, str) else mod for mod in list_module]

    list_module = [_ for _ in list_module if _.name not in skip_module]

    if reorder:
        list_module = reorder_module_list(list_module)

    if verbose:
        fLOG("update pip if needed")
    update_pip()
    modules = list_module
    again = []
    for mod in modules:
        if verbose:
            fLOG("check module: ", mod.name)
        if mod.is_installed() and mod.has_update():
            ver = mod.get_pypi_version()
            inst = mod.get_installed_version()
            m = "    - updating module  {0} --- {1} --> {2} (kind={3})" \
                .format(mod.name, inst, ver, mod.kind)
            fLOG(m)
            b = mod.update(temp_folder=temp_folder, log=verbose)
            if b:
                again.append(m)

    if verbose:
        fLOG("")
        fLOG("updated modules")
        for m in again:
            fLOG(m)


def install_all(temp_folder=".", fLOG=print, verbose=True,
                list_module=None, reorder=True, skip_module=None):
    """
    install modules in *list_module*
    if None, this list will be returned by @see fn ensae_fullset,
    the function starts by updating pip.

    @param  temp_folder     temporary folder
    @param  verbose         more display
    @param  list_module     None or of list of str or @see cl ModuleInstall
    @param  fLOG            logging function
    @param  reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param  skip_module     module to skip (list of str)
    """
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        fLOG("install pip")
        from .get_pip import main
        main()

    if skip_module is None:
        skip_module = []

    if list_module is None:
        from ..packaged import ensae_fullset
        list_module = ensae_fullset()
    else:
        list_module = [find_module_install(mod) if isinstance(
            mod, str) else mod for mod in list_module]

    list_module = [_ for _ in list_module if _.name not in skip_module]

    if reorder:
        list_module = reorder_module_list(list_module)

    if verbose:
        fLOG("update pip if needed")
    update_pip()

    modules = list_module
    again = []
    for mod in modules:
        if verbose:
            fLOG("check module: ", mod.name)
        if not mod.is_installed():
            ver = mod.version
            m = "    - installing module  {0} --- --> {1} (kind={2})" \
                .format(mod.name, ver, mod.kind)
            fLOG(m)
            b = mod.install(temp_folder=temp_folder, log=verbose)
            if b:
                again.append(m)

    if verbose:
        fLOG("")
        fLOG("installed modules")
        for m in again:
            fLOG(m)