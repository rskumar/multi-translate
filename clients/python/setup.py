# coding: utf-8

"""
    multi-translate

    Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.  # noqa: E501

    The version of the OpenAPI document: 0.1.14
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "multitranslateclient"
VERSION = "0.1.14"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="multi-translate",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/rekon-oss/multi-translate/clients/python",
    keywords=["OpenAPI", "OpenAPI-Generator", "multi-translate"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.  # noqa: E501
    """
)
