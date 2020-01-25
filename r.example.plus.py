#!/usr/bin/env python

"""
MODULE:    r.example.plus

AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>

PURPOSE:   Add two raster maps (an example of a module in Python)

COPYRIGHT: (C) 2018 by Vaclav Petras and the GRASS Development Team

This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.
"""

#%module
#% description: Adds the values of two rasters (A + B)
#% keyword: raster
#% keyword: algebra
#% keyword: sum
#%end
#%option G_OPT_R_INPUT
#% key: araster
#% description: Name of input raster A in an expression A + B
#%end
#%option G_OPT_R_INPUT
#% key: braster
#% description: Name of input raster B in an expression A + B
#%end
#%option G_OPT_R_OUTPUT
#%end


import sys

import grass.script as gs


def main():
    options, flags = gs.parser()
    araster = options['araster']
    braster = options['braster']
    output = options['output']

    gs.mapcalc('{r} = {a} + {b}'.format(r=output, a=araster, b=braster))

    return 0


if __name__ == "__main__":
    sys.exit(main())
