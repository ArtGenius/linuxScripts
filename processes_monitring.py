import os, sys

def timeToSeconds(timeString):
	timeElements = timeString.split(':')
	secs = int(timeElements[2])
	mins = int(timeElements[1])
	hours = int(timeElements[0])
	return secs + mins * 60 + hours * 360

permittedTime = sys.argv[1]
permittedAmmount = sys.argv[2]

processes = os.popen("ps -ef").read().split('\n')
userProcessesMap = {}
for procString in processes[1:len(processes)-1]:
	try:
		procEntries = procString.split()
		pid = procEntries[1]
		procOwner = procEntries[0]
		if procOwner == 'root':
			continue
		procCommand = procEntries[7]
		usersProcesses = userProcessesMap.get(procOwner, [])
		usersProcesses.append(pid + ' '+ procCommand)
		userProcessesMap[procOwner] = usersProcesses
		procTime = timeToSeconds(procEntries[6])
		# print(procTime)
		if procTime > int(permittedTime):
			print('process ' + pid + ' (' + procCommand + ') consumes too many processor time (more than ' + permittedTime + 's)')
	except IOError: # proc has already terminated
         continue

for k, v in userProcessesMap.items():
	if len(v) > int(permittedAmmount):
		print('User ' + k + ' has more than ' + permittedAmmount + ' processes:')
		for proc in v:
			print(proc)
