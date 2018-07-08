"""
Execute the Markov Chain of the data and produce the output
"""
import data_retrieval
from markov_python.cc_markov import MarkovChain

data_retrieval.retr()
mc = MarkovChain()
mc.add_file("gulistan-raw.txt")
sentence = mc.generate_text(20)
output = ""
for item in sentence:
    print item,
