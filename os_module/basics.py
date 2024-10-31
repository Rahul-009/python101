import os
from datetime import datetime


print(dir(os))  # will print all commmands for os
print(dir(os.path))  # print all available command for os.path


# current working directory
print(os.getcwd())

# change directory
os.chdir('/home/alpha')

# list all files and folders in a directory
print(os.listdir())

# make directory
os.mkdir('os-Demo')                     # make one
os.makedirs('os-Demo-2/sub-dir-01')     # make whole dir

# remove directory
os.rmdir('os-Demo')                     # remove one 
os.removedirs('os-Demo-2/sub-dir-01')   # remove whole dir

# rename directory
os.rename('test.txt', 'demo.txt')

# detail info about a file
print(os.stat('os_module/readme.md'))
mod_time = os.stat('os_module/readme.md').st_mtime
print(datetime.fromtimestamp(mod_time))

# shows all file and folders | simply tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# to check environment variable
os.environ.get('HOME')

# can cause error related to slash
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

# works perfectly
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('/temp/test.txt'))
print(os.path.split('/temp/test.txt'))
print(os.path.splitext('/temp/test.txt'))
print(os.path.basename('/temp/test.txt'))
print(os.path.exists('/temp/test.txt'))
print(os.path.isfile('/temp/test.txt'))
print(os.path.isdir('/temp/test.txt'))