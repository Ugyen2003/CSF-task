def reverse_words(input_string):
    words = input_string.split(' ')
    reversed_words = ' '.join(reversed(words))
    return reversed_words
input_string = "Hellow, how are you?"
reversed_string = reverse_words(input_string)
print(reversed_string) # Output: "you? are how Hellow,"