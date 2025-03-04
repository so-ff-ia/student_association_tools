from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import ssl
import smtplib
import pandas as pd


email_sender = 'nextgenbiotech.fabit@gmail.com'
email_password = input('password: ')

# email_receivers = [""]

path = input("path: ")
df = pd.read_csv(path)
email_receivers = list(df.Email)

subject = 'Seminar - 4th March - Engineered Bacteriophages for Medical Applications'

images = [
    {"path": "poster.jpeg", "cid": "poster"},
    {"path": "Updated logo+name+slogan.png", "cid": "logo"}
]


def send_email(receivers):

    for person in receivers:
        my_email = MIMEMultipart()
        my_email['From'] = email_sender
        my_email['To'] = person
        my_email['Subject'] = subject
        
        for image in images:
            with open(image["path"], "rb") as img_file:
                img = MIMEImage(img_file.read())
                img.add_header("Content-ID",f"<{image['cid']}>")  
                img.add_header("Content-Disposition", "inline", filename=image["path"])
                my_email.attach(img)

        with open("email_body.html", encoding="utf-8") as f:
            html = f.read()        
        my_email.attach(MIMEText(html, "html"))

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, person, my_email.as_string())
                print(f"Email sent successfully!{person}")
        except Exception as e:
            print(f"Failed to send email: {e}")


send_email(email_receivers)
