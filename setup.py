import os
from setuptools import setup, find_packages


setup(
    name='quentin',
    version=0.0,
    author='Code Hat Labs, LLC',
    author_email='dev@codehatlabs.com',
    url='https://github.com/CodeHatLabs/quentin',
    description='Django tools for Elastic Beanstalk Web/Worker Deployments',
    packages=find_packages(),
    long_description="",
    keywords='django',
    zip_safe=False,
    install_requires=[
        'ebpy>=0.0'
    ],
    test_suite='',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
