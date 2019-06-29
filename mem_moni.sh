#bash myscript
filename=/result.log  
filesize=`ls -l $filename | awk '{ print $5 }'`  
maxsize=$((1024*1024*10)) #Âú10MÇåÀí 
if [ $filesize -gt $maxsize ]  
then  
    > /result.log
else   
    date +%Y-%m-%d  +" " +%H:%-M:%-S >> /result.log
    vmstat >> /result.log
fi 



crontab -e
0 * * * * /result.sh >/dev/null 2>&1
0,10,20,30,40,50 * * * * /result.sh >/dev/null 2>&1
