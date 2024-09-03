
## Interactive Learning Chatbot

## Overview
This project is an interactive Python-based chatbot that learns from user interactions by dynamically updating its knowledge base. The chatbot uses natural language processing to understand user queries and provides relevant responses, improving over time as it learns from new questions.

## Features
- **Dynamic Learning**: The chatbot prompts users for answers to unknown questions and stores them for future use.
- **Query Matching**: Implements a matching algorithm using `difflib` to find the closest match to user queries, ensuring accurate responses.
- **Knowledge Base**: Utilizes a JSON-based knowledge base that is updated in real-time as the chatbot learns new information.

## Technologies Used
- **Python**: Core programming language for implementing the chatbot.
- **JSON**: Used for storing and updating the knowledge base.
- **difflib**: Library used to match user queries with stored questions.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/interactive-learning-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd interactive-learning-chatbot
   ```
3. Run the chatbot:
   ```bash
   python chatbot.py
   ```
4. Start interacting with the chatbot in the terminal.

## Usage
- Type a question to receive an answer from the chatbot.
- If the chatbot does not know the answer, it will ask you to provide one, which it will remember for future interactions.
- To quit the chatbot, type `quit`.

## Future Improvements
- Implement a graphical user interface (GUI) for better user interaction.
- Expand the knowledge base with more diverse topics.
- Improve the matching algorithm for even more accurate responses.
