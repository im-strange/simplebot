# SimpleBot
Python simple chatbot wrapper. <br>![](https://badgen.net/badge/license/MIT/blue) ![](https://badgen.net/badge/simplebot/v1.0.0/blue)

## Installation

```
pip install git+https://github.com/im-strange/simplebot.git
```

## Documentation
### Setting up `intents.json`

The `SimpleBot` class takes json file where intents are listed.
The format of `.json` file should be as following:

```json
{
  "intents":
  [
    {
      "tag": "your_tag_here",
      "patterns": ["patterns here"],
      "responses": ["responses here"]
    }
  ]
}
```

### Example

```json
{
  "intents":
  [
    {
      "tag": "no_result",
      "patterns": [],
      "responses": ["sorry, I don't understand"]
    },
    {
      "tag": "greeting",
      "patterns": ["hi", "hello", "sup"],
      "responses": ["hi there!", "hello there!"]
    }
  ]
}
```

> Note: when none of the given tags fits with the input, it will redirect to the first tag, which is in this example the `no_result` tag.
<br>
<hr>

### Coding your chatbot

After creating your `intents.json` where tags, patterns, and responses
are listed, coding the bot is the next step.

```py
from simplebot import SimpleBot

bot = SimpleBot()
bot.train("intents.json")
response = bot.respond("hi")
print(response)

# output:
# Hi there!
```

In the code above, we import the class `SimpleBot` and initialize it as variable `bot`.
Then, we called the `train()` function to set the `intents.json`. Finally, we called the `respond()` function to give the response for the given
input, and print it in the end.
<br>

### Custom function

With `SimpleBot` you can add custom function when particular tag is reached.
We can do this by leaving the `responses` list blank.
<br>

For instance, I want to add a feature to my chatbot that gives me the weather everytime I asked for it.
We can do this by adding new tag to `intents.json`

```json
  ...
{
  "tag": "weather",
  "patterns": [
    "what is the weather?", 
    "can you give me the weather?",
    "what's the weather today?"
  ],
  "responses": []
}
  ...
```

In the code above, we added `weather` tag that has no responses.
Then, we can code the bot and add the function

```py
from simplebot import SimpleBot

bot = SimpleBot()
bot.train("intents.json")

def get_weather():
  # your code here
  # the function should return string

custom_functions = {
  "weather": get_weather
}

bot.set_functions(custom_functions)

response = bot.respond("what's the weather today?")
print(response)
``` 

In the code above, noticed that we added a function `get_weather` which returns string object. We then set the function by calling the `set_functions()`. We set the argument to variable `custom_functions` which
has tags as key, and function as value. Now, when `weather` tag is reached,
The returned object will be sent by bot.
<br>

> This repo is Licensed with MIT.
