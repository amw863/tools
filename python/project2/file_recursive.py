import os

def get_recursive_file_list(path):
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        full_file_name = os.path.join(path,file_name)
        all_files.append(full_file_name)

        if os.path.isdir(full_file_name):
            next_level_files= get_recursive_file_list(full_file_name)
            all_files.append(next_level_files)
    return all_files
path ='http://www.cnblogs.com/herbert/archive'
#print(get_recursive_file_list(path))

for root ,dirs, files in os.walk(path):
    print("Root=",root,'Dirs=',dirs,"files=",files )
