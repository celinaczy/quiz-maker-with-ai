import nltk
import csv
import random
import re
import openai
import time
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')


# convert txt files to python lists
def txt_to_list(filename):
    # opening the file in read mode
    my_file = open(filename, "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text 
    # when newline ('\n') is seen.
    data_into_list = data.split("\n")
    data_into_list = [word.lower() for word in data_into_list]

    my_file.close()
    return data_into_list


# common-words.txt contains 10.000 most common words in English (MIT license)
common_words = txt_to_list('common-words.txt.txt')

# returns a dictionary with sample sentences as values
def gap_fill_sents(filename):
    vocab_list = txt_to_list(filename)
    sample_sentence = 'Provide a sample sentence with the word '
    gap_fill_sents = {}
    # time.sleep(30)
    for word in vocab_list:
        if word.endswith('ing'):
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": sample_sentence + word + 'as an adjective'}])
        else:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": sample_sentence + word}])

        reply_content = completion.choices[0].message.content
        new_sent = reply_content.replace(str(word), '_____')
        gap_fill_sents[word] = new_sent

        # dictionary to csv     
        with open(filename[:-4] + '-' + 'sample-sents.csv', 'w') as f:
            f.write('sep=; \n')
            for k, v in gap_fill_sents.items():
                f.write(k)
                f.write(';')
                f.write(v)
                f.write('\n')

    return gap_fill_sents


mydict = gap_fill_sents('financial-crimes.txt')


# returns n random words to test
def test_set(mydict, word_number=10):
    keys = list(mydict.keys())
    # remove keys which are more than one word
    # to be improved later
    for key in keys:
        if " " in key:
            keys.remove(key)
    randomlist = random.sample(range(len(keys)), word_number)
    randomkeys = []
    for i in randomlist:
        randomkeys += [keys[i]]
    # for i in range(len(randomkeys)-1):
    #    randomkeys[i] = lemmatizer.lemmatize(randomkeys[i])
    return randomkeys


def questions_set(mydict, questions_number=10, o_number=4, seconds_number=20):
    wordlist = common_words
    randomkeys = test_set(mydict, questions_number)
    questions = []

    for x in range(len(randomkeys)):

        new_word = randomkeys[x]

        # create a list of all similar words
        similar_words = []

        for i in wordlist:
            if i != new_word and i not in similar_words and abs(len(new_word) - len(i)) < 2 and i.startswith(
                    new_word[:1]) and i.endswith(new_word[-3:]):
                similar_words += [i]
        if len(similar_words) < 3:
            for i in wordlist:
                if i != new_word and i not in similar_words and abs(len(new_word) - len(i)) < 2 and i.startswith(
                        new_word[0]) and i.endswith(new_word[-2:]):
                    similar_words += [i]
        if len(similar_words) < 3:
            for i in wordlist:
                if i != new_word and i not in similar_words and abs(len(new_word) - len(i)) < 2 and i.endswith(
                        new_word[-2:]):
                    similar_words += [i]
        if len(similar_words) < 3:
            similar_words += 'whatever'

        # randomly chose o_number of similar words and use them as options for multiple-chioce

        options = []
        options += [new_word]

        for i in random.sample(range(0, len(similar_words)), (o_number - 1)):
            options += [similar_words[i]]

        # shuffle by sorting alphabetically

        options.sort()

        # find the correct option
        correct_option = 0
        for i in range(0, (len(options))):
            if options[i] == new_word:
                correct_option = i + 1
        # delete brackets from definitions
        value = mydict[randomkeys[x]]
        if value[0] == '(':
            mydict[randomkeys[x]] = str(value[1:-1])

        # create a question with options, seconds_number and correct_option as a list
        question = []
        question += mydict[randomkeys[x]], *options, seconds_number, correct_option

        # add to list of questions
        questions += [question]
    # save questions to csv
    with open('questions.csv', 'w') as f:
        f.write('sep=; \n')
        for q in range(len(questions)):
            for i in questions[q]:
                f.write(str(i))
                f.write(';')
            f.write('\n')
    return questions


questions_set(mydict,3)
