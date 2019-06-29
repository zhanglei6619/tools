# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
'''
import smtplib  
from email.mime.text import MIMEText  
import pandas as pd
#mailto_list = ['uestc-zl@163.com','chareleyzl@aliyun.com']
mail_host="smtp.sina.com"  #设置服务器
mail_user="chareleyzl"    #用户名
mail_pass="123456"   #口令 
mail_postfix="sina.com"  #发件箱的后缀
me="ZL"+"<"+mail_user+"@"+mail_postfix+">"  #发件人信息
header = u'2016年1月工资单' #邮件标题
doc = 'f:/2016.01' #发送excel文件名（注意必须按固定格式）
df = pd.read_excel(doc+'.xls') #读取excel工资单 
def send_mail(): 
    for i in range(df[u'序号'].max()):
        msg = MIMEText(str(df.iloc[i,1:-2]),_subtype='plain',_charset='utf-8')  #.format('G')
        msg['Subject'] =  header
        msg['From'] = me 
        msg['To'] = str(df.ix[i][u'邮件地址'])
        try:  
            server = smtplib.SMTP()  
            server.connect(mail_host)  
            server.login(mail_user,mail_pass)  
            server.sendmail(me, msg['To'], msg.as_string())  
            server.close()  
        except Exception,e:  
            with open(doc+'.log','a') as f:   #生成未发送名单
                f.writelines('未发送：'+str(df.ix[i][u'姓名']) + str(df.ix[i][u'邮件地址']))
            return False
        with open(doc+'.log','a') as f:   #生成已成功发送名单
            f.writelines('已发送：'+str(df.ix[i][u'姓名']) + str(df.ix[i][u'邮件地址'] + '\n'))
    return True  
             
if __name__ == '__main__':  
    if send_mail():  
        print 'all success!' 
    else:  
        print "unsuccess"