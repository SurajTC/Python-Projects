# import smtplib

import getpass

from email_validator import validate_email

def get_sender_mail():
    gmail = input("Enter Sender Gmail Address : ")
# password = input("Enter password for "+ gmail +" :")
    try:
        valid=validate_email(gmail)
        gmail=valid.email

    except:
        print("\nError : invalid Email address\n")
        get_sender_mail()
        return
        
    password = getpass.getpass("Enter password for "+ gmail +" :")

    print('''
    Please Login to %s using your preferred web browser
    and copy the link below to allow python to access your Gmail ID
    
    Link to enable access for Less secure apps :
    https://myaccount.google.com/lesssecureapps

    ''' %gmail)
    input("Press <Enter> when done")

    print(password)

get_sender_mail()

