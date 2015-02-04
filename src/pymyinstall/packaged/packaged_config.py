"""
@file
@brief Defines different set of modules to install.
"""
import sys
from ..installhelper.module_install import ModuleInstall

def small_installation():
    """
    returns a list of modules to work with pandas, numpy, ipython, ...

    @return             a list of modules to install

    To install them:
    @code
    for _ in complete_installation() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = [
                #ModuleInstall("setuptools",     "wheel"),        # removed with 3.4
                #ModuleInstall("pip",            "wheel"),            # removed with 3.4
                #
                ModuleInstall("six",            "pip"),
                ModuleInstall("lxml",           "wheel"),
                ModuleInstall("jinja2",         "pip"),
                ModuleInstall("pygments",       "pip"),
                ModuleInstall("pyparsing",      "pip"),
                ModuleInstall("python-dateutil","pip", "dateutil"),
                ModuleInstall("html5lib",       "pip"),
                ModuleInstall("beautifulsoup4", "pip", mname="bs4"),
                ModuleInstall("coverage",       "pip"),
                ModuleInstall("pytz",           "pip"),
                ModuleInstall("pyreadline",     "pip",mname="pyreadline"),
                ModuleInstall("husl",           "pip"),
                #
                ModuleInstall("openpyxl",       "pip", version="1.8.6"),
                ModuleInstall("xlrd",           "pip"),
                #
                ModuleInstall("tornado",        "wheel"),
                ModuleInstall("pyzmq",          "wheel", mname="zmq"),
                #
                ModuleInstall("pycparser",      "wheel"),
                ModuleInstall("Cython",         "wheel"),
                ModuleInstall("numpy",          "wheel"),
                ModuleInstall("matplotlib",     "wheel"),
                ModuleInstall("seaborn",        "pip"),
                ModuleInstall("scipy",          "wheel"),
                ModuleInstall("statsmodels",    "wheel"),  # needs scipy
                ModuleInstall("networkx",       "wheel"),
                ModuleInstall("graphviz",       "pip"),
                #
                ModuleInstall("pandas",         "wheel"),
                ModuleInstall("scikit-learn",   "wheel", mname="sklearn"),
                ModuleInstall("ipython",        "pip", mname="IPython"),
                #
                ModuleInstall("ggplot",         "pip"),  # needs statsmodels
                ModuleInstall("mpld3",          "pip"),
                #
                ModuleInstall("pyquickhelper",  "github", "sdpython"),
                ModuleInstall("pyensae",        "github", "sdpython"),
                ModuleInstall("ensae_teaching_cs", "github", "sdpython"),
                #
                ModuleInstall("typecheck-decorator", "github", "prechelt", mname="typecheck"),
                #
                ModuleInstall("requests",       "pip"),
                #ModuleInstall("PyQt",           "wheel", mname="PyQt4"),
                ModuleInstall("PySide",         "wheel"),
                ModuleInstall("spyder",         "wheel", script="spyder.bat"),
                #
                #
                ModuleInstall("dbfread",        "pip"),   # to read dbase format
                ModuleInstall("xmltodict",      "pip"),   # XML to JSON
                ModuleInstall("ansiconv",       "pip"),   # shell to plain
                ModuleInstall("ansi2html",      "pip"),   # shell to HTML
                #
                ModuleInstall("nodeenv",        "pip"),   # node.js
                ]

    if sys.platform.startswith("win"):
        mod.append ( ModuleInstall("pywin32",   "wheel", mname = "win32com") )
        mod.append ( ModuleInstall("winshell",  "pip") )

    return mod

def complete_installation():
    """
    returns a list of modules to install, an rich set
    to work with data and more

    @return             a list of modules to install

    To install them:
    @code
    for _ in complete_installation() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = [
                ModuleInstall("virtualenv",     "wheel"),
                #ModuleInstall("setuptools",     "wheel"),                # removed with 3.4
                #ModuleInstall("pip",            "wheel"),                    # removed with 3.4
                ModuleInstall("typecheck-decorator", "pip", mname="typecheck"),
                #
                ModuleInstall("six",            "pip"),
                ModuleInstall("lxml",           "wheel"),
                ModuleInstall("jinja2",         "pip"),
                ModuleInstall("pygments",       "pip"),
                ModuleInstall("pyparsing",      "pip"),
                ModuleInstall("python-dateutil","pip", "dateutil"),
                ModuleInstall("html5lib",       "pip"),
                ModuleInstall("beautifulsoup4", "pip", mname="bs4"),
                ModuleInstall("coverage",       "pip"),
                ModuleInstall("pytz",           "pip"),
                ModuleInstall("SQLAlchemy",     "wheel", mname="sqlalchemy"),
                ModuleInstall("flask-sqlalchemy","pip",mname="flask.ext.sqlalchemy"),
                ModuleInstall("pyreadline",     "pip",mname="pyreadline"),
                ModuleInstall("simplejson",     "wheel"),
                ModuleInstall("husl",           "pip"),
                #
                ModuleInstall("openpyxl",       "pip", version="1.8.6"),
                ModuleInstall("python-pptx",    "github", "sdpython"),
                ModuleInstall("XlsxWriter",     "pip", mname="xlsxwriter"),
                #
                ModuleInstall("tornado",        "wheel"),
                ModuleInstall("flask",          "pip"),
                ModuleInstall("pyzmq",          "wheel", mname="zmq"),
                #
                ModuleInstall("pycparser",      "wheel"),
                ModuleInstall("Cython",         "wheel"),
                ModuleInstall("cffi",           "wheel"),
                ModuleInstall("numpy",          "wheel"),
                ModuleInstall("blaze",          "wheel"),
                ModuleInstall("scipy",          "wheel"),
                ModuleInstall("matplotlib",     "wheel"),
                ModuleInstall("seaborn",        "pip"),
                ModuleInstall("tables",         "wheel"),
                ModuleInstall("sympy",          "pip"),
                ModuleInstall("gmpy2",          "wheel"),
                ModuleInstall("llvmpy",         "wheel", mname="llvm"),
                ModuleInstall("numba",          "wheel"),
                ModuleInstall("networkx",       "wheel"),
                ModuleInstall("graphviz",       "pip"),
                #
                ModuleInstall("pandas",         "wheel"),
                ModuleInstall("scikit-learn",   "wheel", mname="sklearn"),
                ModuleInstall("scikit-image",   "wheel", mname="skimage"),
                ModuleInstall("patsy",          "pip"),
                ModuleInstall("statsmodels",    "wheel"),  # needs scipy
                ModuleInstall("ipython",        "wheel", mname="IPython"),
                ModuleInstall("cvxopt",         "wheel"),
                ModuleInstall("pymc",           "wheel"),
                ModuleInstall("PyWavelets",     "wheel", mname="pywt"),
                ModuleInstall("fastcluster",    "wheel"),
                #
                ModuleInstall("ggplot",         "pip"),  # needs statsmodels
                ModuleInstall("d3py",           "github", "sdpython"),
                ModuleInstall("mpld3",          "pip"),
                ModuleInstall("prettyplotlib",  "pip"),
                ModuleInstall("bokeh",          "pip"),
                ModuleInstall("pyshp",          "pip", mname="shapefile"), # needed by shapely
                ModuleInstall("Shapely",        "wheel", mname="shapely"),  # exe on Windows to get geos.dll
                ModuleInstall("vispy",          "pip"),
                #
                #ModuleInstall("tessera-client", "github", "sdpython", mname="tessera_client"),
                #ModuleInstall("tessera",        "github", "sdpython"),   # does not really work yet
                #
                ModuleInstall("rpy2",           "wheel"),
                #ModuleInstall("pythonnet",      "wheel", mname="clr"),  # included in ensae_teaching_cs
                #
                ModuleInstall("pyquickhelper",  "github", "sdpython"),
                ModuleInstall("pyensae",        "github", "sdpython"),
                ModuleInstall("ensae_teaching_cs", "github", "sdpython"),
                #
                ModuleInstall("typecheck-decorator", "github", "prechelt", mname="typecheck"),
                #
                ModuleInstall("selenium",       "pip"),
                ModuleInstall("Pillow",         "wheel", mname = "PIL"),
                ModuleInstall("pygame",         "wheel"),
                ModuleInstall("markupsafe",     "pip"),
                ModuleInstall("requests",       "pip"),
                ModuleInstall("Kivy",           "wheel", mname="kivy"),
                #ModuleInstall("PyQt",           "wheel", mname="PyQt4"),
                ModuleInstall("PySide",         "wheel"),
                ModuleInstall("spyder",         "wheel", script="spyder.bat"),
                #
                ModuleInstall("py4j",           "pip"),
                ModuleInstall("python-igraph",  "wheel", mname="igraph"),
                #
                ModuleInstall("luigi",          "pip"),
                #
                #ModuleInstall("Cartopy",        "wheel", mname="cartopy"),
                ModuleInstall("smopy",          "pip"),
                ModuleInstall("folium",         "github", "sdpython"),
                ModuleInstall("basemap",        "wheel", mname="mpl_toolkits.basemap"),
                #
                ModuleInstall("sphinx",         "pip"),
                ModuleInstall("sphinxcontrib-fancybox",     "pip", mname="sphinxcontrib.fancybox"),
                ModuleInstall("sphinx_rtd_theme",           "pip"),
                ModuleInstall("sphinxjp.themes.basicstrap", "pip"),
                ModuleInstall("solar_theme",                "pip"),
                ModuleInstall("cloud_sptheme",              "pip"),
                ModuleInstall("sphinx_readable_theme",      "pip"),
                ModuleInstall("hachibee-sphinx-theme",      "pip", mname="hachibee_sphinx_theme"),
                ModuleInstall("wild_sphinx_theme",          "pip"),
                ModuleInstall("sphinx_bootstrap_theme",     "pip"),
                ModuleInstall("sphinxjp.themes.sphinxjp",   "pip"),
                ModuleInstall("sphinxjp.themes.revealjs",   "github", "sdpython"),

                #
                ModuleInstall("dbfread",                    "pip"),   # to read dbase format
                ModuleInstall("xmltodict",                  "pip"),   # XML to JSON
                ModuleInstall("python-linkedin",            "github", "sdpython", mname="linkedin"),   # access to linkedin
                ModuleInstall("requests_oauthlib",          "pip"),
                ModuleInstall("antlr4-python3-runtime",     "pip", mname="antlr4"),
                #ModuleInstall("unqlite",                    "pip"),   # key/value store (NoSQL)
                #ModuleInstall("typecheck-decorator",        "pip", mname="typecheck"),
                ModuleInstall("pycontracts",                "pip", mname="contracts"),
                ModuleInstall("ansiconv",                   "pip"),   # shell to plain
                ModuleInstall("ansi2html",                  "pip"),   # shell to HTML
                ModuleInstall("feedparser",                 "pip"),   # to parse RSS streams

                #
                ModuleInstall("ecdsa",                      "pip"),
                ModuleInstall("pycrypto",                   "exe_xd", mname="Crypto"),
                ModuleInstall("paramiko",                   "pip"),
                #
                ModuleInstall("pattern", "pip") if sys.version_info[0] < 3 else None,   # to read dbase format
                #
                ModuleInstall("nodeenv",                    "pip"),   # node.js
                ModuleInstall("python-jenkins",             "pip", mname="jenkins"),  # for Jenkins
                ModuleInstall("psutil",                     "wheel"),  #
                #
                #ModuleInstall("pyrsslocal", "github", "sdpython"),
                #ModuleInstall("python-nvd3", "github", "sdpython"),
                #ModuleInstall("splinter", "github", "cobrateam"),
                #ModuleInstall("pypdf2", "pip"),
                #ModuleInstall("pdfminer", "pip"),
                #ModuleInstall("liblinear",      "wheel"),
                #ModuleInstall("lsqfit",      "wheel"),
                #ModuleInstall("marisa-trie",      "wheel", mname="marisa_trie"),
                #ModuleInstall("boost_python",   "wheel"),
                ]

    if sys.platform.startswith("win"):
        mod.append ( ModuleInstall("pywin32",   "wheel", mname = "win32com") )
        mod.append ( ModuleInstall("winshell",  "pip") )

    return [ _ for _ in mod if _ is not None ]

def installation_cubes():
    """
    A cube is a multidimensional array.
    This functions gathers the dependencies for module `cubes <https://github.com/Stiivi/cubes>`_
    (`documentation <http://cubes.databrewery.org/dev/doc/>`_)
    and `cubesviewer <https://github.com/jjmontesl/cubesviewer>`_.

    """
    mod = [
                ModuleInstall("python-dateutil","pip", "dateutil"),
                ModuleInstall("django",         "pip"),
                ModuleInstall("pytz",           "pip"),
                ModuleInstall("jsonschema",     "pip"),
                ModuleInstall("cubes",          "github", "Stiivi"),  # the PyPI version does not work with Python 3
            ]

    return mod

def installation_huge_datasets():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
                ModuleInstall("h5py",           "wheel"),
                ModuleInstall("blosc",          "wheel"),
                ModuleInstall("numexpr",        "wheel"),
                ModuleInstall("tables",         "wheel"),
            ]

    return mod

def installation_azure():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
                ModuleInstall("azure",          "pip"),
            ]

    return mod