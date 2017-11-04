#!/usr/bin/python
import os, sys

permittedSize = sys.argv[1]

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
            	total_size += os.path.getsize(fp)
    return total_size

rootDir = '/home'
if len(sys.argv) < 2:
	print('python check_home_dir_size <size in bytes>')
else:
	allDirsWithPermittedSize = True	
	for dirName in next(os.walk('/home'))[1]:
		fileSize = get_size('/home/' + dirName)
		if fileSize > int(permittedSize):
			allDirsWithPermittedSize = False
	   		print(dirName + 'home directory size is too big (%s)' % fileSize)
	if allDirsWithPermittedSize:
		print('All home directories have size < '+ permittedSize)