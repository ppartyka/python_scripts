#!/usr/local/bin/python3

import smtplib
import time

ticket = "tnum.txt"

def ticketnumber():
    with open(ticket, 'r') as file:
        i = file.read()
    return i

def updatenumber():
    with open(ticket, 'r') as file:
        number = int(file.read()) +  1
        file.close()
        with open(ticket, 'w+') as file2:
            file2.write(str(number))
            file.close()
    return ticketnumber()

def subjectext():
    date = time.asctime()
    keywords = input("Key words: ")
    status = input("Status: ")
    SUB = "Ticket Number: " + updatenumber().strip() + " | " + date + " | " + "Keywords: " + keywords + " | " + "Status: " + status
    return SUB

def sendmail(SUB, TEXT):
    FROM = 'me@ppartyka.com'
    TO = 'me@ppartyka.com'
    message = """Subject: %s\n\n%s""" % (SUB, TEXT)
    server = smtplib.SMTP('localhost')
    server.sendmail(FROM, TO, message)
    server.quit()


if __name__ == '__main__':
    while True:
        print(int(ticketnumber().strip()) + 1)
        print()
        TEXT = input("Support Ticket: ")
        SUB = subjectext()
        sendmail(SUB, TEXT)
        print()
