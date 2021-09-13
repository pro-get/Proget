'''
made on Python 3.8.10

PLEASE NOTE:
This module works for python 3.x only!
because "urllib" module is not avaliable in Python 2.x
but in python 2.x you can use this code with "urllib2" module instead.

How to run in python shell?
>>> import proget
>>> proget.main("download my_software(version)") #it downloads "my_software" with version being "version".
'''

import os
import sys
import time
import yaml
import urllib
import tempfile
import requests
import platform
import subprocess
import animation
import zipfile
from github import Github
import urllib.request as req

TEMP = tempfile.gettempdir()
arch = platform.architecture()[0]
progress = ["|","/","-","\\"]

def clear():
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

def getfile(args):
	args = list(args)
	for file in args:
		num = 0
		print("Starting to download..",end = "\r")
		url = file
		local_filename = file.split("/")[-1]
		with requests.get(url, stream=True) as r:
			r.raise_for_status()
			with open(local_filename, 'wb') as f:
				for chunk in r.iter_content(chunk_size=8192):
					f.write(chunk)
					print("Downloading file '{}' [{}]".format(file,progress[num]), end = "\r")
					if num != 3: num = num+1 
					else: num = 0
		print("\ndownloaded file {}".format(local_filename))

@animation.wait(['pro-Getting the repo (|)','pro-Getting the repo (/)','pro-Getting the repo (-)','pro-Getting the repo (\\)'])
def githubGet(args):
	args = list(args)
	for repo in args:
		repoName = repo.split('/')[1]
		repoAuthor = repo.split('/')[0]
		if ':' in repoName:
			tmprepoName = repoName.split(':')[0]
			repoMain = repoName.split(':')[1]
			repoName = tmprepoName
		else:
			repoMain = 'main'
			try:
				try:
					tmp = requests.head("https://codeload.github.com/{}/zip/refs/heads/master".format(repo)).headers['Content-Length']
				except requests.exceptions.HTTPError:
					print('Repo "{}" does not exist..\nmaybe, you\'ve misspelled it?'.format(repo))
					sys.exit()
			except KeyError:
				repoMain = 'master'
		url = 'https://codeload.github.com/{}/{}/zip/refs/heads/{}'.format(repoAuthor,repoName,repoMain)
		local_filename = '{}.temp'.format(repoName)
		with requests.get(url, stream=True) as r:
			r.raise_for_status()
			with open(local_filename, 'wb') as f:
				for chunk in r.iter_content(chunk_size=8192):
					f.write(chunk)
		zipfile.ZipFile(local_filename,'r').extractall("./")
		os.remove(local_filename)
		print('Repo: {} download done..'.format(repo))
					

def download(names):	
	names = list(names)
	for name in names:
		if "(" and ")" not in name:
			ver = "latest"
			name_ver_r = name
		else:
			ver = name[name.find("(")+len("("):name.find(")")]
			name_ver_r = name.replace("({})".format(ver),"")
		num = 0
		start = time.time()
		print("Looking for file links..", end = "\r")
		try:
			try:
				file_info = req.urlopen("https://proget.whirlpool.repl.co/data/{}.yml".format(name_ver_r))
			except urllib.error.HTTPError:
				print("cannot find file information of {}".format(name))
				continue
		except urllib.error.URLError:
			print("Unable to connect... Check your connection..")
			print("Could not install {} due to Network Issues".format(name_ver_r))
			continue
		url_contents = file_info.read().decode()
		url_data = yaml.safe_load(url_contents)
		data = url_data
		#url_contents = url_contents.split("\n")
		if data[name_ver_r][ver][arch]["installer"][0][0] != "~":
			url = data[name_ver_r][ver][arch]["installer"][0]
		else:
			url = data[name_ver_r][ver][arch]["installer"][0][2:-1]
			print(url)
			continue
		#url = url_contents[0].split("~")[-1]
		local_filename = TEMP+"\\"+url.split('/')[-1]
		print("Reaching requested file..", end = "\r")
		url_file = req.urlopen(url)
		size= url_file.headers["Content-Length"]	
		print("Starting to download file", end = "\r")
		with requests.get(url, stream=True) as r:
			r.raise_for_status()
			with open(local_filename, 'wb') as f:
				sz = 0
				for chunk in r.iter_content(chunk_size=8192):  
					percent = sz / int(size)*100
					f.write(chunk)
					sz = sz+8192
					#print("abc ",floor_percent, sz)
					print("Downloading.. [{}] file \"{}\" Done: {}%  of {}kb".format(progress[num], url, round(percent,2),int(size)/1024), end = "\r")
					if num != 3: num = num+1 
					else: num = 0
	
		print("Finished in {} seconds".format(time.time()-start), end = "\n")
		#print("file can be found at {}".format(local_filename))
		os.system(local_filename)
		return local_filename

def main(optional = ""):
	if optional == "":
		if len(sys.argv) != 1:
			if "download" in sys.argv[1].lower():
				download(sys.argv[2:])
			elif "github" in sys.argv[1].lower():
				githubGet(sys.argv[2:])
			elif "uninstall" in sys.argv[1].lower():
				print("Uninstaller coming soon..")
			elif "get" in sys.argv[1].lower():
				getfile(sys.argv[2:])
			else:
				subprocess.check_call(" ".join(sys.argv[1:]))
		elif len(sys.argv) == 1 or sys.argv[1] in "--help ?":
			print("""
proget [option] (arguments)

>> option:
	download > download a software
	github   > download github repository
	get      > download a specific file

>> arguments:
	names    > the names of files/programs/repositories to download

EXAMPLES:
	proget download python(v3.8)
	proget github microsoft/terminal
	proget get https://www.whirlpool.repl.co/data/sublime_text.yml
  """)
	else:
		command_split = optional.split()
		if "download" in command_split[1].lower():
			download(command_split[2:])
		elif "github" in command_split[1].lower():
			githubGet(command_split[2:])
		elif "uninstall" in command_split[1].lower():
			print("Uninstaller coming soon..")
		elif "get" in command_split[1].lower():
			getfile(command_split[2:])
		else:
			subprocess.check_call(" ".join(sys.argv[1:]))

if __name__ in "__main__":  
	main()
