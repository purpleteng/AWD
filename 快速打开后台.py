#!/usr/bin/python3
#By purplet
import webbrowser
file = open('url_admin.txt','r')
file_list = file.readlines()
for i in file_list:
    try:
        webbrowser.open(i.strip())
    except:
        print("error")