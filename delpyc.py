#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re


def dirwalk(path):
    pycf = re.compile(r'\.pyc$')
    for path,d,fl in os.walk(path):
        for fn in fl:
            if pycf.search(fn):
                print 'pyc file:' + os.path.join(path,fn)

def itdir(path):
#    curp=os.getcwd()
    curp=os.path.abspath(path)
    hiddenf = re.compile(r'^\..')
    import sys,traceback
    pycf = re.compile(r'\.pyc$')
    for fll in os.listdir(path):
        #print fll
        fullpath = os.path.join(curp,fll)
        if os.path.isdir(fullpath):
#            print fll,'is a folder'
            if  not hiddenf.match(fll):
#                print 'calling itdir on '+fullpath
                
                itdir(fullpath)
#                traceback.print_tb()
                for en in traceback.extract_stack():
                    print en
                print 'end of one stack'
        else:
            if not hiddenf.match(fll) and pycf.search(fullpath):
                print fullpath #curp+'/'+fll
                os.remove(fullpath)
            #if pycf.search(fullpath):
             #   print fll,'is a pyc file'

if __name__ == '__main__':
    itdir('.')
    #dirwalk('.')
