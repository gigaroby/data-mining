from setuptools import setup

setup(
    name='similarity',
    version='0.1',
    packages=['similarity'],
    entry_points='''
        [console_scripts]
        check-similarity=similarity:main
    ''',
)


