```

     .:~^::::  ....::.  .  ..    .:    .:^^:^~!~:........  .
....^.~~777!^.          ..       ..   ...  .:^:........:77!~
:::.^^::!Y5Y?~:...:....~J777~~...:^::. .:::^~~!!~::^^~^~JGBG
!~:^^^~!777!!!~~^^~~~!7JJ??YY?~^~7~.....~5GGGPGGG5?Y55?!~!7?
:::^^~~~~~!!77?777777!!7!!!77!7777!~~^~~?YJJYY????JJYYYJ555J
..:^~~~~~~~~~~!!???77777??777!777777?777!7!!!!!!!!!!^~JJY5YJ
^~!7J??7~~~~~~~~!!777?????!:.^~::^7??7!!!!!!!!777?7^.!77777?
...:^!??JJ!~~~~~~~~~^:..:^:. .:.   .~??77777777!!!:.^777777!
   . :~~~~~~~~~~~~^.     ..:::...    .^!7????777~:.:~!!!!!!!
   .:!7~:::^!!!7Y?.....:!JJJ?!~:::.    ^~~~~~~~~^..???JJ?777
    ... ....!YYY5~^^::!J55YJJJ?!^:::.  .7JJJJ??^: ^555YYYJJJ
        ...  .:~!.^~:!YY?!~7YYY~:..:.  .!JJ??J?^. ^7!!!!!77!
~^^^:::...    .^~...^YJ!~.:757^..   .. .^~~!!!~^.:!!!!!!!!!!
~~~!!~~~^.....:^~^ .75Y?7^:7Y~:.....::  ^!!!!?!..~!!!!!!!!!!
~~!!!!!!~~~~~~!!!!.^?Y5Y?7!?Y7::::::::. !!!!7J^.~!!!!!!!!!!!
  .:::~~~^~~7!!777~~!?55YJ?JY?:::::::..^77!7J!.~!~!!!!!!~~~~
       .. .....^^^?JY?J55YY?7^:...::...:^:.?J............   
                  .^^ .?5YYJ?!:..::.  ..  :Y^               
               .........Y555Y7^:::..   ...Y?..              
       ........::::...::!555?~^^:..   ...~P~.. .            
  ........::^:^~~!^..:!~:JYJ??J~::..  .:^J?.................
:^^^^~~~~~~!!!!!!~:..^^.~YJ?Y5?!!7~.   .!J^.^^~~~^^^^~~^^^^^
^~~~~~~~~~~~~~~!!^:....!Y5Y755????^.:..:?~.~7^::^^~~~~~~!!!~
~~~~~~~~~~~~~!7JJ^.. ::?YJYJ55YJ7!^..Y7:.  :7!^::..:^~~~~~~~
^^~~^^~~^^^~7YJYJ~...:~^7?JY5Y?!^^:.~Y?~:...:...::...^~~~~~~
^^^^^^^^^^^!JJ?5Y:. .^~7!!!777~~~::?5J?7~:::::....:...^~~~~~
^^^^^^^^~~^!J??PJ:  :^^!?J777!~^^:YP5YYJ!:.::..........^~~^^
^^^^^^^~~~~!?7?57. .^7~777?77!!!~.YPP5YY?~:::...........^^::
^^^^^^^^^^~~777Y7.. ^Y?!77?J?JJJ~.~55P5Y?!:::     ......::::
::::.:^^^^^^~!7J~.  :?JJ?J???7?J^. ?Y555J7^::.     ......:::
.....:::^^^^^~!7^:..:7???J777~77:..J?7YYJ7~:.:.      .....:.
 ......:::^^~~^!::..:~7??7!!!~7!:.!Y~.~?J7!^....     .......
   .   .::^:^^~~:.  .^~!!~!!~^~: .?!.  ~77^::..:.. .  ......
 .    .:..::::::..  .^^~!^~~~:...!!. . .~^^::........ ......
      ....::.........::~~^^~^.  :~:.... .!!!~^:.............
         .:. .:... ..::^^^^^:. .^:. ...  ^!!~^::............
        .::..... .  ...::.::. .::.  ......~~~^^:.:......  ..

```

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
