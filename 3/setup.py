from setuptools import setup

setup(
    name='hyperball',
    version='0.1',
    packages=['iperpalla'],
    install_requires=['numpy'],
    entry_points='''
        [console_scripts]
        run-hyperball=iperpalla:main
    ''',
)


