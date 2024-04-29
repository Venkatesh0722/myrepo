#!/u01/app/oracle/middleware/wls12c_silent/oracle_common/common/bin/wlst.sh
import os, sys
readTemplate('/u01/app/oracle/middleware/wls12c_silent/wlserver/common/templates/wls/wls.jar')
cd('/Security/base_domain/User/weblogic')
cmo.setPassword('welcome1')
cd('/Server/AdminServer')
setOption('ServerStartMode', 'prod')
cmo.setName('admin_test')
cmo.setListenPort(7001)
cmo.setListenAddress('192.168.225.114')
writeDomain('/u01/app/oracle/middleware/wls12c_silent/user_projects/domains/hcm_test')
closeTemplate()
print '>>>Domain created successfully>>>'
exit()
