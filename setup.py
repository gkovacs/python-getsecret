import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="getsecret",
    version="0.0.2",
    author="Geza Kovacs",
    author_email="noreply@gkovacs.com",
    description="Reads credentials from a yaml file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gkovacs/python-getsecret",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)