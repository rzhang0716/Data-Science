import smtplib
from email.message import  EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'name1'
email['to'] = 'email.address.1'
email['subject'] = 'subject'

email.set_content(html.substitue(name="Kan"), 'html')  # ({'name:"Kan"})

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com', 'password')
    smtp.send_message(email)
    print('all good!')


