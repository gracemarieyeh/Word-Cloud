# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:15:42 2020

@author: grace
"""

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    
    #list of words without punctuations
    
    newstring = '' #create new empty string to store string w/o punctuation
    lowercase = []
    
    list_words = file_contents.split()
    
    for word in list_words:
        word = word.lower()
        lowercase.append(word)
    
    for word in lowercase:
        for char in word:
            if char.isalpha() == True:
                continue
            elif char in punctuations:
                    word = word.replace(char,"")
                #print(word)
        newstring += word + ' '
        
    newlist1 = newstring.split()         

    #list of words without uninteresting words
    newlist2 = []
    for word in newlist1:
        if word in uninteresting_words:
            continue
        else:
            newlist2.append(word)
            
    #generate dictionary
    freq_dictionary = {} #define empty dictionary
    
    for word in newlist2:
        if word not in freq_dictionary: #add words into the dictionary
            freq_dictionary[word] = 1
        else:
            freq_dictionary[word] += 1
    return freq_dictionary

file_contents = input('Enter text: ')

dictionary = calculate_frequencies(file_contents)
print(dictionary)

