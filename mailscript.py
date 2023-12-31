import smtplib
from email.mime.multipart import MIMEMultipart
import pandas as pd
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


sender_email = '#@gmail.com'
sender_password = 'pass'
#recipient_email = '#'
subject = 'Unveiling the Ultimate Challenge: Capture the Flag Event on August 18th!'
message = """
Warm regards from the TEAM SARK!

We greatly appreciate your enrollment in our upcoming CAPTURE THE FLAG event. Your registration has been successfully confirmed.

🚩 Prepare to engage in CAPTURE THE FLAG! 🚩

🗓️ Date: August 18th, 2023
🕟 Time: 5:00 PM
📍 Venue: Vasudha Lab, 2nd floor CSE BLOCK

Refine your abilities and seize the opportunity to compete for prizes totaling ₹6000!

Wishing you the best of luck!!👍

Best regards,
TEAM SARK
"""
csv_path = 'maillist.csv'
df = pd.read_csv(csv_path)

with open('event_image.jpg', 'rb') as image_file:
    image = MIMEImage(image_file.read())
    image.add_header('Content-Disposition', 'attachment', filename='event_image.jpg')

for remail in df['Email']:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = remail
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(image)
    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()


    server.login(sender_email, sender_password)

    server.sendmail(sender_email,remail,msg.as_string())

    server.quit()
    print("Email sent successfully!")




