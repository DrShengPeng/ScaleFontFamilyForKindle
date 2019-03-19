#!/usr/bin/env python
# Usage
# CMD old-font-roman-only [scale]

import fontforge
import os
import psMat
import re
import sys

tgtHeight = 480.0

def reg_to_family(regNm, ext):
    if regNm.find("Regular") > 0:
        cn = re.sub('-?Regular','',regNm)
    elif regNm.find("Roman") > 0:
        cn = re.sub('-?Roman','',regNm)
    else:
        cn = regNm

    fam = [regNm + ext]
    #NB: add more naming variants
    tmpl = ["-Italic","-Bold","-BoldItalic","-Bold-Italic"]
    for v in tmpl:
        if os.path.isfile(cn + v + ext):
            print("file found: " + v)
            fam.append(cn+v+ext)
    return fam


fName   = sys.argv[1]

fNameStem, fNameExt = os.path.splitext(fName)
fam = reg_to_family(fNameStem, fNameExt)

font = fontforge.open(fName)
rxh = font.xHeight
font.close()

if len(sys.argv) == 3:
    scale = sys.argv[2]
else:
    xh = font.xHeight
    if xh > tgtHeight:
        scale = "1.100"
    else:
        scale = '{:1.3f}'.format(tgtHeight/rxh)

for f in fam:
    font = fontforge.open(f)
    font.em = 2048
    font.selection.all()
    font.transform(psMat.scale(float(scale)))
    fNameStem, fNameExt = os.path.splitext(f)
    sfNameStem = fNameStem + '-s' + scale
    font.generate(sfNameStem + fNameExt)
    font.close()
