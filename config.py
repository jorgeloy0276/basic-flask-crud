from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'task_manager')
    SECRET_KEY = os.getenv('SECRET_KEY', 'supermegasecretkey')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your_email@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your_app_password')
    # MYSQL_HOST = 'localhost'
#     # MYSQL_USER = 'root'
#     # MYSQL_PASSWORD = ''
#     # MYSQL_DB = 'flask_crud_basic'
#     #
#     # SECRET_KEY = 'super_secret_key'