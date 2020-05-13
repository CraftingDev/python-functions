import os


# Create file inside directory and list files
def new_directory(directory, filename):
	# Before creating a new directory, check to see if it already exists
	if os.path.isdir(directory) == False:
		os.mkdir(directory)
	# Create the new file inside of the new directory
	dir = os.chdir(directory)
	# varify the path using getcwd()
	cwd = os.getcwd()
	# print the current directory
	print("Current working directory is:", cwd)

	with open("script.py", "w") as file:
		pass
	# Return the list of files in the new directory
	return os.listdir(cwd)


print(new_directory("PythonPrograms", "script.py"))
