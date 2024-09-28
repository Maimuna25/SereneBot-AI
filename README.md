# SereneBot AI

SereneBot is an AI-powered chatbot designed to provide emotional support by helping users manage and understand their emotions. Users can tell the chatbot how they're feeling, and based on their mood, SereneBot offers tailored solutions, advice, and coping strategies.

## Table of Contents

- Features
- Getting Started
- Installation
- Usage
- How It Works
- Contributing
- License
## Features

- **Emotion Detection**: SereneBot detects user emotions based on the text input.
- **Personalized Suggestions**: Provides advice, solutions, or motivational responses based on the mood expressed by the user.
- **Unrecognized Question Logging**: Logs questions or emotions that SereneBot can't interpret for further improvements.
- **Question Clustering**: Uses machine learning (K-Means clustering) to group common unrecognized questions for future learning.
## Getting Started

To get a local copy of SereneBot AI up and running, follow these simple steps.

### Prerequisites
- **Python 3.7+**

- Required libraries (listed in requirements.txt)
  
### Installation
1. Clone the repository:

git clone https://github.com/your-username/SereneBot-AI.git

2. Navigate to the project directory:

cd SereneBot-AI

3. Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

4. Install the required dependencies:

pip install -r requirements.txt

## Usage

Once you've installed the dependencies, you can interact with SereneBot.

1. Run the chatbot:

python chatbot.py

2. Chat with SereneBot by typing in how you're feeling:

User: I'm feeling anxious.

SereneBot: I'm sorry to hear that you're feeling anxious. Here are a few things you could try: deep breathing exercises, journaling your thoughts, or taking a short walk.

3. Logging unrecognized questions: If SereneBot doesn't recognize how you're feeling, your question is logged for future analysis and improvements.
4. Clustering Analysis: You can run the clustering script to analyze unrecognized questions and see common themes:

python cluster_unrecognized_questions.py

## How It Works

### Emotional Analysis
The chatbot uses predefined categories to match user input to emotions like happiness, sadness, stress, anxiety, etc. It then responds with advice based on these emotions.

### Machine Learning for Clustering
The cluster_unrecognized_questions() method uses TF-IDF vectorization and K-Means clustering to group unrecognized questions for analysis. This helps in improving the bot's responses over time.

### Logging
Unrecognized user inputs are stored in a JSON file (unrecognized_questions.json) so developers can track which emotions or phrases the bot doesn't yet understand. These can be reviewed and added to future versions.

## Contributing

Contributions are welcome! If you would like to contribute, please:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-name.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-name.
Submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
