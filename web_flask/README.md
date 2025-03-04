0x04. AirBnB clone - Web framework
==================================

Concepts
--------

*For this project, students are expected to look at this concept:*

-   [AirBnB clone](https://intranet.hbtn.io/concepts/74)

Resources
---------

**Read or watch**:

-   [What is a Web Framework?](https://intranet.hbtn.io/rltoken/iWopX7mh5JZI0BtpNmMOCA "What is a Web Framework?")
-   [A Minimal Application](https://intranet.hbtn.io/rltoken/aY1qkYlIbCDDULBN6nJNYA "A Minimal Application")
-   [Routing](https://intranet.hbtn.io/rltoken/bAqYEpI4Ph-zLU7EM8iXjg "Routing") (*except "HTTP Methods"*)
-   [Rendering Templates](https://intranet.hbtn.io/rltoken/mpA3GC0bX8WOHO15xUL2Yw "Rendering Templates")
-   [Synopsis](https://intranet.hbtn.io/rltoken/-JZxrxnDnOID141U1qDcew "Synopsis")
-   [Variables](https://intranet.hbtn.io/rltoken/-qwqxJ6YyQ7Z9JvvPIE1AA "Variables")
-   [Comments](https://intranet.hbtn.io/rltoken/TsdwbqCk1utlpeOhc5eUFg "Comments")
-   [Whitespace Control](https://intranet.hbtn.io/rltoken/NR5WFn7I6qUTh-b70Od69Q "Whitespace Control")
-   [List of Control Structures](https://intranet.hbtn.io/rltoken/pyvwBzYKgoDeNQ6_QIwUsw "List of Control Structures") (*read up to "Call"*)
-   [Flask](https://intranet.hbtn.io/rltoken/k2C-4UmlYXgA6oMgO7fLgg "Flask")
-   [Jinja](https://intranet.hbtn.io/rltoken/fid5cMJKYMaRJqL60PlUew "Jinja")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/kGCHY64UciygJ4I0ANPGCA "explain to anyone"), **without the help of Google**:

### General

-   What is a Web Framework
-   How to build a web framework with Flask
-   How to define routes in Flask
-   What is a route
-   How to handle variables in a route
-   What is a template
-   How to create a HTML response in Flask by using a template
-   How to create a dynamic template (loops, conditions...)
-   How to display in HTML data from a MySQL database

Requirements
------------

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style (version 1.7)
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   A `README.md` file at the root of the folder of the project is mandatory
-   Your code should be W3C compliant and validate with [W3C-Validator](https://intranet.hbtn.io/rltoken/nx649rCOtVwREiT1Y3VR9w "W3C-Validator") (except for jinja template)
-   All your CSS files should be in the `styles` folder
-   All your images should be in the `images` folder
-   You are not allowed to use `!important` or `id` (`#...` in the CSS file)
-   All tags must be in uppercase
-   Current screenshots have been done on `Chrome 56.0.2924.87`.
-   No cross browsers

More Info
---------

### Install Flask

```
$ pip3 install Flask

```

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png)