# quiz-maker-with-ai
This is a simple Python script that generates vocabulary quizzes (multiple choice gap-fill exercise) using OpenAI API to generate sample sentences. 
I wrote it to speed up the process of creating quizzes for my students on kahoot.com - the program generates questions in a format that can be directly uploaded on the platform. 

# Requirements 
## Packages 
To run the program you'll need Python and the following packages installed: 
* random
* openai
* os

## OpenAI API key 
Unfortunately, the project is based on a paid service provided by OpenAI so setting up an account at https://platform.openai.com/ and getting an API key is required. 
Once you generate your API key save it as an environment variable OPENAI_API_KEY

# Use 
The program takes a list of vocabulary items (as a txt file) and creates two csv files: 
* *[name]-sample-sents.csv* which stores one sample sentence for each of the vocabulary items provided
*  *questions.csv which* which contains questions together with multiple-choice options, formatted in the following way:
  ```
The sudden _____ of her hidden talent left everyone in awe.;reception;reflection;resolution;revelation;20;4;
```
that is the format required by kahoot.com and the fields correspond to  
* question
* option1
* option2
* option3
* option4
* number of seconds to answer
* correct option

once the questions.csv file is generated can be uploaded to kahoot.com
The incorrect options are provided by searching for similar words in [this dictionary](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt) of most common English words. 

Note: To create and host quizzes on the platform you'll need to log in or sign up

# Disclaimer
As AI plays a big role in this process, the results are not completely predictable and the quizzes require reviewing before using them in a classroom. 
