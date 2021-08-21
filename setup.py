from setuptools import setup, find_packages

import hiddeneye_reborn

# META DATA
__author__ = "Open Security Group"
# TODO add author email to get rid of warning
__version__ = hiddeneye_reborn.__version__
__package_name__ = "hiddeneye_reborn"
__description__ = "Appropriate Phishing Tool"
__python_requires__ = ">=3.6.*"
__install_requires__ = ['pywebcopy', 'py7zr', 'pyyaml', 'rich' ]
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
            'hiddeneye-reborn = hiddeneye_reborn.hiddeneye_reborn:main',
            'hiddeneye = hiddeneye_reborn.hiddeneye_reborn:main'
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
        "Topic :: Education :: Testing",
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: Utilities",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
