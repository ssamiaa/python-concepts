from collections import Counter

# sentence as input and lowercase
sentence = input("Enter a sentence: ").lower() 

words = sentence.split(" ")

frequencies = Counter(words) # counter + the result in a dictionary 

# displaying words in order of frequency
for word, freq in frequencies.most_common(): 
    print(f"{word}: {freq}")








