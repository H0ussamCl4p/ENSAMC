---
title: DSA using C
date: 2025-09-24
author: CHOUBIK Houssam
draft: false
tags:
  - DSA
  - CS2C
  - ENSAMC
---

# Intro

[Guide to DSA in C](https://www.geeksforgeeks.org/c/learn-dsa-in-c/)

Books :
[Data Structure Book](https://gnindia.dronacharya.info/IT/3rdSem/Downloads/DataStructure/Books/DATA-STRUCTURE-BOOK-3.pdf)
[Fundamentals of Data Structures in C - Ellis Horowitz](https://mrce.in/ebooks/Fundamentals-of-Data-Structures-in-C-Ellis-Horowitz-Sartaj-Sahni-etc.-.pdf)


# Structures in C

nb : we shouldnt declare a struc or table in the middle of the program , always declare it in the top.


# File handling in C

- fprintf to print
- fscanf to read

In C, you can create, open, read, and write to files by declaring a [pointer](https://www.w3schools.com/c/c_pointers.php) of type `FILE`, and use the `fopen()` function:

```c
FILE *fptr;  
fptr = fopen(_filename_, _mode_);
```

`FILE` is basically a data type, and we need to create a pointer variable to work with it (`fptr`). For now, this line is not important. It's just something you need when working with files.

To actually open a file, use the `fopen()` function, which takes two parameters:


| Parameter  | Description                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| _filename_ | The name of the actual file you want to open (or create), like `filename.txt`                                                                                                                    |
| _mode_     | A single character, which represents what you want to do with the file (read, write or append):<br><br>`w` - Writes to a file  <br>`a` - Appends new data to a file  <br>`r` - Reads from a file |

