
# sudo nano /etc/rc.local
# python3 SendEmail.py

import socket  
import time  
import urllib.request import urlopen
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText    
    
def sendEmail(smtpserver,username,password,sender,receiver,subject,msghtml):  
    msg = MIMEMultipart()  
    msg["To"] = ','.join(receiver) 
    msg["From"] = sender  
    msg['Subject'] =  subject  
    msgText = MIMEText(msghtml,'html','utf-8')  
    msg.attach(msgText)  
    #sendEmail  
    smtp = smtplib.SMTP()  
    smtp.connect(smtpserver)  
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver, msg.as_string())  
    smtp.quit() 

def get_ip_address():  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.connect(("1.1.1.1",80))  
    ipAddr=s.getsockname()[0]  
    s.close()  
    return ipAddr 

def check_network():  
    while True:  
        try:  
            result=urlopen('http://www.google.com').read()  
            print("Network is Ready!")  
            break  
        except Exception:  
            print("Network is not ready,Sleep 5s....")
            time.sleep(5)  
    return True

def get_ip_address():  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.connect(("1.1.1.1",80))  
    ipAddr=s.getsockname()[0]  
    s.close()  
    return ipAddr  



if __name__ == '__main__':  
    check_network()  
    ipAddr=get_ip_address()  
    sendEmail('smtp.xxx','xxxxxx','xxxx','xxxxxx@cc.ncu.edu.tw',['xxxxxx@gmail.com',''],'IP Address Of Raspberry Pi3',ipAddr) 
    print('Email Sended')
