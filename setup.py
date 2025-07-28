# setup.py

from setuptools import setup, find_packages

setup(
    name="game_sdk",
    version="0.1.0",
    packages=find_packages(include=["sdk", "sdk.*"]),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Hemanth Kumar Karthikeyan",
    description="A lightweight SDK for tracking game install and purchase events.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
