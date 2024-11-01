import glob


print(glob.glob('file.txt'))

# ? means any character
print(glob.glob('?ile.txt'))

# any 4 letter filename
print(glob.glob('????.txt'))

print(glob.glob('*.txt'))
print(glob.glob('*.*'))

# any file that starts with a or v or d
print(glob.glob('[avd]*.txt'))

# any file that do no start with z or f
print(glob.glob('[!zf]*.txt'))

# search through all folders
print(glob.glob('**/*.txt'))


# efficient and faster for large amount of files
globs = glob.iglob('**/*.py',
                   root_dir='/home/alpha/Desktop/python101',
                   recursive=True,
                   include_hidden = True)

for i, file in enumerate(globs, 1):
    print(i, file, sep = ': ')

