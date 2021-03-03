# Lispy

## Description

A lisp-like language made with Python

Documentation : <https://alexishuvier.github.io/Lispy-Docs/>

## Dependencies

- Python 3.8+

## Installation

- Download last release or master (unstable)
- Launch any lispy file with `python .\Lispy.py <file>.lpy [--debug]` or launch interpreter with `python .\Lispy.py [--debug]`
- Enjoy

## Features

- Basic mathematic operators : +, -, *, /, //, %
- Basic logic operators : =, !=, <=, >=, <, >, !
- Basic functions :

  - Variables management with def, set, del
  - display to print something
  - input to get input from user
  - Conditions with if
  - Loop with for and while
  - Get type of object with type
  - Assertions with assert
  - Import to import other lispy file or native module or python module

- Native modules (import \<name>):

  - str : Manage string (9 constants, 22 functions)
  - list : Manage list (23 functions)
  - dict : Manage dictionnary (7 functions)
  - math : Many functions and constants for mathematics (5 constants, 27 functions)
  - stats : Get mean, median, mode and variance (4 functions)
  - rand : Get random numbers or choice in list (5 functions)
  - sys : Get internal system informations (3 functions)
  - os : Some operations with operating system (5 functions)
  - path : Manage, read or write file, directory or path (12 functions)
  - turtle : Based on python's turtle (36 functions)
  - sqlite : Connection with sqlite DB (5 functions)
  - csv : Read, Write and Manage CSV File (19 functions)

- Additive modules (import \<python:name>):

  - lpygame : Make you own game based on python's pygame (WIP) (87 functions) (must install pygame)
  - lrequests : Based on python's requests (WIP) (8 functions) (must install requests)
  - lpycord : Make you own discord bot (WIP) (51 functions) (must install discord.py)

## Changelog

### V 1.0.0 : XXX Update - XX/XX/XX (INDEV)

- First version
