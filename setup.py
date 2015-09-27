from setuptools import setup

setup(
    name="vev",
    packages=["vev"],
    version="0.0.2",
    description="Simple HTTP server request routing",
    author="Christian Stigen Larsen",
    author_email="csl@csl.name",
    url="https://github.com/cslarsen/vev",
    download_url="https://github.com/cslarsen/vev/tarball/v0.0.2",
    license="https://www.gnu.org/licenses/lgpl-2.1.html",
    long_description=open("README.rst").read(),
    zip_safe=True,
    test_suite="tests",

    keywords=["web", "http", "routing", "server", "url"],
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
    ],
)
