import smtplib
import datetime

def text_send(number, message, carrier):
    import yaml
    gmail_server = 'smtp.gmail.com'
    port_num = 587
    now = str(datetime.datetime.now())
    
    carriers = {
    'AT&T': '@txt.att.net',
    'T-Mobile': '@tmomail.net',
    'Verizon': '@vtext.com',
    'Sprint': '@messaging.sprintpcs.com',
    'Xfinity Mobile': '@vtext.com',
    'Virgin Mobile': '@vmobl.com',
    'Tracfone': '@mmst5.tracfone.com',
    'Simple Mobile':'@smtext.com',
    'Mint Mobile': '@mailmymobile.net',
    'Red Pocket': '@vtext.com',
    'Metro PCS': '@mymetropcs.com',
    'Boost Mobile':'@sms.myboostmobile.com',
    'Cricket':'@sms.cricketwireless.net',
    'Republic Wireless': '@text.republicwireless.com',
    'Google Fi (Project Fi)': '@msg.fi.google.com',
    'U.S. Cellular': '@email.uscc.net',
    'Ting':'@message.ting.com',
    'Consumer Cellular':'@mailmymobile.net',
    'C-Spire': '@cspire1.com',
    'Page Plus': '@vtext.com',
    }

    conf = yaml.safe_load(open('./logins.txt'))
    username = conf['email']['user']
    password = conf['email']['password']
    
    phone_number = number+carriers[carrier]
    cred = (username,password)
    
    server = smtplib.SMTP(gmail_server,port=port_num)
    server.starttls()
    server.login(cred[0],cred[1])
   
    server.sendmail(cred[0],phone_number,message)
    print('Message sent @',now)
    
text_send(number=<Phone Number Here> ,carrier=< Carrier here>, message = <message here>)