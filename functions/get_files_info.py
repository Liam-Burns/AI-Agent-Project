import os

def get_files_info(working_directory, directory="."):
    absolute_working_directory = os.path.abspath(working_directory)
    target_directory = os.path.join(working_directory, directory)

    if target_directory.startswith(absolute_working_directory) == False:
        print(absolute_working_directory)
        print(target_directory)
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    # elif not os.path.isdir(abs_path):
    #     return f'Error: "{directory}" is not a directory'
    else:
        print(absolute_working_directory)
        print(target_directory)
        return "Good"
    
#Examples to de-bug
AI_directory = "liam-burns/AI-Agent-Project"
path_1 = "calculator/tests.py"
path_2 = 'calculator'
path_3 = 'bookbot'

print(get_files_info(AI_directory, path_3))



'''
Here are some standard library functions you'll find helpful:

os.path.abspath(): Get an absolute path from a relative path
os.path.join(): Join two paths together safely (handles slashes)
.startswith(): Check if a string starts with a substring
os.path.isdir(): Check if a path is a directory
os.listdir(): List the contents of a directory
os.path.getsize(): Get the size of a file
os.path.isfile(): Check if a path is a file
.join(): Join a list of strings together with a separator

'''