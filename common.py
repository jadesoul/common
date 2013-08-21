#coding:utf8

##############################################
#
#	This is a file containning the most common python
#	code during my work. 
#
#	By Jadesoul @ 2013-8-21 17:35:15
#
##############################################

import getopt

from sys import argv, exit

#filesys
import os, shutil
from os import listdir, getcwd as pwd, chdir as cd, readlink, mkdir as md, makedirs as mds	\
	remove as rm, rmdir as rd
from os.path import split as splitdir, splitext, join, dirname, isfile, islink, isdir, exists, abspath,  \
	getatime as fatime, getmtime as fmtime, getctime as fctime, getsize as fsize

from time import sleep

def fread(path, binary=False):
	mode='r'
	if binary: mode+='b'
	f=open(path, mode)
	s=f.read()
	f.close()
	return s
    
def fwrite(s, path, append=False, binary=False):
	mode='w'
	if append: mode='a'
	if binary: mode+='b'
	f=open(path, mode)
	f.write(s)
	f.close()

def fappend(s, path, binary=False): fwrite(s, path, True, binary)
def listall(root='.'): return [join(root, i) for i in listdir(root)]
def listfiles(root='.'): return filter(isfile, listall(root))
def listdirs(root='.'): return filter(isdir, listall(root))
def listlinks(root='.'): return filter(islink, listall(root))
def u8(s): return s.encode('utf8') if type(s) is unicode else s.decode('utf8')
def gb(s): return s.encode('gbk') if type(s) is unicode else s.decode('gbk')
    
def split_path(fullpath):
    '''
    split a path into 5 parts: 
        fullpath, dirpath, filename, name, ext
    usage:
        fp, dp, fn, name, ext=split(fp)
    '''
    dirpath, filename=splitdir(fullpath)
    name, ext=splitext(filename)
    return fullpath, dirpath, filename, name, ext
    
from dbg import cerr, clog










if __name__=='__main__':
	print u8('你好'), gb('你好')

	
	
	
	