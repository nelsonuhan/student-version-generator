import setuptools

long_description = ''

setuptools.setup(
    name='studentversiongenerator',
    version='0.1',
    description='''
        Create a student version of a Jupyter notebook:
        clear outputs, remove all cells tagged with "solution"
    ''',
    long_description=long_description,
    url='',
    author='Nelson Uhan',
    author_email='nelson@uhan.me',
    license='MIT',
    packages=['studentversiongenerator'],
    install_requires=['nbconvert', 'traitlets'],
    entry_points={
        'console_scripts': [
            'sv = studentversiongenerator.generator:main'
        ],
    }
)
