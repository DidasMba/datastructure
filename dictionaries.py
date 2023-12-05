import re

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Sample input
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
