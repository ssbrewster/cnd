DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cnd',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = '95xbfeqoxjbte1akxebwi12mxqik#t=x(ycq$3_59j-$)u+hp$'

RECAPTCHA_PUBLIC_KEY = '6LeAatwSAAAAAKadk_ui-53Mcod0u6UnUO5ZqxBq'
RECAPTCHA_PRIVATE_KEY = '6LeAatwSAAAAAPgojA4oRD55hDUfSXcprBvzRO-t'

ADMINS = (
    ('Jamie Neil', 'jamie.neil@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'jamie.neil@gmail.com'

CONTACT_SENDER = 'jamie.neil@gmail.com'

CONTACT_RECIPIENTS = [
    'jamie.neil@gmail.com',
]

SITE_BANNER = 'This is a demonstration site. DO NOT ENTER REAL DATA.'
