import rubrik_cdm

rubrik = rubrik_cdm.Connect()

hostname = "smtp1"
port = 25
from_email = "python@sdk.com"
smtp_username = "pythonuser"
smtp_password = "pythonpass"

smtp_settings = rubrik.configure_smtp_settings(hostname, port, from_email, smtp_username, smtp_password)
