from setuptools import setup, find_packages

setup(
    name='cli-calculator',
    version='0.1',
    packages=['app', 'tests'],
    url='',
    license='MIT License',
    author='Jesús Andrés Hincapié',
    author_email='jahlon@outlook.com',
    description='A simple CLI calculator',
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        calc=app.calculator:calc
    '''
)
