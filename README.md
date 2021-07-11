# Proget

## A software downloader tool made for cli users

#### NEW: Github repository downloading
just run

`proget github owner/repo`
(replace owner by owner and repo by repository name)

What it does?

  So, basically. you give it the command in the console.

  ```
  proget download sublime_text
  ```

  by default if no version is given, it just uses the key "latest" and for versions:
  
  ```
  proget download sublime_text(v4)
  ```

  in this way you pass versions..
  then it splits the command, 

  `(proget,download,[sublime_text(v4),**args])`

  after that it reads every software name
  and connect to the web and look for the file from http://proget.whirlpool.repl.co and gets info of the links..
  then simply it downloads the file and opens it when finished.

Which Operating systems are supported?
  
  Only windows is supported

What if the software doesn't support my architecture?
  
  If your architecture is not supported then, the file which contains the links gives a negative response by returning a string. and you will be informed about that.

```


Dependencies:

> pyYAML

> urllib

> requests

> platform
```

changelog:
```
v1:
  ~ support for github repo download
  ~ fixed minor bugs from v1.0b4
```
