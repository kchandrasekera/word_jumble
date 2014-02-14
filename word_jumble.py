def word_jumble():
  scrambled_word = raw_input('Enter a word to scramble: ')
  matching_words = []
  scrambled_word_length = len(scrambled_word)
  dictionary = import_dictionary('dictionary.txt')
  dictionary.sort(key = len)
  for word in dictionary:
    if len(word) > scrambled_word_length:
      if scrambled_word in matching_words: matching_words.remove(scrambled_word)
      break
    if matching_word(word, scrambled_word):
      matching_words.append(word)
  return matching_words


def import_dictionary(file):
  dictionary_file = open(file)
  dictionary = dictionary_file.read().splitlines()
  dictionary_file.close()
  return dictionary


def matching_word(word, scrambled_word):
  characters = list(scrambled_word)
  for letter in word:
    if letter in characters:
      characters.remove(letter)
    else:
      return False
  return True


print word_jumble()
