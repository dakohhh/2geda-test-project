from django.conf import settings
from django.core.mail import EmailMessage
from main.models import User


def send_welcome_email(firstname, lastname, email):
    subject = "Welcome to 2GEDA"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    html_content = f"""<div style="text-align: center;">
            <img src="https://scontent.cdninstagram.com/v/t51.2885-19/363756093_303976558862287_5611095969302283316_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=107&_nc_ohc=LPH_FY9Njf0AX8YXLxb&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDcn5HYfxaRfLn94dfMc9wlu6Hc6X3636IzKz_5UnBctw&oe=65E26A6B&_nc_sid=10d13b" alt="Company Logo" style="border-radius: 50%; width: 200px; height: 200px; object-fit: cover; margin-top: 20px;">
        </div>
        <p style="font-size: 16px; margin-bottom: 20px;">Dear {firstname} {lastname} ,</p>
        <p style="font-size: 16px; margin-bottom: 20px;">Thank you! :-)</p>
        <p style="font-size: 16px; margin-bottom: 0;">2GEDA </p>
    </div>"""

    email = EmailMessage(subject, html_content, from_email, recipient_list)
    email.content_subtype = "html" 

    email.send()



