#!/usr/bin/python
import os
import stat
import filecmp

resportFileName = 'duplicatesReport'
# get and validate directory to check
rootDir = raw_input("Enter the path to check: ")
assert os.path.exists(rootDir), "path does not exist, " + str(rootDir)
print(rootDir) 
# map with duplicates. key - file name, value - list of duplicate files' paths
filesMap = {}
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
    	fileList = filesMap.get(fname, [])
    	if (len(fileList) > 0):
    		if len(list(filter((lambda x: filecmp.cmp(x, dirName+'/'+fname)), fileList))) > 0:
    			fileList.append(dirName+'/'+fname)
    	else:			
    		fileList.append(dirName+'/'+fname)
    	filesMap[fname]=fileList
filesMap = {k:v for k,v in filesMap.iteritems() if len(v)>1}
if(len(filesMap) > 0):
	# writing report
	fo = open(resportFileName, 'w')
	for file, fileList in filesMap.iteritems():
		fileInfoString = 'Duplicates list for file with name "%s":\n' % file
		fo.write(fileInfoString)
		print(fileInfoString)
		for path in fileList:
			fo.write('\t%s\n' % path)
			print('\t%s\n' % path)
	fo.close()
	print('Duplicates report is ' + os.path.realpath(resportFileName))
	# removing duplicates
	if input('Start removing? Enter 1 to continue, any other key to exit:\n') == 1:
		for file, fileList in filesMap.iteritems():
			print('Duplicates list for file "%s"' % file)
			for path in fileList:
				print('\t%s\n' % path)
			for path in fileList:
				remove = input('Remove file "%s"? yes(1) no(2)\n' % path)
				while(remove != 1 and  remove != 2):
					remove = input('Remove file "%s"? yes(1) no(2)\n' % path)
				if(remove==1):
					os.remove(path)
					print 'removed'
else:
	print 'No Duplicates found'				