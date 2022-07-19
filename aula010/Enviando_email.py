from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Gabriel Rocha', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Gabriel da silva Rocha'
msg['to'] = 'milenalindalima7@gmail.com'
msg['subject'] = 'Atenção: este e um e-mail de testes.'
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('lol2.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gabrielrocha12.gs@gmail.com', '99356058')
    smtp.send_message(msg)
    print('Email enviado')