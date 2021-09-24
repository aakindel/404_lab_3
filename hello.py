#!/usr/bin/env python3

# code from lab session

import os, json
print("Content-type:test/html\r\n\r\n")
print
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")


#Q1 
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
#print(json_object)

#Q2
for param in os.environ.keys():
    #print(f"<em>{param}</em> = {os.environ[param]}</li>")
    if (param == "QUERY_STRING"):
        print ("<b>%20s</b>: %s<br>" %(param, os.environ[param]))

#Q3 - ?
for param in os.environ.keys():
    if (param == "HTTP_USER_AGENT"):
        print ("<b>%20s</b>: %s<br>" %(param, os.environ[param]))