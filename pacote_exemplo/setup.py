#!/usr/bin/env python3
from setuptools import setup

setup(
	name='my_hello_joaoppc',
	version='0.1',
	packages=['my_hello'],
	scripts=['scripts/hello.py'],
	install_requires=[
	'docutils>=0.3'
	]
	
	)
