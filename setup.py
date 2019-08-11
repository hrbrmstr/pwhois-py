import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywhois",
    version="1.0",
    author="W. Dean Freeman",
    author_email="badfilemagic@gmail.com",
    description="A Python client for Prefix Whois (pwhois) servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/badfilemagic/pwhois-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent"
    ],
)