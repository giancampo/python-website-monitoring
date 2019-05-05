# written in Python 2: This could cause issues with later versions of Python

#sources:
#starting idea > https://www.reddit.com/r/learnpython/comments/3f4wx8/comparing_2_files_with_python/
#difflib.differ docs > https://docs.python.org/2/library/difflib.html#difflib.Differ
#checking if two files are equals > https://stackoverflow.com/questions/1072569/see-if-two-files-have-the-same-content-in-python
#sending emails with Python > http://stackabuse.com/how-to-send-emails-with-gmail-using-python/

import os
import urllib2
import html2text
import difflib
import filecmp
import smtplib
import sys

#enconding setting in order to work with the html file
reload(sys)
sys.setdefaultencoding('utf8')

#download and store new html file
os.rename('ABSOLUTE-PATH-TO/new_html.html', 'ABSOLUTE-PATH-TO/old_html.html')

url = 'YOUR-URL-TO-MONITOR'
response = urllib2.urlopen(url)
webContent = response.read()
f = open('ABSOLUTE-PATH-TO/new_html.html', 'w')
f.write(webContent)
f.close()

#convert html to txt files
html1 = open('ABSOLUTE-PATH-TO/old_html.html').read()
html2 = open('ABSOLUTE-PATH-TO/new_html.html').read()

old_file = html2text.html2text(html1)
new_file = html2text.html2text(html2)

#write text into txt files
old_text = open('ABSOLUTE-PATH-TO/old_text.txt', 'w')
new_text = open('ABSOLUTE-PATH-TO/canali/new_text.txt', 'w')

old_text.write(old_file)
new_text.write(new_file)

old_text.close()
new_text.close()

#make diff
old_text = open('ABSOLUTE-PATH-TO/old_text.txt', 'r')
new_text = open('ABSOLUTE-PATH-TO/new_text.txt', 'r')

d = difflib.Differ()
diff = list(d.compare(old_text.readlines(), new_text.readlines()))
with open('ABSOLUTE-PATH-TO/diff.txt', 'w') as diff_file:
    _diff = ''.join(diff)
    diff_file.write(_diff)

old_text.close()
new_text.close()

#send an email if the script has found differences
if filecmp.cmp('ABSOLUTE-PATH-TO/old_text.txt', 'ABSOLUTE-PATH-TO/new_text.txt') == True:
    print 'no emails sent'
else:
    gmail_user = 'YOUR-GMAIL-ADDRESS'
    gmail_password = 'YOUR-GMAIL-PASSWORD'

    sent_from = gmail_user
    to = ['EMAIL-ADDRESS-1', 'EMAIL-ADDRESS-2']
    subject = 'Changes in the homepage!'
    body = _diff

    email_text = '''From: %s\nTo: %s\nSubject: %s\n\n%s''' % (sent_from, ', '.join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print 'Email sent!'

#files closing
diff_file.close()
