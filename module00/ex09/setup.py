from setuptools import setup, find_packages
"""This is the setup file for the ft_package package."""
setup(
    name="ft_package",
    version="0.0.1",
    description="My first package",
    author="hdiot",
    author_email="hdiot@student.42nice.fr",
    url="https://github.com/LeDiabetique/Piscine-DataScience/tree/main/\
module00/ex09/ft_package",
    license="MIT",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    packages=find_packages(),
)
