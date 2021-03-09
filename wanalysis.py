import win32evtlog as log # Install module pywin32 
system = log.OpenEventLog(None,"System")
cnt = log.GetNumberOfEventLogRecords(system)
flags= log.EVENTLOG_BACKWARDS_READ|log.EVENTLOG_SEQUENTIAL_READ
#print(cnt)
def evnt(a):
    et = {0:'SUCCESS',1:'ERROR',2:'WARNING',4:'INFORMATION',8:'AUDIT-SUCCESS',10:'AUDIT-FAILURE'}
    if a in et:
        return et[a]
while True:
    rd = log.ReadEventLog(system,flags,1)
    print(len(rd))
    if rd: 
        for i in rd:
            print("RecordNumber: ",i.RecordNumber)
            print("EventID: ",i.EventID)
            print("SourceName: ",i.SourceName)
            print("TimeGenerated: ",i.TimeGenerated)
            print("TimeWritten: ",i.TimeWritten)
            print("Level: ",evnt(i.EventType))
            print("EventCategory: ",i.EventCategory)
            print("ComputerName: ",i.ComputerName)
            print("Data: ",i.StringInserts)
            print("########################################")
            print('\n')

