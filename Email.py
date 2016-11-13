# David Fuller
#
# 7-30-2016

import smtplib

# Define Email class
class Email(object):
    GMAIL = ""
    PASS = ""
    
    # Constructor
    def __init__(self):
        self.sender = self.GMAIL
        self.receiver = self.GMAIL
        self.message = "Test email"

    # Method sets sender
    def setSender(self, sender):
        self.sender = sender

    # Method sets receiver
    def setReceiver(self, receiver):
        self.receiver = receiver

    # Method sets message
    def setMessage(self, message):
        self.message = message

    # Message send email
    def sendEmail(self):
        gmailUser = self.GMAIL
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo
        smtpObj.login(gmailUser, self.PASS)
        smtpObj.sendmail(self.sender, self.receiver, self.message)
        smtpObj.close()

    # Method decides which email overload to call
    def email(self, *args, **kwargs):
        getattr(self, "email_" + str(len(args)))(*args, **kwargs)

    # Method sends default email
    def email_0(self):
        self.sendEmail()

    # Method sends email with given message
    def email_1(self, message):
        self.message = message
        self.sendEmail()

    # Method sends email with given message and receiver
    def email_2(self, receiver, message):
        self.receiver = receiver
        self.message = message
        self.sendEmail()

    # Method sends email with given message, sender, and receiver
    def email_3(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.sendEmail()
        
