from setuptools import setup

setup(
  name="simplebot",
  version="1.0.0",
  url="https://github.com/im-strange/simplebot.git",
  author="im-strange",
  description="Module for your simple chatbot.",
  include_package_data=True,
  packages=[
    "simplebot"
  ],
  package_data={
    "simplebot": ["data/*.json"]
  }
)
