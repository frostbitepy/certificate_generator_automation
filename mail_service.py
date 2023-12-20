import smtplib
from email.mime.text import MIMEText

def enviar_correo(destinatario, nombre):
    # Crea el mensaje
    mensaje = MIMEText(f'Haz click en el siguiente link para descargar tu certificado: http://localhost:5000/descargar_certificado/{nombre}')
    mensaje['Subject'] = 'Descarga tu certificado'
    mensaje['From'] = 'tu_correo@gmail.com'
    mensaje['To'] = destinatario

    # Envia el correo
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('tu_correo@gmail.com', 'tu_contraseña')
    servidor.send_message(mensaje)
    servidor.quit()