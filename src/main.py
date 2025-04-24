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
    sayings_path = os.path.join(current_dir, '/Users/jv.ravichandran/ai-agent-project/src//data/dataset.csv')
    meanings_path = os.path.join(current_dir, '/Users/jv.ravichandran/ai-agent-project/src//data/meanings.csv')
    
    # Load and preprocess data
    sayings_data = load_data(sayings_path)
    if sayings_data is None:
        print(f"Error: Failed to load data from {sayings_path}.")
        return
    meanings_data = load_data(meanings_path)
    if meanings_data is None:
        print(f"Error: Failed to load data from {meanings_path}.")
        return

    processed_sayings = preprocess_data(sayings_data)
    processed_meanings = preprocess_data(meanings_data)
    if processed_sayings is None or processed_meanings is None:
        print("Error: Failed to preprocess data.")
        return

    # Initialize the model
    model = Model()
    
    model.train(processed_sayings, processed_meanings)

    interact_with_model(model)

if __name__ == "__main__":
    main()