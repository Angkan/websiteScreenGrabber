#!/usr/bin/env python
#When running please check whitespaces are correct on your system

from selenium import webdriver
from pyvirtualdisplay import Display
import os
import sys

#show usage to end user
print "usage: " + sys.argv[0] + " path_of_subdomains_directory " +  "outputDir"

#check argument length and exit if no match
if (len(sys.argv) < 3):
	print "[-]Insufficient arguments... Exiting!"
	sys.exit(1)

f = open(sys.argv[1])
lines = f.readlines()

#make location to save screenshots
os.mkdir(sys.argv[2])
print "[+]Results shall be found in folder: " + sys.argv[2]
os.chdir(sys.argv[2])

def capture(url):
	display = Display(visible=0,size=(800,600))
	display.start()
	try:
		#Take screenshots
		url1 = "https://" + url
		url2 = "http://" + url
		browser = webdriver.PhantomJS()
		browser.set_page_load_timeout(10)
		print "at: " + url1
		browser.get(url1)
		browser.save_screenshot(url+"1.png")
		print "at: " + url2
		browser.get(url2)
		browser.save_screenshot(url+"2.png")
		print "[+]Done!"
		browser.quit()
	except Exception,e:
		print "[-]Error occured for url " + url + " due to: " + str(e)
		pass


print "[+]Starting capture"
for line in lines:
        line = line.strip("\r").strip("\n")
        capture(line)

#close file handler after iterations finish
print "[+]capture finished"
f.close()
