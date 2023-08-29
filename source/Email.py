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

def sendMail(instances = "", disks = "", snapshots = "", projects = "", all_actionable_items = {}):
    if 'nodeGroups' not in all_actionable_items:
        all_actionable_items['nodeGroups'] = []
    if 'disks' not in all_actionable_items:
        all_actionable_items['disks'] = []
    if 'instances' not in all_actionable_items:
        all_actionable_items['instances'] = []
    if 'snapshots' not in all_actionable_items:
        all_actionable_items['snapshots'] = []

    today =  date.today()
    sender_email = os.getenv('GCP_SCRIPT_EMAIL_TO')
    receiver_email = os.getenv('GCP_SCRIPT_EMAIL_TO')

    message = MIMEMultipart()
    message["Subject"] = f'GCP {today.strftime("%d %B %Y")} Usage Report'
    message["From"] = sender_email
    message["To"] = receiver_email

     # Add the HTML content to the email.
    html =  HTML.generateHTML(instances, disks, snapshots, projects, all_actionable_items)
    html_part = MIMEText(html, "html")
    message.attach(html_part)

    # Add the Excel attachments to the email
    for project_obj in projects:
        attachment_name = f"{project_obj['project_id']}.xlsx"
        print(f"Attaching : {attachment_name}")
        attachment  = f"{os.getcwd()}\\{project_obj['project_id']}.xlsx"
        attachment_part = MIMEBase("application", "octet-stream")
        attachment_part.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(attachment_part)
        attachment_part.add_header(
            "Content-Disposition",
            f"attachment; filename={attachment_name}",
        )
        message.attach(attachment_part)
    

    # Send the email.
    smtp_server = "SMTP.commvault.com"

    smtp_connection = smtplib.SMTP(smtp_server)
    smtp_connection.starttls()
    smtp_connection.sendmail(sender_email, receiver_email, message.as_string())
    smtp_connection.quit()
    print("Mail Sent!")
