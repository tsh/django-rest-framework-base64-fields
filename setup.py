#!/usr/bin/env python
from __future__ import unicode_literals

import ast
import re
from setuptools import Command, setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('django_rest_framework_base64_fields/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


class Test(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test_project import main
        main()


setup(
    name='django-rest-framework-base64-fields',
    version=version,
    url='https://github.com/tsh/django-rest-framework-base64-fields',
    license='MIT',
    author='Anton Nikulin',
    author_email='tsh@codebakery.io',
    description='Django Rest Framework base64 file fields',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.7',
        'djangorestframework>=3.2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: djangorestframework',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={'test': Test},
)
