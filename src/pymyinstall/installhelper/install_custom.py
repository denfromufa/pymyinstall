# coding: latin-1
"""
@file
@brief Various functions to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
from __future__ import print_function

import os
import sys
if sys.version_info[0] == 2:
    import urllib2 as urllib_request
    import urllib2 as urllib_error
    import httplib as http_client
else:
    import urllib.request as urllib_request
    import urllib.error as urllib_error
    import http.client as http_client

from .module_install import ModuleInstall
from .install_memoize import install_memoize


@install_memoize
def download_page(url):
    """
    download a page from a url

    @param      url     url
    @return             content
    """
    try:
        req = urllib_request.Request(
            url, headers={
                'User-agent': 'Mozilla/5.0'})
        u = urllib_request.urlopen(req)
        text = u.read()
        u.close()
    except urllib_error.HTTPError as e:
        raise Exception("unable to get archive from: " + url) from e

    typstr = str  # unicode#
    return typstr(text, encoding="utf8")


def download_file(url, outfile):
    """
    download a file from a url, the function does not download the file
    again if outfile already exists

    @param      url         url
    @param      outfile     outfile
    @return                 outfile
    """
    if os.path.exists(outfile):
        return outfile

    try:
        req = urllib_request.Request(
            url,
            headers={
                'User-agent': 'Mozilla/5.0'},
        )
        u = urllib_request.urlopen(req)
        text = u.read()
        u.close()
    except urllib_error.HTTPError as e:
        raise Exception("unable to get archive from: " + url) from e
    except http_client.IncompleteRead as ee:
        raise Exception("unable to complete reading from: " + url) from ee

    with open(outfile, "wb") as f:
        f.write(text)

    return outfile


def download_from_sourceforge(url, outfile, fLOG=print, temp_folder="."):
    """
    download a file from a url using redirection,
    the function does not download the file
    again if outfile already exists

    @param      url         url
    @param      outfile     outfile
    @param      fLOG        logging function
    @param      temp_folder only used if installation of module requests is needed
    @return                 outfile

    The function will install module `requests <http://docs.python-requests.org/en/latest/>`_
    if not present.
    """
    if os.path.exists(outfile):
        return outfile

    try:
        import requests
    except ImportError:
        fLOG("installing module requests")
        ModuleInstall("requests", fLOG=fLOG).install(temp_folder=temp_folder)
        import requests

    try:
        req = requests.get(url, allow_redirects=True, stream=True)
        text = req.raw.read()
        fLOG("len ", len(text))
    except urllib_error.HTTPError as e:
        raise Exception("unable to get archive from: " + url) from e
    except requests.exceptions.ConnectionError as ee:
        raise Exception("unable to get archive from: " + url) from ee

    if len(text) < 20 and text.decode(
            "ascii").lower().startswith("bad request"):
        raise Exception("Bad Request for url: " + url)

    with open(outfile, "wb") as f:
        f.write(text)

    return outfile
