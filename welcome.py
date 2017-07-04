#!/usr/bin/python
import cgi

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
data1=cgi.FieldStorage()

print "<h1 style='text-align:center;'>"
print "Welcome to cloud services"
print "</h1>"

print "select services : "
'''
print "<form>"
print '<input type="radio" name="same" >SAAS (Software As A Service)'  
print '<input type="radio" name="same" >STAAS (Storage As A Service)'  
print '<input type="radio" name="same" >IAAS (Infrastucture As A Service)'  
print '<input type="submit" value="Next">'	 
print "</form>"
'''
print "</br>"
print "<a href='saas.html'> SAAS</a></br>"
print "<a href='staas.html'> STAAS</a></br>"
print "<a href='http://127.0.0.1/iaas.html'> IAAS</a></br>"

