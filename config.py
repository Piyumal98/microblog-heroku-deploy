import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://ttakpcjxtrnymq:d0c134048277e419f0452f9fa08f1d5e6925f0a0617b69d2a73944bd967163ba@ec2-52-200-5-135.compute-1.amazonaws.com:5432/da8qac8jdae2mc', \
            'postgresql://ttakpcjxtrnymq:d0c134048277e419f0452f9fa08f1d5e6925f0a0617b69d2a73944bd967163ba@ec2-52-200-5-135.compute-1.amazonaws.com:5432/da8qac8jdae2mc') or \
        'sqlite:///ttakpcjxtrnymq:d0c134048277e419f0452f9fa08f1d5e6925f0a0617b69d2a73944bd967163ba@ec2-52-200-5-135.compute-1.amazonaws.com:5432/da8qac8jdae2mc' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    POSTS_PER_PAGE = 25
