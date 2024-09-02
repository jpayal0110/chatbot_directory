import json
from difflib import get_close_matches #gives the closest match

#load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file: #open file path as reading file
        data: dict = json.load(file)
    return data

#save the old responses from the user to answer the future questions
def save_knowledge_base(file_path: str, data:dict):
    with open(file_path, 'w') as file: #open file path as writing file
        json.dump(data,file, indent=2)
    
def find_best_match(user_question: str, questions:list[str]) -> str | None:
    #matches is list which is implementing function get_close_matches
    #where funct takes user_questions, give the best matching no. 1 with 60% SIMILARITY i.e. 0.6
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None: #| is or -> str or None
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    

def chat_bot():
    #variable for knowledge_base
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == "quit":
            break
        
        #best match in json
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer : str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            #add new answer to knowledge base
            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print('Bot: Thank you! I learned a new response!')

if __name__ == '__main__':
    chat_bot()
