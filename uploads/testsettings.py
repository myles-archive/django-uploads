DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': '/tmp/asgard-uploads-devel.db'
	}
}
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.sites',
	'django.contrib.sitemaps',
	
	'south',
	'django_markup',
	'taggit',
	
	'uploads',
]
ROOT_URLCONF = 'uploads.testurls'