'''
made on Python 3.8.10

NOTE:
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

def githubGet(args):
	args = list(args)
	for repo in args:
		repoName = repo
		num = 0
		files = []
		repo = Github().get_repo(repo)
		contents = repo.get_contents("")
		while contents:
			print("Getting files info [{}]".format(progress[num]), end = "\r")
			file_content = contents.pop(0)
			if file_content.type == "dir":
				contents.extend(repo.get_contents(file_content.path))
			else:
				files.append(str(file_content)[18:-2])
			if num != 3: num = num+1 
			else: num = 0
		print("starting to download repository {}".format(repoName), end = "\r")
		for file in files:
			if False:
				continue
			local_filename = repoName.split("/")[-1]+"/{}".format(file)
			url = "https://raw.githubusercontent.com/{}/master/{}".format(repoName,file)
			with requests.get(url, stream=True) as r:
				r.raise_for_status()
				if not os.path.exists("/".join(local_filename.split("/")[:-1])):
					os.makedirs("/".join(local_filename.split("/")[:-1]))
				with open(local_filename, 'wb') as f:
					for chunk in r.iter_content(chunk_size=8192):
						f.write(chunk)
						print("Downloading.. [{}] file '{}'".format(progress[num], file), end = "\r")
						if num != 3: num = num+1 
						else: num = 0
			print("Finished downloading '{}' from repository '{}'".format(file, repoName))


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
	
		print("Finished in {} seconds".format(time.time()-start)+" "*(len(progress[num], url, round(percent,2),int(size)/1024)+2)+"\n")
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
			else:
				subprocess.check_call(" ".join(sys.argv[1:]))
		elif len(sys.argv) == 1 or sys.argv[1] in "--help ?":
			print("use ProGet [option] [argument]")
			print(" examples:")
			print("	  proget download software_name(version)")
	else:
		command_split = optional.split()
		if "download" in command_split[1].lower():
			download(command_split[2:])
		else:
			subprocess.check_call(" ".join(sys.argv[1:]))

if __name__ in "__main__":  
	main()
