"""
Execute the Markov Chain of the data and produce the output
"""
import data_retrieval
from markov_python.cc_markov import MarkovChain

data_retrieval.retr()
mc = MarkovChain()
mc.add_file("gulistan-raw.txt")
sentence = mc.generate_text(10)
print "\nGENERATED SENTENCE: "
sentence[0] = sentence[0]
for i in range(0, len(sentence)):
    print sentence[i],
