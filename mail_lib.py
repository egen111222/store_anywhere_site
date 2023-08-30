from flask_mail import Mail,Message
import os
mail = Mail()

def send_mail(title="",
              body="",
              recipients=[]):
    msg = Message(title,
                  body=body,
                  sender=os.environ["MAIL_USERNAME"],
                  recipients=recipients)
    mail.send(msg)
    
