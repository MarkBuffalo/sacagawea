![Painting of Sacagawea](https://i.imgur.com/gRRFm8n.jpg)

# Table of Contents

- [What is Sacagawea?](#what-is-sacagawea-)
  * [Why?](#why-)
- [Usage](#usage)
  * [Inputfile](#inputfile)
  * [CIDR Range](#cidr-range)
  * [Web Driver Engine (Chrome or Firefox)](#web-driver-engine--chrome-or-firefox-)
  * [Example output:](#example-output-)
  * [Parameters](#parameters)

# What is Sacagawea?

Sacagawea is a project for quickly taking screenshots of a large amount of websites automatically. This is an early beta that needs to be improved before it'll run fast enough.


![Sacagawea in action](https://i.imgur.com/qj8S5uK.png)


## Why?

Imagine you're on a red team engagement and there are hundreds, perhaps thousands of hosts. You have limited time to get a quick overview of the juiciest targets.

Enter Sacagawea the Explorer. This script generates screenshots of each page, port and protocol, then displays them in an html file that allows you to sort between protocols and ports.

You are then free to pick the most likely targets of opportunity.

# Usage

## Inputfile

Your input file must be formatted like so:

 ```
 https://website.com
 http://website.com
 https://website.com:8080
 http://website.com:8080
 ```
## CIDR Range

 ```
$ ./sacagawea.py -c 10.1.0.0/16
 ```
 
 You can even combine input files with CIDR ranges:
 
 ```
$ ./sacagawea.py -c 10.1.0.0/16 -i more_hosts.txt
 ```
 
If you choose a CIDR range, currently it defaults to checking 80, 443, 8080 and 8443. If you know what you're looking for and want to speed things up, create your own input file with ports and protocols.

## Web Driver Engine Selection

You can use either Chrome or Firefox. Firefox is the default web driver, so if you want to use chrome you can choose like so:
 
 ```
$ ./sacagawea.py -c 10.1.0.0/16 -b chrome
 ```

 
 
## Example output:

```
         ,
        /:\
        >:<  This project is dedicated to
        >:<  Missing and Murdered Indigenous Women
        >:<  
   ,,,,,\:/  May you find your way home...
  #########
//////\\\\ \
//  _   _  \\  .---.
\(  O _ O  )/  \___  ,-. ,-. ,-. ,-. ,-. . , , ,-. ,-.
/\\=  _\ =//\      \ ,-| |   ,-| | | ,-| |/|/  |-' ,-|
\\/\ --- /\//  `---' `-^ `-' `-^ `-| `-^ ' '   `-' `-^
//\ '---' /\\                     ,|
\//       \\/                     `'
/\\       //\\
\\/       \//
 #         #
 "         "

[!] Loaded target list from 10.1.0.0/16
[!] 10.1.0.0/16 was parsed into 65536 host(s).
[Sacagawea Progress:   8%] █▎    | Host: 5503 of 65536 | Elapsed: 05:36 | Remaining: 30:03 | Rate: 33.28 sites/s 

```

## Parameters

```
usage: sacagawea.py [-h] [-i INPUTFILE] [-b BROWSER] [-c CIDR] [-r]

Sacagawea The Explorer

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Specify a text file with line-separated domains
  -b BROWSER, --browser BROWSER
                        The browser driver to use. e.g.: firefox/chrome. Default is Firefox.
  -c CIDR, --cidr CIDR  CIDR Range to use in lieu of --inputfile.
  -r, --report          Regenerate the report instead of running another long-winded scan.
 ```
