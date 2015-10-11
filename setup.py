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
    url='',
    author='Cello Hsueh',
    license='MIT',
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
    zip_safe=False
)