from setuptools import setup, find_packages

setup(
  name="simplebot",
  version="1.0.0",
  url="https://github.com/im-strange/simplebot.git",
  author="Samuel Genoguin",
  description="Module for your own simple chatbot.",
  packages=find_packages(),
  include_package_data=True,
  package_data={
    "": ["data/sample-intents.json"]
  }
)
