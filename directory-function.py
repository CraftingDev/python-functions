#!/usr/bin/env python
# import the modules
import requests
import os

# Set the folder path
path = "C:/Users/User/Desktop/customers/"
folder = os.listdir(path)
# our key values
keys = ["title", "name", "date", "feedback"]
for file in folder:
    count = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[count]] = value
            count += 1
    print(fb)
    response = requests.post("http://35.225.64.219/feedback/", json=fb)

print(response.request.body)
print(response.status_code)

# directory = "C:/User/Users/Desktop/customers/"
# # Create file inside directory and list files
# def new_directory(directory, filename):
# 	# Before creating a new directory, check to see if it already exists
# 	if os.path.isdir(directory) == False:
# 		os.mkdir(directory)
# 	# Create the new file inside of the new directory
# 	dir = os.chdir(directory)
# 	# varify the path using getcwd()
# 	cwd = os.getcwd()
# 	# print the current directory
# 	print("Current working directory is:", cwd)
#
# 	with open("script.py", "w") as file:
# 		pass
# 	# Return the list of files in the new directory
# 	return os.listdir(cwd)
#
#
# print(new_directory())
