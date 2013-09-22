#!/usr/local/bin/python3

import smtplib
import time

ticket = "tnum.txt"

def ticketnumber():
    '''
    This function simply retrieves the ticket number for the tnum.txt file
    this file is only supposed to be 1 line.
    '''
    with open(ticket, 'r') as file:
        i = file.read()
    return i

def updatenumber():
    '''
    This function updates the ticketnumber in the ticket variable and returns the updated number. 
    '''
    with open(ticket, 'r') as file:
        number = int(file.read()) +  1
        file.close()
        with open(ticket, 'w+') as file2:
            file2.write(str(number))
            file.close()
    return ticketnumber()

def subjectext():
    '''
    This function constructs and returns the subject of the email ticket. 
    The updated ticket number, date, keywords, and status of the ticket are concatenated.
    '''
    date = time.asctime()
    keywords = input("Key words: ")
    status = input("Status: ")
    SUB = "Ticket Number: " + updatenumber().strip() + " | " + date + " | " + "Keywords: " + keywords + " | " + "Status: " + status
    return SUB

def sendmail(SUB, TEXT):
    '''
    This function sends the mail to your 'support account.'
    '''
    FROM = 'support@domain.com'
    TO = 'support@domain.com'
    message = """Subject: %s\n\n%s""" % (SUB, TEXT)
    server = smtplib.SMTP('localhost')
    server.sendmail(FROM, TO, message)
    server.quit()


if __name__ == '__main__':
    '''
    This is where the script actually runs. Its in a while loop so after you send out a ticket
    the next ticket is already up and ready to be written and sent.
    This idea is to have a cli window open on the system and just send emails on the fly quickly.
    '''
    while True:
        print(int(ticketnumber().strip()) + 1)
        print()
        TEXT = input("Support Ticket: ")
        SUB = subjectext()
        sendmail(SUB, TEXT)
        print()
