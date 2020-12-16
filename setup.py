from pathlib import Path

from setuptools import find_packages, setup

README = Path("README.md").read_text()

setup(name="oh-my-papers",
      packages=find_packages(),
      description="Your research literature query through Python.",
      long_description=README,
      long_description_content_type="text/markdown",
      version="0.1.0",
      author="Zhihang Zheng, Mr-Milk",
      url="https://github.com/Squirtle692/Oh-my-papers",
      author_email="",
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Intended Audience :: Science/Research",
      ],
      python_requires='>=3.6',
      install_requires=[''],
      )
