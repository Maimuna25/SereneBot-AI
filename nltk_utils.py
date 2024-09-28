import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from unrecognised_responses import log_unrecognized_question
from responses import responses

# Initialize NLTK tools
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


# Function to clean a question or input text
def clean_text(text):
    tokens = word_tokenize(text.lower())
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum()]
    return ' '.join(cleaned_tokens)


# Clean the responses dictionary
cleaned_responses = {}

for key, value in responses.items():
    if "questions" in value:
        cleaned_questions = [clean_text(q) for q in value["questions"]]
    else:
        cleaned_questions = []

    cleaned_responses[key] = {
        "questions": cleaned_questions,
        "response": value["response"],
        "solution": value.get("solution")
    }


# Preprocess the user input
def preprocess_input(text):
    cleaned_text = clean_text(text)
    return set(cleaned_text.split())


# Define the get_response function
def get_response(user_input):
    cleaned_input = preprocess_input(user_input)
    for key,value in cleaned_responses.items():
        for question in value.get("questions", []):
            cleaned_question = set(question.split())
            if cleaned_question.issubset(cleaned_input):
                response = value['response']
                solution = value.get("solution")
                if solution:
                    response += f" Here's a suggestion: {solution}"
                return response

    # Log the unrecognized question if no match is found
    log_unrecognized_question(user_input)

    # Return the unknown response
    return cleaned_responses['unknown']['response']

