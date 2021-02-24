import subprocess as sp
import re 
from array import *

#import title

output = []
#filter_object = []

#Run nmap for port 445 via shell and put output into an array
fourfourfive = sp.check_output("for i in $(nmap -4 -n -p 445 -iL ranges.txt | grep report | grep -E '132|133|134' | awk '{print $5}'); " "do echo $i ; done", shell=True)

#run cme smb against IPs found through nmap command and save to array
for x in fourfourfive.splitlines():
	crackmapexec = sp.check_output("cme --timeout 3 smb " + x.decode('utf-8') + " | sed 's/\x1b\[[0-9;]*m//g'", shell=True)
	output += [crackmapexec.decode('utf-8')] 

#search arrray for voutdated servers (add fix for 2008)(add fix for 6.1 UNIX)
if any("2008" in s for s in output) or any("Windows Server 2003" in f for f in output) or any("Windows 6.1" in g for g in output) or any("Windows 7" in h for h in output):

#search array for 2008 and add to variable
	zeroeight = filter(lambda a: "2008" in a, output)
#if variable contains info print the cme information (add fix to print out each on new lint, not sure if this happens)
	if any("Windows" in i for i in  zeroeight):
		print ('Outdated Windows Detected Server 2008')
#search array again and put into variable (find way to do this without having to do it twice)
		zeroeight = filter(lambda a: "2008" in a, output)
#print array (try to get it to print each on new line, splitlines('\n')??
		print (list(zeroeight))
	print ()

#maybe try turning this into switch or something?
	zerothree = filter(lambda b: 'Windows Server 2003' in b, output)
	if any("Windows" in j for j in zerothree):
		print ('Outdated Windows Detected Server 2003')
		zerothree = filter(lambda b: 'Windows Server 2003' in b, output)
		print (list(zerothree))
	print ()

	seven = filter(lambda c: 'Windows 7' in c, output)
	if any("Windows" in k for k in seven):
		print ('Outdated Windows 7 EUD')
		seven = filter(lambda c: 'Windows 7' in c, output)
		print (list(seven)) 

#maybe add else for if no servers are found at all?
else:
	print ('No Outdated Windows Identified')





