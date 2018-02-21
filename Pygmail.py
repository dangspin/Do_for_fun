#! /usr/bin/python

"""
This is the python script for sending email by my Gmail account.

Author: Charlie Dang
Date: Feb/21/2018

"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import sys
import os
import re


## Define the constant variables for this script:
SENDER = "dangxiaoqian@gmail.com"
PASSWORD = "511168020601dxq"

## The class text is used to generate the basic information we need to generate the email
class Text:

    def __init__(self, From, To, Text=None, Attached=None, hasSignature = True):
        ## define the variables
        if (From == None or not isinstance(From, str)):
            raise ValueError("Please input the correct sender information")
        self.sender = From

        if (To == None or not isinstance(To, str)):
            raise ValueError("Please input the correct receiver information")
        self.receiver = To

        ## message information
        if (Text != None and re.search(r"txt", Text) ):
            name = os.getcwd() + "/"+Text

            with open(name, 'r') as file:
                lines = file.readlines()

            string = "".join(lines)
            self.text = string
        elif (Text != None and isinstance(Text, str)):
            self.text = Text
        else:
            self.text = ""

        ## Attached file
        self.attahced = Attached

        ## signature
        if hasSignature == True:
            self.signature = "Charlie Dang, Dr. \nPhone: 13801186674"
        else:
            self.signature = ""

        ## Title of the email
        self.title = ""

    def generateText(self, Title=""):
        """
        This is the function to generate the text message
        """
        self.title = Title
        message = "From: %s \nTo: %s \n \n%s\n\n\n%s" %(self.sender, self.receiver, self.text, self.signature)

        return message

    def _setSignature(self, yourSig):
        """
        You can reset the signature by this method
        """
        self.signature = yourSig

    def getTitle(self):
        """
        This function will return the title of the message
        """
        return self.title

## The MIMEMultipart object
text = Text(SENDER, sys.argv[1], Text=sys.argv[2])
message = text.generateText(sys.argv[3])
msg = MIMEMultipart()

msg['From'] = SENDER
msg['To'] = sys.argv[1]
msg['Subject'] = text.getTitle()

msg.attach(MIMEText(message,'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(SENDER, PASSWORD)

server.sendmail(SENDER, sys.argv[1], msg.as_string())
server.quit()