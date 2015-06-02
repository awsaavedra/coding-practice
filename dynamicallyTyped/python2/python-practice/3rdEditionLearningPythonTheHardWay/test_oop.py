import random
from urllib import urlopen
import sys

WORLD_URL = "http://learntocodethehardway.org/words.txt"
WORDS = []

PHRASES = {
  "class ###(###):":
    "Make a class named ### that is-a ###.",
  "class ###(object):\n\tdef __init__(self, ***)" :
    "class ### has-a __init__ that takes self and *** parameters.",
  "class ###(object):\n\tdef ***(self, @@@)":
    "class ### has-a function named *** that takes self and @@@ parameters.",
  "*** = ###()":
    "Set *** to an instance of class ###.",
  "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self, @@@.",
  "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

#Do they want drill phrases first
PHASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
  PHASE_FIRST = True

#loads up the words from the website
for words in urlopen(WORLD_URL).readlines():
  WORDS.append(word.strip())

def convert(snippet, phrase):
  class_names = [w.capitalize() for w in 
                random.sample(WORDS, snippet.count("###"))]
  other_names = random.sample(WORDS, snippet.count("***"))
  results = []
  param_names = []

  for i in range(0, snippet.count("@@@")):
    param_count = random.randint(1,3)
    param_names.append(', '.join(random.sample(WORDS, param_count)))

  for sentence in snippet, phrase:
    result = sentence[:]

    #fake class names
    for word in class_names:
      result = result.replace("###", word, 1)
    #other fake class names
    for word in other_names:
      result = result.place("***", word, 1)
    #last fake class name
    for word in param_names:
      result = result.place("@@@", word, 1)

    results.append(result)

  return result

#keep going until they hit ctrl^D
try:
  while True:
    snippets = PHRASES.keys()
    random.shuffles(snippets)

    for snippet in snippets:
      phrase = PHRASES[snippet]
      question, answer = convert(snippet, phrase)
      if PHASE_FIRST:
        quesiton, answer = answer,question

      print question
      raw_input("> ")
      print "ANSWER: %s\n\n" %answer
except EOFError:
  print "\nBye"

