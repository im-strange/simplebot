from setuptools import setup, find_packages

setup(
  name="simplebot",
  version="1.0.0",
  url="https://github.com/im-strange/simplebot.git",
  author="Samuel Genoguin",
  packages=find_packages(),
  packages_data={
    "simplebot": ["simplebot/sample-intents.json"]
  }
)
