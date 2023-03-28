import win32com.client as win32
import os
from datetime import date

# Import modules
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import HTML

def sendMail(instances = "", disks = "", snapshots = "", projects = ""):
    today =  date.today()

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = os.getenv('GCP_SCRIPT_EMAIL_TO')
    mail.Subject = f'GCP {today.strftime("%d %B %Y")} Usage Report'
    mail.HTMLBody = HTML.generateHTML(instances, disks, snapshots, projects)
    #this field is optional

    # To attach a file to the email (optional):
    for project_obj in projects:
        print(f"Attaching : {project_obj['project_id']}.xlsx")
        attachment  = f"{os.getcwd()}\\{project_obj['project_id']}.xlsx"
        mail.Attachments.Add(attachment)

    print(os.getcwd())

    mail.Send()
    print("Mail Sent!")



def sendMail2():
    sender_email = "arnabdst.99@gmail.com"
    receiver_email = "abiswas@commvault.com"
    password = "kejleazvqbjozsht"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi, This is text mail"""

    html =  """
        <!DOCTYPE html>
        <html lang="en" style="box-sizing: border-box; padding: 0; margin: 0;">
        <head>
            <title>Email</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width">
        </head>
        <body style="box-sizing: border-box; padding: 0; margin: 0;">
            <main style="box-sizing: border-box; padding: 0; margin: 0; width: 100vw; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: 'Trebuchet MS';">
            <div class="container" style="box-sizing: border-box; margin: 0; width: 80%; padding: 20px; border-radius: 10px; box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px,
                rgba(0, 0, 0, 0.24) 0px 1px 2px;">
                <h2 style="box-sizing: border-box; padding: 0; margin: 0; text-align: center; margin-bottom: 10px;">Weekly GCP Usage Report</h2>
                <hr style="box-sizing: border-box; padding: 0; margin: 0; text-align: center; margin-bottom: 10px;">
                <div class="intances" style="box-sizing: border-box; padding: 0; margin: 0; display: flex; flex-direction: column; justify-content: space-between;">
                <p style="box-sizing: border-box; margin: 0; margin-bottom: 5px; padding: 0 30px;">Number of <b style="box-sizing: border-box; padding: 0; margin: 0;">instances</b> created: <span class="bad" style="box-sizing: border-box; padding: 0; margin: 0; float: right; font-weight: 600; color: #cd0404;">5</span></p>
                </div>

                <div class="disks" style="box-sizing: border-box; padding: 0; margin: 0; display: flex; flex-direction: column; justify-content: space-between;">
                <p style="box-sizing: border-box; margin: 0; margin-bottom: 5px; padding: 0 30px;">Number of <b style="box-sizing: border-box; padding: 0; margin: 0;">disk</b> created: <span class="good" style="box-sizing: border-box; padding: 0; margin: 0; float: right; font-weight: 600; color: #03c988;">5</span></p>
                </div>

                <div class="snapshots" style="box-sizing: border-box; padding: 0; margin: 0; display: flex; flex-direction: column; justify-content: space-between;">
                <p style="box-sizing: border-box; margin: 0; margin-bottom: 5px; padding: 0 30px;">Number of <b style="box-sizing: border-box; padding: 0; margin: 0;">snapshots</b> created: <span style="box-sizing: border-box; padding: 0; margin: 0; float: right; font-weight: 600;">5</span></p>
                </div>
            </div>
            </main>
        </body>
        </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
