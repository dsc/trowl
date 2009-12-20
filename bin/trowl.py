#!/usr/bin/env python
# encoding: utf-8
__author__    = 'David Schoonover <david@clearspring.com>'
__date__      = '2009-12-19'
__copyright__ = 'Copyright (c) 2009 Clearspring Technologies, Inc. All rights reserved.'
__version__   = (0, 0, 1)

import sys




def main():
    from optparse import OptionParser

    parser = OptionParser(
        usage   = 'usage: %prog [options] [config]', 
        version = '%prog'+" %i.%i.%i" % __version__)
    parser.add_option("-W", "--workers", default=4, type="int",
        help="Number of workers to start. [default: %default]")
    
    
    (options, args) = parser.parse_args()
    
    
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
