
---
title: Numpy Doc - Python
date: 2025-04-29
author: CHOUBIK Houssam
draft: false
tags:
  - Python
  - Numpy
  - Documentation
  - ENSAMC
---

### **Step 1 :** Before proceding installation of Numpy Library you must install pip :

[Check this website ](https://pip.pypa.io/en/stable/installation/) 

#### Supported Methods[](https://pip.pypa.io/en/stable/installation/#supported-methods "Link to this heading")

If your Python environment does not have pip installed, there are 2 mechanisms to install pip supported directly by pip’s maintainers:

- [`ensurepip`](https://pip.pypa.io/en/stable/installation/#ensurepip)
    
- [`get-pip.py`](https://pip.pypa.io/en/stable/installation/#get-pip-py)

Methode 1 : ensurepip

```cmd
C:> py -m ensurepip --upgrade
```

Methode 2 : get-pip.py

```cmd
C:> py get-pip.py
```

### **Step 2 :** Upgrading pip

Upgrade your `pip` by running:

```cmd
C:> py -m pip install --upgrade pip
```

### **Step 3 :** Installing numpy

You can run the following command on your command line CMD :

```cmd
C:> pip install numpy
```

### **Step 4 :** Checking the version of numpy / Ensuring that numpy is installed

Create a python file using cmd or any text editor.
And write the following code, then run it.

```python
import
numpy
print(numpy .__version__) # ou bien print(numpy.version.version)
```

### For those who had version conflicts

Try to create first a python environement by runing this command in your CMD / Terminal :

```cmd
C:> python -m venv yourenvironnementname
```

Nb : You can name `yourenvironnementname` by any name for example ill name it `venv1` :

```cmd
C:> python -m venv venv1
```

Then activate your environnement by running the following command :

```cmd
C:> venv1\Scripts\activate
```

You should see someting like this : 

```cmd
(venv1) C:> 
```

Then re install numpy while your python environnement is active.