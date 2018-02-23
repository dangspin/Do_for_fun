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

DEFAULT_BODY = ""
DEFAULT_TITLE = "No Subject!"

## The class text is used to generate the basic information we need to generate the email
class Text:

    global FILE_EXTENTION
    FILE_EXTENTION = ['.txt', '.doc','.doxc']

    def __init__(self, From, To, Text=None, Attached=None, hasSignature = True):
        ## define the variables
        if (From == None or not isinstance(From, str)):
            raise ValueError("Please input the correct sender information")
        self.sender = From

        if (To == None or not isinstance(To, str)):
            raise ValueError("Please input the correct receiver information")
        self.receiver = To

        ## message information
        if (Text != None and (os.path.splitext(Text)[-1].lower() in FILE_EXTENTION)):
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

## Define command line argument variables
Input_info = sys.argv

if (len(Input_info) <= 1):
    raise Exception("Not enougth input!!")
elif (len(Input_info) == 2):
    TO = sys.argv[1]
    BODY = DEFAULT_BODY
    TITLE = DEFAULT_TITLE
elif (len(Input_info) == 3):
    TO = sys.argv[1]
    BODY = sys.argv[2]
    TITLE = DEFAULT_TITLE
elif (len(Input_info) == 4):
    TO = sys.argv[1]
    BODY = sys.argv[2]
    TITLE = sys.argv[3]

## The MIMEMultipart object
text = Text(SENDER, TO, Text=BODY)
message = text.generateText(TITLE)
msg = MIMEMultipart()

## Basic Information
msg['From'] = SENDER
msg['To'] = TO
msg['Subject'] = text.getTitle()

## Body of the message
msg.attach(MIMEText(message,'plain'))


## Setup to send Email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(SENDER, PASSWORD)

server.sendmail(SENDER, TO, msg.as_string())
server.quit()
