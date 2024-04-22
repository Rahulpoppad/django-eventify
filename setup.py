from distutils.core import setup

setup(
  name = 'django_eventify',
  packages = ['django_eventify'],
  version = '0.7',
  license='MIT',
  description = 'Event management utility classes',   # Give a short description about your library
  author = 'Poppad Rahul',                   # Type in your name
  author_email = 'rahulpoppad.1999@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Rahulpoppad/django-eventify',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Rahulpoppad/django-eventify/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['EVENT', 'BOOKING'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'django',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)