import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


# Function to log unrecognized questions to a file
def log_unrecognized_question(user_input):
    with open('unrecognized_questions.json', 'a') as f:
        json.dump({"question": user_input}, f)
        f.write("\n")


def cluster_unrecognized_questions():
    # Load unrecognised questions
    with open('unrecognized_questions.json', 'r') as f:
        unrecognized_questions = [json.loads(line)["question"] for line in f]

    # Vectorize the questions
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(unrecognized_questions)

    # Perform clustering
    kmeans = KMeans(n_clusters=5, random_state=42).fit(X)
    clusters = kmeans.labels_

    # Group questions by cluster
    clustered_questions = [[] for _ in range(5)]
    for idx, question in enumerate(unrecognized_questions):
        clustered_questions[clusters[idx]].append(question)

    return clustered_questions
