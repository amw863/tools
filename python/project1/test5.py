import os
import os.path

# this folder is custom
rootdir="C:\\xampp\\htdocs\\drupal7"
filename_list = []
for parent,dirnames,filenames in os.walk(rootdir):
	#case 1:
	for dirname in dirnames:
		print("parent folder is:" + parent)
		print("dirname is:" + dirname)
	#case 2
	for filename in filenames:	
		print("parent folder is:" + parent)
		print("filename with full path:"+ os.path.join(parent,filename))
		filename_list.append(os.path.join(parent, filename))

file_object = open('./test.txt', '+a')
for str in filename_list:
    file_object.write(str)
file_object.close()
