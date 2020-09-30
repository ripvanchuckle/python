import os.path

path = str(input("Please provide a directory to save your file to: "))

isdir = str(os.path.isdir(path))

if isdir == 'True':
	print("Directory exists!")
	print()
	file = input("Please provide a file name: ")
	name = input("Please tell me your name: ")
	address = input("Please tell me your address: ")
	phone = input("Please tell me your phone number: ")
	os.chdir(path)
	with open(file, 'w') as file_object:
		file_object.write((name + ","))
		file_object.write((address + ","))
		file_object.write((phone))
	print()
	print(f' File contents of {path}\\{file}', "are" )
	print()
	f = open((file), "r")
	print(f.read())
	f.close()
elif isdir == 'False':
	dirct = input("Directory does not exist, do you wish to create it? ")
	if dirct == 'Y':
		os.mkdir(path)
		file = input("Please provide a file name: ")
		name = input("Please tell me your name: ")
		address = input("Please tell me your address: ")
		phone = input("Please tell me your phone number: ")
		os.chdir(path)
		with open(file, 'w') as file_object:
			file_object.write((name + ","))
			file_object.write((address + ","))
			file_object.write((phone))
		print()
		print(f' File contents of {path}\\{file}', "are" )
		print()
		f = open((file), "r")
		print(f.read())
		f.close()
	else:
		print("Program cannot continue. Exiting.")
