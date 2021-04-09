from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='dev-radio',
    version='1.0.0',
    description="A simple cmdline radio to listen to python podcasts and some music.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Legion-God/dev-radio',
    author="Shubhendra Rajkarne",
    author_email='srajkarne10@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[],
    entry_points='''
        [console_scripts]
        dradio=src.main:dradio
    ''',
    python_requires=">=3.6",
)