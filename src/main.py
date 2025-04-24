import os
from agents.base_agent import BaseAgent
from models.model import Model
from utils.helpers import load_data, preprocess_data

def interact_with_model(model):
    while True:
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        prediction = model.predict([prompt])  # Assuming predict can handle a list of inputs
        print(f"Prediction: {prediction}")
        
def main():
    # Initialize the AI agent
    agent = BaseAgent()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    wordtype_path = os.path.join(current_dir, <path to your dataset> eg.'/Users/jv.ravichandran/ai-agent-project/src//data/dataset.csv')
    
    # Load and preprocess data
    wordtype_data = load_data(wordtype_path)
    if wordtype_data is None:
        print(f"Error: Failed to load data from {wordtype_path}.")
        return
   
    processed_word = preprocess_data(wordtype_data)
    
    if processed_word is None:
        print("Error: Failed to preprocess data.")
        return

    # Initialize the model
    model = Model()
    
    model.train(processed_word)

    interact_with_model(model)

if __name__ == "__main__":
    main()
