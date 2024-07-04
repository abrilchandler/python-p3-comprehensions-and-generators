#!/usr/bin/env python3

def return_evens(num_list):
    num_list_even = [num for num in num_list if num % 2 == 0]
    return num_list_even
def make_exclamation(sentence_list):
    exclamation = "!"
    exclamation_sentence_list = [sentence + exclamation for sentence in sentence_list if sentence]
    return exclamation_sentence_list