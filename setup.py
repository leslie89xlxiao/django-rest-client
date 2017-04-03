import os

from setuptools import setup, find_packages

version = '1.0.0'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rest-client',
    version=version,
    description='Django rest client is a client to call other services.',
    author='leslie89xlxiao',
    author_email='leslie89xlxiao@gmail.com',
    url='https://github.com/leslie89xlxiao/django-rest-client',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 2.7',
    ]
)
