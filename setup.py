from setuptools import setup

setup(
    name='test',
    version='0.1.0',
    packages=find_packages(include=['test', 'test.*'])
    install_requires=[
        'numpy>=1.14.5',
    ]
)

