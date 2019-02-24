import setuptools

with open("README.md", "r") as fh:
    README = fh.read()

setuptools.setup(
    name="mscthr",
    version="0.0.1",
    author="aug0stus",
    author_email="",
    description="An implementation of music theory w/ Python",
    long_description=README,
    url="",
    packages=setuptools.find_packages()
)
