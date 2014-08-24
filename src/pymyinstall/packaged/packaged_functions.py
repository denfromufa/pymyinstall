#-*- coding: utf-8 -*-
"""
Helpers to install many modules for a specific usage.
"""
from ..installhelper.install_cmd import run_cmd, ModuleInstall, unzip_files, add_shortcut_to_desktop_for_module
from .packaged_config import complete_installation, small_installation
    
def datascientist(  folder          = "install", 
                    modules         = True, 
                    website         = True, 
                    scite           = True,
                    pandoc          = True,
                    ipython         = True,
                    sqlitespy       = True,
                    shortcuts       = True,
                    ipython_folder  = ".",
                    fLOG            = print,
                    browser         = None,
                    skip            = [],
                    full            = False,
                    additional_path = []):
    """
    
    install all necessary modules for a data scientist
    
    @param      additional_path     additional paths to add to ipython
    @param      folder              where to install everything
    @param      modules             go through the list of necessary modules
    @param      website             open website when the routine to install a software is not implemented yet
    @param      scite               install Scite (and modify the config file to remove tab, adjust python path)
    @param      ipython             setup ipython
    @param      ipython_folder      current folder for ipython
    @param      sqlitespy           install SQLiteSpy
    @param      pandoc              install pandoc
    @param      shortcuts           add shortcuts on the desktop (scite, ipython, spyder)
    @param      browser             browser to use for the notebooks if not the default one (ie, firefox, chrome)
    @param      skip                to skip some modules if they fail
    @param      full                if True, install many modules including the ones used to generate the documentation
    
    @example(Install manything for a Data Scientist)
    @code
    from pymyinstall import datascientist
    datascientist ("install", full=True)
    @endcode
    @endexample
    
    If you run this command from the python interpreter::
    
        >>> from pymyinstall import datascientist
        >>> datascientist ("install")
        
    The module installed with pip do not appear in the list of available modules
    unless the python interpreter is started again. The best way is to run those two commands
    from the Python IDLE and to restart the interpreter before a second run.
    The second time, the function does not install again what was already installed.
    
    """
    if modules :
        modules = complete_installation() if full else small_installation() 
        for _ in modules :
            if _.name in skip or _.mname in skip :
                fLOG("skip module", _.name, " import name:", _.mname)
            else :
                _.install(temp_folder=folder)    

    if website :
        get_install_list()
        
    if scite :
        scite = install_scite(folder, fLOG = fLOG)
    
    if pandoc :
        install_pandoc(folder, fLOG = fLOG)
        
    if ipython :
        setup_ipython(ipython_folder, additional_path=additional_path, browser = browser)
        
    if sqlitespy:
        sqlitespy_file = install_sqlitespy(folder, fLOG = fLOG)
        
    if shortcuts :
        if ipython  : add_shortcut_to_desktop_for_ipython(ipython_folder)
        if scite    : add_shortcut_to_desktop_for_scite(scite)
        if ipython  : add_shortcut_to_desktop_for_module("spyder")
        if sqlitespy: add_shortcut_to_desktop_for_sqlitespy(sqlitespy_file)
    