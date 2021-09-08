#Modules are imported here
import os
import shutil
import time

#Main Funtion of the code

def main():
	deleted_folders_count = 0
	deleted_files_count = 0
	path = input("Enter The folder:- ")
	days = 1
	seconds = time.time() - (days * 24 * 60 * 60)

#Condition to Check The path exists or not

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= FolderAge(root_folder):
				remove_folder(root_folder)
				deleted_folders_count += 1 
				break      

			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)

#To Check the folder age 

					if seconds >= FolderAge(folder_path):
						remove_folder(folder_path)
						deleted_folders_count += 1 

				for file in files:
					file_path = os.path.join(root_folder, file)

					if seconds >= FolderAge(file_path):
						remove_file(file_path)
						deleted_files_count += 1

  #To delete The file or folder

		else:
			
			if seconds >= FolderAge(path):
			
				remove_file(path)
				deleted_files_count += 1 

	else:		
		print(f'"{path}" is not found')
		deleted_files_count += 1 

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")

#funtion To remove the folder

def remove_folder(path):

	
	if not shutil.rmtree(path):	
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)

#Funtion to delete the file

def remove_file(path):

	if not os.remove(path):
		
		print(f"{path} is removed successfully")

	else:
		
		print("Unable to delete the "+path)

#Function To Get the folder age

def FolderAge(path):

	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__':
	main()