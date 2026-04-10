from setuptools import setup, find_packages
from os import path
import io


def readme():
    this_directory = path.abspath(path.dirname(__file__))
    with io.open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
        return f.read()


setup(
    name="tradingeconomics",
    packages=find_packages(exclude=["tests*"]),
    version="4.5.9",
    description="Trading Economics API",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    author="Trading Economics",
    author_email="support@tradingeconomics.com",
    license="MIT",
    url="https://github.com/tradingeconomics/tradingeconomics-python",
    download_url="https://github.com/tradingeconomics/tradingeconomics-python/tree/main/dist",
    keywords=["tradingeconomics", "data"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
    ],
    install_requires=[
        "pandas>=2.0,<4",
        "websocket-client>=1.0",
    ],
)
