#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
# -*- coding: iso-8859-1 -*-

"""An HTML writer supporting link to external documentation.

This module is a frontend for the Docutils_ HTML writer. It allows a document
to reference objects documented in the API documentation generated by
extraction tools such as Doxygen_ or Epydoc_.

.. _Docutils:   http://docutils.sourceforge.net/
.. _Doxygen:    http://www.doxygen.org/
.. _Epydoc:     http://epydoc.sourceforge.net/
"""

# $Id: apirst2html.py 1531 2007-02-18 23:07:25Z dvarrazzo $
__version__ = "$Revision: 1531 $"[11:-2]
__author__ = "Daniele Varrazzo"
__copyright__ = "Copyright (C) 2007 by Daniele Varrazzo"
__docformat__ = 'reStructuredText en'

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

# We have to do some path magic to prevent Python from getting
# confused about the difference between the ``epydoc.py`` script, and the
# real ``epydoc`` package.  So remove ``sys.path[0]``, which contains the
# directory of the script.
import sys, os.path
script_path = os.path.abspath(sys.path[0])
sys.path = [p for p in sys.path if os.path.abspath(p) != script_path]

import epydoc.docwriter.xlink as xlink

from docutils.core import publish_cmdline, default_description
description = ('Generates (X)HTML documents with API documentation links.  '
                + default_description)
publish_cmdline(reader=xlink.ApiLinkReader(), writer_name='html',
                description=description)
