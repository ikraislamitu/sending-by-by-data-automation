from mailer import *
import mysql.connector

if __name__ == '__main__':
    custom_recipient = ["mail1","mail2", "mail3"]
    test_mode = True

    confirm = input("Press Y to confirm: ")
    if confirm == 'Y':
        mydb = mysql.connector.connect(
            host="your server",
            user="username", passwd="password", database="database")
        mycursor = mydb.cursor()
        sql = """your query"""

        mycursor.execute(sql)
        result = mycursor.fetchall()

        mail_sender = mailer()
        EMAIL_SUBJECT = "Mail subject"
        # ""  # input("Please enter the subject: ")
        HTML_FILE = "file.html"  # input("Please enter the html template's name / path: ") # "new_year.html" #

        count = 1
        for r in result:
            email = r[0]
            if test_mode == True:
                email = "mail"

            title = r[1]
            full_name = r[2]

            sent_status = mail_sender.send_mail(email, EMAIL_SUBJECT, HTML_FILE)
            if (sent_status == True):
                print("{}/{}: {} >>> {} {} --> ok".format(count, len(result), email, title, full_name))
            else:
                print("{}/{}: {} --> failed".format(count, len(result), email))

            if test_mode == True and count == 1:
                break

            count += 1

        if test_mode == True:

            for email in custom_recipient:
                sent_status = mail_sender.send_mail(email, EMAIL_SUBJECT, HTML_FILE)
                if (sent_status == True):
                    print("SPECIAL RECIPIENT: {} --> ok".format(email))
                else:
                    print("SPECIAL RECIPIENT: {} --> failed".format(email))