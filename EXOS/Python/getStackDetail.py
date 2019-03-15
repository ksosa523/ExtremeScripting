##### | Created by: Kevin Sosa | #####
# This script shows the stacking configuration of a stack
# and then sends the information to the desired e-mail recipient
import smtplib
import sys
from email.mime.text import MIMEText

# Declare variables
me = "user@example.com"
to = "user@example.com"
smtp = "smtp.example.com"
#print("Parameters are: %s, %s and %s." % (me,to,smtp) )

# Run command to show stacking information
mac_address = emc_cli.send('sh stacking | include "00"').getOutput()

# Run command to show serial number and version number
serial_no = emc_cli.send('sh ver | include "IMG"').getOutput()

# Concatenate and Format Strings for Subject Line
formatForSubject = (mac_address + "\n" + serial_no)
subject = formatForSubject.split("#")[0]
if (subject.find('Slot') != -1):
    subject = subject[7:len(subject)-3]
else:
    subject = subject[0:len(subject)-3]

# Concatenate and Format Strings for Body Text
mac_address = mac_address.split('00"')[1]
serial_no = serial_no.split('IMG"')[1]

count = 0 
formattedMacAddressInfo = mac_address.split("\n")
formattedSerialNoInfo = serial_no.split("\n")
numberOfLines = len(formattedMacAddressInfo)-1
macAddressResults = ""
serialNoResults = ""

while count < numberOfLines:
    macAddressResults = macAddressResults + formattedMacAddressInfo[count] + "\n"
    count = count + 1

    
count = 0

while count < numberOfLines:
    serialNoResults = serialNoResults + formattedSerialNoInfo[count] + "\n"
    count = count + 1
    
    
cli_results = (macAddressResults + "\n--------------\n" + serialNoResults)
message = "Subject: {}\n\n{}".format(subject, cli_results)

#print(cli_results)


# Send e-mail
s = smtplib.SMTP(smtp)
s.sendmail(me,to,message)
s.quit()
