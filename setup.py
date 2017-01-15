from setuptools import setup, find_packages

setup(
    name='nameko-elasticsearch',
    version='0.1-beta',
    description='@TODO',
    long_description='@TODO',
    author='Fill Q',
    author_email='fill@njoyx.net',
    url='https://github.com/NJoyX/nameko-elasticsearch',
    license='Apache License, Version 2.0',
    packages=find_packages(),
    install_requires=[
        "nameko",
        "six",
        "requests",
        "elasticsearch-dsl>=5.0.0,<6.0.0"
    ],
    include_package_data=True,
    zip_safe=True,
    keywords=['nameko', 'elasticsearch', 'database', 'search'],
    classifiers=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)
