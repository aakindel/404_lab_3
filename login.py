#!/usr/bin/env python3

# code adapted from lab session

import sys, time
import os, json
import cgi, cgitb
import secret
import templates

form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

if secret.username == username and secret.password == password:
    print("Set-Cookie: login=true;")

    if os.environ["HTTP_COOKIE"] == "login=true":
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<Title>Hello - Second CGI Program</Title>")
        print("</head>")
        print(templates.secret_page(username, password))
        print("</html>")
    else:
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<Title>Hello - Second CGI Program</Title>")
        print("</head>")
        print("<body>")
        print("<p><b>Please return to the index page and login again using the correct credentials to access the secret page!</b></p>")
        print("</body>")
        print("</html>")
else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<Title>Hello - Second CGI Program</Title>")
    print("</head>")
    print("<body>")
    print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
    print("</body>")
    print("</html>")
