from setuptools import setup

setup(
    name='hyperball',
    version='0.1',
    packages=['iperpalla'],
    entry_points='''
        [console_scripts]
        check-similarity=similarity:main
    ''',
)


