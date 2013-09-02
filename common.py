#coding:utf8

##############################################
#
#	This is a file containning the most common python
#	code during my work. 
#
#	By Jadesoul @ 2013-8-21 17:35:15
#
##############################################

import os, sys, re, shutil, getopt, datetime, time, urllib, urllib2, struct, logging
from os import listdir, getcwd as pwd, chdir as cd, mkdir as md, makedirs as mds, remove as rm, rmdir as rd, system as run
from os.path import split as splitdir, splitext, join, dirname, isfile, islink, isdir, exists, abspath, getatime as fatime, getmtime as fmtime, getctime as fctime, getsize as fsize
from re import compile, sub as rsub
from urlparse import urlsplit, urlunsplit, urlunparse, urljoin, urldefrag
from random import sample as rsample, shuffle, randint
from copy import deepcopy as clone
from pprint import pprint as dump

def cerr(s): sys.stderr.write(str(s)+'\n')
def cout(s): sys.stdout.write(str(s)+'\n')
clog=cerr

from sys import argv, exit
argc=len(argv)
app=splitdir(argv[0])[1]

from time import sleep
def now(): return datetime.datetime.now()
def nowfn(): return str(now()).replace(' ', '_').replace('.', '_').replace(':', '-')

def listall(root='.'): return [join(root, i) for i in listdir(root)]
def listfiles(root='.'): return filter(isfile, listall(root))
def listdirs(root='.'): return filter(isdir, listall(root))
def listlinks(root='.'): return filter(islink, listall(root))
def u8(s): return s.encode('utf8') if type(s) is unicode else s.decode('utf8')
def gb(s): return s.encode('gbk') if type(s) is unicode else s.decode('gbk')

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
def split(fp): dp, fn=splitdir(fp); name, ext=splitext(fn); return fp, dp, fn, name, ext

try: import cjson; jencode=cjson.encode; jdecode=cjson.decode
except: import json; jencode=json.dumps; jdecode=json.loads
def jdump(obj, fp): fwrite(jencode(obj), fp)
def jload(fp): return jdecode(fread(fp))

try:
	import simplejson
	def jexport(obj, is_unicode=False): 
		return simplejson.dumps(obj, skipkeys=False, indent=4, ensure_ascii=False) if is_unicode else simplejson.dumps(obj, encoding='utf8', skipkeys=False, indent=4, ensure_ascii=False)
except: pass

try: import cPickle as pickle
except: import pickle
pencode=pickle.dumps
pdecode=pickle.loads
def pdump(obj, fp): f=open(fp, 'wb'); pickle.dump(obj, f); f.close()
def pload(fp): f=open(fp, 'rb'); obj=pickle.load(f); return obj

urlencode=urllib.quote
urldecode=urllib.unquote

try:
	import multiprocessing as mp
	from mp import Pool
	def urlparse(url): 
		p=urlsplit(url)
		return p.scheme, p.netloc, p.hostname, p.port, p.username, p.password, p.path, p.query, p.fragment
except: pass

def query(url, params={}, data='', headers={'User-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1'}): 
	req=urllib2.Request(url, urllib.urlencode(params))
	req.data=data
	req.headers.update(headers)
	f=urllib2.urlopen(req)
	html=f.read()
	f.close()
	return html
	
def batch(cmds):
	for cmd in cmds.strip().split('\n'):
		print 'RUN @', now(), '- CMD:', cmd, run(cmd)

def vsorted(d): return sorted(d.items(), key=lambda x: x[1])
def rvsorted(d): return sorted(d.items(), key=lambda x: x[1],  reverse=True)
def ksorted(d): return sorted(d.items(), key=lambda x: x[0])
def rksorted(d): return sorted(d.items(), key=lambda x: x[0],  reverse=True)
def sort_table_by_colume(table, col_id, reverse=False): return sorted(table, key=lambda x: x[col_id],  reverse=reverse)

def unique(lst): return list(set(lst))
def reversed(lst): return lst[::-1]

def parallel(func, data, handle=None):
	rets=Pool(processes=mp.cpu_count()).map(func, data)
	if handle: handle(rets)


message_format='%(name)-8s %(asctime)s %(levelname)-8s %(message)s'
time_format='[%Y-%m-%d %a %H:%M:%S]'
default_formatter=logging.Formatter(message_format, time_format)
logging.basicConfig(level=1, format=message_format, datefmt=time_format, stream=sys.stdout)

class Logger(object):
	def __init__(self, name, level=logging.NOTSET, filepath=None, stream=sys.stdout):
		self.logger=logging.getLogger(name)
		self.logger.setLevel(level)
		if filepath: self.log_file(filepath)
		if stream: self.log_stream(stream)
		
	def log_file(self, filepath, level=logging.NOTSET, formatter=default_formatter):	
		fh=logging.FileHandler(filepath)
		fh.setLevel(level)
		fh.setFormatter(formatter)
		self.logger.addHandler(fh)
		
	def log_stream(self, stream=sys.stdout, level=logging.NOTSET, formatter=default_formatter):	
		sh=logging.StreamHandler(stream)
		sh.setLevel(level)
		sh.setFormatter(formatter)
		self.logger.addHandler(sh)
		
logger=Logger('Jadesoul', 1)
debug=logger.logger.debug
info=logger.logger.info
warn=logger.logger.warn
error=logger.logger.error
critical=logger.logger.critical

if __name__=='__main__':
	print u8('你好'), gb('你好	')
	print listall()
	print listdirs()
	print listfiles()
	clog('hi')
	debug('debug')
	warn('debug')
	
	
	
	