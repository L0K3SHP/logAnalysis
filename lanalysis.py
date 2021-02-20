f = open("/var/log/dpkg.log","r")        # Chnage the path of log file, that want to view 
#count = len(open("/var/log/xrdp.log","r").readlines(  ))
#print(count)
count = 0
fdict = {}
for x in f:
	#print(x)
	xsplit = x.split(' ',2)
	#print(xsplit[0], xsplit[1], xsplit[2])
	#print(xsplit[2].strip(' ]'))
	fdict[count] = {'Date:Time':xsplit[0],'Type':xsplit[1],'Detail':xsplit[2].strip(' ]')}
	count = count+1	
print(fdict)
