# quiz-maker-with-ai
This is a simple Python script that generates vocabulary quizzes (multiple choice gap-fill exercise) using OpenAI API to generate sample sentences. 
I wrote it to speed up the process of creating quizzes for my students on kahoot.com - the program generates questions in a format that can be directly uploaded on the platform. 

## Installation

1. Clone the repository: `git clone https://github.com/your-username/quiz-maker-with-ai.git`
2. Navigate to the project directory: `cd quiz-maker-with-ai`
3. Install required dependencies: `pip install -r requirements.txt`

### OpenAI API key 
Unfortunately, the project is based on a paid service provided by OpenAI so setting up an account at https://platform.openai.com/ and getting an API key is required. 
Once you generate your API key save it as an environment variable `OPENAI_API_KEY`

## Usage

1. Create a text file with a list of vocabulary items (e.g., `vocabulary.txt`).
2. Run the script: `python quiz_maker.py vocabulary.txt`
3. Two CSV files will be generated: `[name]-sample-sents.csv` and `questions.csv`.
4. Upload `questions.csv` to kahoot.com for quiz creation.
Note: To create and host quizzes on the platform you'll need to log in or sign up

## Acknowledgments
The incorrect options are provided by searching for similar words in [this dictionary](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt) of most common English words. 


# Disclaimer
As AI plays a big role in this process, the results are not completely predictable and the quizzes require reviewing before using them in a classroom. 
