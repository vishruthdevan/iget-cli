from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='iget',
    version='1.0',
    py_modules=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        iget=iget:iget
    '''
)
