#our target is a link <a> type "promo code" object

import mechanize
import html5lib
import difflib

br = mechanize.Browser() # prep
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]
response = br.open("https://deliveroo.co.uk/checkout/payment") # go to deliveroo.co.uk website
for link in br.links(): # for all the links on the current page (including <a>, <area> and <iframes>)
	print "link text: " + link.text # print the link text
	print "link url: " + link.url # print the link url
for form in br.forms(): # for each form on the current page
	print "Form name: ", form.name # print the form name
	print form # print the form
'''
#print response.read() # not logged in originally btw
#str1 = response.read()
#for link in br.links(): # for all the links on the current page (including <a>, <area> and <iframes>)
#	print "link text: " + link.text # print the link text
#	print "link url: " + link.url # print the link url
	#print link #print the link
#print "first link = " + str(br.links()[0])
#print "second link = " + str(br.links()[1])
#print "third link = " + str(br.links()[2])
response = br.follow_link(br.find_link("Login"))
#response = br.follow_link(br.links()[2]) # click the "become a driver" link
#print response.geturl() # print the response url
#print response.read() # print the response
#str2 = response.read()
#d = difflib.Differ() # make diff object
#diff = d.compare(str1, str2) # assign diff to the comparison of the strings
#print ''.join(diff)
#for form in br.forms(): # for each form on the current page
	#print "Form name: ", form.name # print the form name
#	print form # print the form
br.form = list(br.forms())[0] #select the first form (log-in form in this case)
#for control in br.form.controls: #for each control in the form
	#print control # print the control
	#print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
#for link in br.links(): # for all the links on the current page (including <a>, <area> and <iframes>)
#	print "link text: " + link.text # print the link text
#	print "link url: " + link.url # print the link url
control = br.form.find_control("login_email") #find postcode control
control.value = "cheyenneaskate@aol.com" #set postcode
control = br.form.find_control("login_password")
control.value = "conpass1"
response = br.submit() #submit current form
#br.follow_link(br.find_link("Login")) #opens the link, but does not submit form
#print response.read() #logged in

#logged in
#need to change country to china (target)
#for form in br.forms(): # for each form on the current page
	#print form.name # print the form name
	#print form # print the form
br.form = list(br.forms())[0]
for control in br.form.controls: #for each control in the form
	print control.name # print the control
control = br.form.find_control("postcode")
control.value = "OX14ES"
for control in br.form.controls:
	print control.name
	print control.value
response = br.submit(id='find_food')
#print response.read()
for link in br.links(): # for all the links on the current page (including <a>, <area> and <iframes>)
	print "link text: " + link.text # print the link text
	print "link url: " + link.url # print the link url
#response = br.follow_link(br.find_link("Hong Kong")) # go to hong kong
#print response.read()
#br.form = list(br.forms())[0]
#control = br.form.find_control("address_search")
#control.value = "128 Sycamore Street Tai Kok Tsui Kowloon Hong Kong"
#response = br.submit()
#print response.read()
#for link in br.links(): # for all the links on the current page (including <a>, <area> and <iframes>)
#	print "link text: " + link.text # print the link text
#	print "link url: " + link.url # print the link url
#for form in br.forms(): # for each form on the current page
#	print "Form name: ", form.name # print the form name
#	print form # print the form
#br.form = list(br.forms())[0]
#br.form.action = "confirm" #maybe?
#response = br.submit()
#print response.read()
#for link in br.links():
	#print "link text: " + link.text
	#print "link url: " + link.url
#for form in br.forms(): # for each form on the current page
	#print "Form name: ", form.name # print the form name
	#print form # print the form
#problem is that button is in javascript

#(x) need to click the javascript confirm button
#need to click a restaurant
#need to click on food item
#need to click on check out
#(x) need to click on "not now" response to tip
#(x) need to confirm address again (javascript)
#need to click promo code
#need to set promo code value
#need to click update total
#need to check success
'''

#may need http and redirect handlers as well as cookie handlers
#https://stackoverflow.com/questions/2910221/how-can-i-login-to-a-website-with-python
'''
helpful links
https://stackoverflow.com/questions/41608809/python-mechanize-click-on-button
https://bytes.com/topic/python/answers/764326-using-mechanize-python-navigate-website

http://mechanize.readthedocs.io/en/latest/browser_api.html#mechanize.Browser.open
https://answers.yahoo.com/question/index?qid=20120221154059AAfsbJW
https://pypi.python.org/pypi/mechanize#downloads
http://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet
https://stackoverflow.com/questions/1555234/fill-form-values-in-a-web-page-via-a-python-script-not-testing
https://stackoverflow.com/questions/4720470/using-python-and-mechanize-to-submit-form-data-and-authenticate
'''
