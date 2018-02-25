

"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""

sentence = input('Go ahead, type anything you\'d like.\n')

def reverseWordOrder(sentence):

    sentence = sentence.split()
    sentence.reverse()
    sentence = " ".join(sentence)

    print(sentence)

reverseWordOrder(sentence)