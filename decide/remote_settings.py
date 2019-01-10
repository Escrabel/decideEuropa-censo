DEBUG = True

ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'https://decideeuropacenso.herokuapp.com',
    'base': 'https://decideeuropacenso.herokuapp.com',
    'booth': 'https://decideeuropacenso.herokuapp.com',
    'census': 'https://decideeuropacenso.herokuapp.com',
    'mixnet': 'https://decideeuropacenso.herokuapp.com',
    'postproc': 'https://decideeuropacenso.herokuapp.com',
    'store': 'https://decideeuropacenso.herokuapp.com',
    'visualizer': 'https://decideeuropacenso.herokuapp.com',
    'voting': 'https://decideeuropacenso.herokuapp.com',
}

BASEURL = 'https://decideeuropacenso.herokuapp.com'

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'dakir806ijcjbj',
#        'USER': 'jfiqfweoewadiu',
#	'PASSWORD': 'dcea99ecde4f1c66c6224a052bba6fa63b3b7c8bfc27d38a629608471f170215',
#        'HOST': 'ec2-174-129-41-12.compute-1.amazonaws.com',
#        'PORT': 5432,
#    }
#}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
