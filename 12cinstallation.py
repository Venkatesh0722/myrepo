#!/u01/app/oracle/middleware/wls12c1/oracle_common/common/bin/wlst.sh
connect('weblogic','welcome1','t3://192.168.225.114:7001')
print('weblogic server connected successfully')
JAVA_HOME=/u01/app/oracle/middleware/java
export JAVA_HOME
PATH=$JAVA_HOME/bin:$PATH
export PATH
java -Xmx1024m -jar /u01/app/oracle/software/fmw_12.2.1.2.0_wls.jar -silent -responseFile /u01/app/oracle/software/response.rsp -invPtrLoc /u01/app/oracle/software/oraInst.loc
if [ $? -eq 0 ]
then
echo "Weblogic installation is successful"
else
echo "fix the errors to move successfully"
fi
