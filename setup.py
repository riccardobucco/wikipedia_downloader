"""Build script for setuptools."""

# Standard library imports
import setuptools

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="wikipedia_downloader",
    version="0.2",
    author="Riccardo Bucco",
    description="Download Wikipedia data dumps",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/riccardobucco/wikipedia_downloader",
    author_email="riccardobucco@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords="wikipedia dump download",
    packages=setuptools.find_packages()
)
