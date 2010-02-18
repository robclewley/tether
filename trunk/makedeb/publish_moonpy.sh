#!/bin/bash


#Copyright 2009:
#    Isaac Carroll, Kevin Clement, Jon Handy, David Carroll, Daniel Carroll

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


#this script is used for automating the process of creating a 
#debfile out of MoonPy


cd ..
mkdir ./moonpy
echo copying files
cp -r ./client ./moonpy
cp -r ./common ./moonpy
cp -r ./data ./moonpy
cp -r ./server ./moonpy
cp -r ./translations ./moonpy
cp -r ./twisted ./moonpy
cp -r ./zope ./moonpy
cp -r ./AUTHORS.txt ./moonpy
cp -r ./COPYING.txt ./moonpy
cp -r ./moon.py ./moonpy
cp -r ./README.txt ./moonpy
cd moonpy
echo cleaning system and subversion files
find . -name .svn -exec rm -rf {} \;
find . -name *.pyc -exec rm -rf {} \;
cd ..
echo creating multi-arch archive
tar -czvf ./moonpy_all.tar.gz ./moonpy
echo finished creating multi-arch archive
cd moonpy
rm -fr ./zope
rm -fr ./twisted
cd ..
tar -czvf ./moonpy_deb.tar.gz ./moonpy
echo finished creating deb archive
mkdir ./sandbox
mv ./moonpy ./sandbox
mv ./moonpy_deb.tar.gz ./sandbox
cd sandbox/moonpy
#dh_make -e project-tether@googlegroups.com -c gpl3 -f moonpy_deb.tar.gz
#cd ..
#rm -fr ./moonpy_deb.tar.gz