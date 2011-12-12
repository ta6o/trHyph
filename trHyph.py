#!/usr/bin/env python
# -*- coding: utf-8  -*-

# ****************************************************************************
#  This program is free software; you can redistribute it and/or modify 
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# 
# ****************************************************************************

"""
trHyph.py is a python script for generating a TeX-compliant Turkish hyphenation pattern dictionary.
The script and the generated .dic file are both published under GNU General Public License.

Yakup Cetinkaya, December 2010
<ask@yakup.cc>

"""

import sys

consonants = [u"b",u"c",u"ç",u"d",u"f",u"g",u"ğ",u"h",u"j",u"k",u"l",u"m",u"n",u"p",u"r",u"s",u"ş",u"t",u"v",u"y",u"z"]
vowels = [u"a",u"e",u"ı",u"i",u"o",u"ö",u"u",u"ü"]
tokens = []

for i in range(0,len(vowels)):
	for j in range(0,len(vowels)):
		level = int(i==j)*2+1
		tokens.append(unicode(vowels[i]+str(level)+vowels[j]))

for i in range(0,len(consonants)):
	for j in range(0,len(vowels)):
		tokens.append(unicode(consonants[i]+"2"+vowels[j]+"1"))
		
for i in range(0,len(vowels)):
	for j in range(0,len(consonants)):
		for k in range(0,len(consonants)):
			tokens.append(unicode(vowels[i]+"2"+consonants[j]+"1"+consonants[k]))

for i in range(0,len(consonants)):
	for j in range(0,len(consonants)):
		for k in range(0,len(consonants)):
			tokens.append(unicode(consonants[i]+"2"+consonants[j]+"3"+consonants[k]))

f = open("hyph_tr.dic","w")
for t in tokens:
	f.write(t.encode("iso8859_9")+"\n")
f.close()
