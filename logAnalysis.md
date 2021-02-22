# logAnalysis
***
# Windows

  ## Log Location *[C:\Windows\System32\winevt\Logs]*
  > Security Log File/Location: *C:\Windows\System32\winevt\Logs\Security.evtx*
  > 
  > System Log File/Location: *C:\Windows\System32\winevt\Logs\System.evtx*

  ## Register Edit
  > *Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog*
  
***
# Linux

  ## Log Location *[/var/log]*
  ### **System Log**   
  > 
  > Debian based: */var/log/syslog* <br>
  > RedHat based: */var/log/messages*
  >
  ### **Security Log**
  > 
  > Debian based: */var/log/auth.log* <br>
  > RedHat based: */var/log/secure*
  >
  <br>
  
   | Name          | Location      | 
   | ------------- |:-------------:| 
   | `Kern Log`     | */var/log/kern.log* |
   | `Corn Log`     | */var/log/cron*    |  
   | `Apache2 Log` | */var/log/apache2*     |  
   | `MySQL Log`    | */var/log/mysql*  or */var/log/mysqld* |
   | `Mail Log`   | */var/log/maillog*    |  
   | `Qmail Log` | */var/log/qmail/*    | 
   | `Boot Log`  | */var/log/boot.log*   |  
   | `HTTP Log` | */var/log/httpd/*   
