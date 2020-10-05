from setuptools import setup, find_packages


# META DATA
__author__ = "Open Security Group"
__version__ = "0.0a1.dev2"
__package_name__ = "hiddeneye_reborn"
__description__ = "Appropriate Phishing Tool"
__python_requires__ = ">=3.6"
__install_requires__ = ['pywebcopy', ]
__data_files__ = [("", ["LICENSE"])]
__url__ = "https://github.com/Open-Security-Group-OSG/HiddenEyeReborn"

with open("README.md", "r") as readme:
    __long_description__ = readme.read()


setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    description=__description__,
    python_requires=__python_requires__,
    install_requires=__install_requires__,
    url=__url__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    data_files=__data_files__,
    entry_points= {
        "console_scripts": [
            'hiddeneye-reborn = HE_RE.HE_RE:main',
            'hiddeneye = HE_RE.HE_RE:main'
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Education :: Testing",
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
)
