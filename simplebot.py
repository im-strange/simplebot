
import nltk
from nltk.tokenize import word_tokenize
import json
import random
import math
import os

# main class
class SimpleBot:
  def __init__(self):
    self.data = None
    self.functions = {}

  # set json file
  def train(self, json_file):
    self.data = json.load(open(json_file))

  # simplebot is expecting a functions to blank responses
  def set_functions(self, functions_dict):
    self.functions = functions_dict

  # calculate similarity of two phrase/sentences
  def get_similarity(self, phrase1, phrase2):
    n_similar_words = 0
    for word1 in word_tokenize(phrase1.lower()):
      for word2 in word_tokenize(phrase2.lower()):
        if word2 == word1:
          n_similar_words += 1
    return n_similar_words

  # get the tags of the index
  def get_category(self, main_index):
    category = self.data["intents"][main_index]["tag"]
    return category

  # get what tag does the phrase included
  def get_index(self, phrase):
    intents = self.data["intents"]
    similarity = 0
    similarity_list = []
    for item in intents:
      for pattern in item.get("patterns"):
        sim = self.get_similarity(pattern, phrase)
        similarity += sim
      similarity_list.append(similarity)
      similarity = 0
    return similarity_list.index(max(similarity_list))

  # give the best response
  def respond(self, phrase):
    index = (self.get_index(phrase))
    responses = self.data["intents"][index]["responses"]
    functions_dict = [func for func in self.functions]
    category = self.get_category(index)
    if category not in functions_dict:
      rand = random.randint(0, len(responses)) - 1
      response = responses[rand]
      return response
    elif category in functions_dict:
      category_function = self.functions.get(category)
      return category_function()

# chatbot implementation
class Chatbot:
  def __init__(self):
    self.json_file = "sample-intents.json"
    self.json_file_path = os.join(os.path.dirname(os.path.abspath(__file)), self.json_file)
    self.bot = SimpleBot()
    self.bot.train(self.json_file_path)

  # have a conversation
  def talk(self):
    try:
      while True:
        user = input("You> ")
        bot_response = self.bot.respond(user)
        print(f"Bot> {bot_response}")
    except KeyboardInterrupt:
      print("\rBot> Bye!")
      exit()
