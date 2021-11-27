# Proget

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Downloads](https://pepy.tech/badge/proget/month)](https://pypi.org/project/proget)
[![GitHub license](https://img.shields.io/github/license/Whirlpool-programmer/proget.svg)](https://github.com/whirlpool-programmer/proget/blob/master/LICENSE)
[![Size](https://shields.io/github/repo-size/Whirlpool-Programmer/proget)]()

## A software downloader tool made for cli users

## How to use?

very easy to use!

3 main functions:

### 1. download

just give the command:

ex: `proget download python`

then, it will look into the softwares listed in [proget.whms.repl.co](https://proget.whms.repl.co)

after that, it will download the file.. and open it once installed.

pass on the version like this:

`proget download (v3.8)`

it will download the version `v3.8` of `python`

QUESTIONS:


Which Operating systems are supported?
  
\>  Only windows is supported

What if the software doesn't support my architecture?
  
\>  If your architecture is not supported then, the file which contains the links gives a negative response by returning a string. and you will be informed about that.

### 2. Github

simple.. downloads a github repo

ex: `proget github microsoft/terminal`

then it will look, if the repo's main branch is 'main' or 'master'
then simply, it download the zip and extracts it..

pass on the branch name like this:

`proget github microsoft/terminal:inbox`

it will download the `inbox` branch not the `main` or `master` one..

### 3. get

a simple thing..

just download the file specified..

ex: `proget get https://sabnzbd.org/tests/internetspeed/20MB.bin`

then download the file `https://sabnzbd.org/tests/internetspeed/20MB.bin`

<hr>

Dependencies:
- pyYAML
- urllib
- requests
- platform
- alive_progress

<hr>

changelog:

```
v1:
 + support for github repo download
 - fixed minor bugs from v1.0b4
v2:
 + better downloading utlity
 + github repo download with branches
 + updated to work with proget.whms.repl.co as i changed my username
v2.1:
 - bugfixes from v2
v2.5:
 + softwares are downloaded in the current folder
 + use 'proget download --list' to get the list of softwares
 + work with pro-get.github.io instead of proget.whms.repl.co
v2.6:
 + use alive_progress
```
