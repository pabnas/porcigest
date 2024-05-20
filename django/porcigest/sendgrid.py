from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

def send_mail_contact_us(
        nombre_completo: str,
        correo: str,
        direccion: str,
        telefono: str,
        mensaje: str = ''
    ):
    message = Mail(
        from_email='porcigestmanta@gmail.com',
        to_emails='porcigestmanta@gmail.com',
        subject='Nuevo mensaje de contacto desde la página web',
    )
    message.dynamic_template_data = {
        'nombre_completo': nombre_completo,
        'correo': correo,
        'direccion': direccion,
        'telefono': telefono,
        'mensaje': mensaje
    }
    message.template_id = settings.SENDGRID_TEMPLATE_CONTACT_ID
    
    try:
        sg = SendGridAPIClient(
            api_key=settings.SENDGRID_API_KEY
        )
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)