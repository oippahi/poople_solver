import json


class Word:
    def __init__(self, word, list):
        self.word = word
        self.list = list

    def __str__(self):
        return f"Word: {self.word}, earlier words: {self.list}"

"""
Function makes a list of words from a .json file. All words in file should be 4 letters long.
:return
list_of_words = a list of words
"""
def make_list_of_words():
    with open("words.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    list_of_words = [item["word"] for item in data]

    return list_of_words


"""
:param
list_of_words = database of all 4 letter words
original_word = the word that we are trying to change by one letter
list_of_objects = list that contains words turned into objects. Object includes the word and prior words
needed to get to the word
word_of_day = word we are trying to get to changing one letter at a time

:return
new_word = returns object new_word if new_word == word_of_day
"""
def change_one_letter(list_of_words, original_word, list_of_objects, word_of_day):
    original_index = next(i for i, obj in enumerate(list_of_objects) if obj.word == original_word)
    #Find words that differ by one letter
    for word in list_of_words:
        if sum(a != b for a, b in zip(original_word, word)) != 1:
            continue

        #Makes an object of the word and adds it to the list.
        if check_if_earlier(word, list_of_objects):
            new_word = Word(word, list(list_of_objects[original_index].list))
            new_word.list.append(original_word)
            list_of_objects.append(new_word)
            if new_word.word == word_of_day:
                return new_word

"""
Checks if word is a word value in the list_of_objects
"""
def check_if_earlier(word, list_of_objects):
    return not any(obj.word == word for obj in list_of_objects)


def main():
    word_of_day = str.lower(input("Input today's word: "))
    list_of_objects = [Word("poop", [])]
    list_of_words = make_list_of_words()

    i = 0
    while True:
        result = change_one_letter(list_of_words, list_of_objects[i].word, list_of_objects, word_of_day)
        if result is not None:
            print(result)
            break
        i += 1


if __name__ == '__main__':
    main()
