# -*- coding: utf-8 -*- 

from setuptools import setup, find_packages


EXCLUDE_FROM_PACKAGES = [
    'flask_go.project_template',
    #'flask_go.project_template.project_name',
    'flask_go.app_template'
]

setup(
    name='flask-go',
    version='0.1',
    description='Let you create flask project like use django-admin',
    url='https://github.com/CelloCello/flask-go',
    author='Cello Hsueh',
    author_email="cello1124@gmail.com",
    license='BSD',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    scripts=['bin/flask-go.py'],
    entry_points={'console_scripts': [
        'flask-go = flask_go.management:execute_from_command_line',
    ]},
    install_requires=[
        'flask',
        'flask-script',
    ], 
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]    
)