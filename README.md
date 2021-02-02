# Lispy

## Description

A lisp-like language made with Python

## Dependencies

- Python 3.8+

## Installation

- Download last release or master (unstable)
- Launch any lispy file with `python .\Lispy.py <file>.lpy` or launch interpreter with `python .\Lispy.py`
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

  - str : Manage string (9 constants, 19 functions)
  - list : Manage list (21 functions)
  - dict : Manage dictionnary (7 functions)
  - math : Many functions and constants for mathematics (5 constants, 24 functions)
  - stats : Get mean, median, mode and variance (4 functions)
  - rand : Get random numbers or choice in list (5 functions)
  - file : Manage, read or write file (11 functions)
  - turtle : Based on python's turtle (36 functions)
  - sqlite : Connection with sqlite DB (5 functions)

- Additive modules (import \<python:name>):

  - lpygame : Based on python's pygame (WIP) (77 functions) (must install pygame)
  - lrequests : Based on python's requests (WIP) (8 functions) (must install requests)

## Changelog

### V 1.0.0 : XXX Update - XX/XX/XX (INDEV)

- First version
