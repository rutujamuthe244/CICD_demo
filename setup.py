# Databricks notebook source
from setuptools import setup, find_packages

setup(
    name='RepoPOC',  # Name of your project/package
    version='0.1.0',  # Version of your package
    description='Databricks notebooks for creating tables',
    author='Rutuja',  # Replace with your name
    author_email='rutujamuthe24@gmail.com',  # Replace with your email
    url='https://github.com/rutujamuthe244/CICD_demo/',  # Replace with your GitHub repository URL
    packages=find_packages(),  # Automatically find all packages in the repo
    include_package_data=True, # Include data files specified in package_data
    package_data={
        '': ['/*.ipynb'],  # Include all .dbc files from the DDL folder
    },
    install_requires=[],  # List dependencies here if needed (e.g., pandas, numpy)
    python_requires='>=3.7',  # Minimum Python version required
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)



