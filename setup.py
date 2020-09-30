from setuptools import setup, find_packages

__author__ = "Open Security Group"
__version__ = "0.0a1.dev1"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="hidden-eye-reborn-OSG",
    version=__version__,
    author=__author__,
    description="I'll write that later",
    python_requires=">=3.6",  # TODO replace with script
    install_requires=[
        'pywebcopy',
    ],
    url="https://github.com/Open-Security-Group-OSG/HiddenEyeReborn",
    license="The Unlicense",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    data_files=[("", ["LICENSE"])],
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
