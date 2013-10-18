# pysendmail
# author: Ondrej Sika, http://ondrejsika.com, ondrej@ondrejsika.com
# licence: MIT

import smtplib  


def sendmail(email_from, email_to, message, username, password, server):
    server = smtplib.SMTP(server)
    server.starttls()
    server.login(username, password)
    server.sendmail(email_from, email_to, message)
    server.quit()
