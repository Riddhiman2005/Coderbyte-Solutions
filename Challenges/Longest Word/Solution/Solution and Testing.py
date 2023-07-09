
import re

def LongestWord(sen):
    # Remove punctuation and split the string into words
    words = re.findall(r'\w+', sen)

    # Find the longest word
    longest_word = max(words, key=len)

    return longest_word

# Testing the Function with Example Inputs 

print(LongestWord("fun&!! time"))  # Output: time
print(LongestWord("I love dogs"))  # Output: love
