import os

def get_abspath(s):
	dj = s.replace(' ', '').split(',')
	pth = os.path.join(*dj)
	return os.path.abspath(pth)

def frameCommand(venv, to_django):
	venv_cmd = get_abspath(venv)
	dj_cmd = get_abspath(to_django)
	command = "\"cd /d "+venv_cmd+" & activate & cd /d "+dj_cmd+"\""
	return command

def writeBat(file_name, venv_path, django_path):
	with open(file_name, 'w') as f:
		f.writelines("@echo off\n")
		f.writelines("cmd /k "+ frameCommand(venv_path, django_path))

def main():
	again="y"
	while again.lower() == "y" or again == "":
		venv = input('Provide the tree structure to the scripts folder of virtualenv: ')
		to_django = input('Input tree structure from current folder to the django folder containing manage.py. Use ,(comma) as separator: ')
		fname = input('Provide the name for bat-file: ')
		bat_file = fname + ".bat"

		v_path = get_abspath(venv)
		dj_path = get_abspath(to_django)
		print("Virtualenv scripts path: "+v_path)
		print("Django directory path: "+dj_path)

		again = input("Want to change paths? y/n (y): ")
	writeBat(bat_file, v_path, dj_path)

if __name__ == '__main__':
	main()