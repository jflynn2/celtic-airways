from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fy#4mz2=36r9tez)6hvc#oe@)c26y=2g)%e51jyg2c#9_0qid0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)