class Model:
    def __init__(self):
        self.word_types = {}  # Dictionary to store word-to-type mappings

    def train(self, wordtype_data):
        """Train the model by populating the knowledge base, word types, and meanings."""
        # Load sayings and word types from sayings_data
        for line in wordtype_data:
            parts = line.split(',', 2)  # Split into word, type
            if len(parts) == 2:
                word, word_type = parts[0].strip(), parts[1].strip()
                self.word_types[word.lower()] = word_type

    def predict(self, data):
        """Respond based on the user's prompt."""
        predictions = []
        for prompt in data:
            # Extract the word from the prompt
            word = prompt.split()[-1].strip("'\"?.!")
            word_lower = word.lower()

            # Determine the intent based on the prompt
            if "type of word" in prompt.lower():
                # Respond with the word type
                word_type = self.word_types.get(word_lower, "unknown")
                predictions.append(f"The word '{word}' is a {word_type}.")
    
            else:
                # Default response if the intent is unclear
                predictions.append(f"I'm not sure what you're asking about '{word}'.")
        return predictions

    def evaluate(self, predictions, processed_data):
        """Dummy evaluate method (not needed for this implementation)."""
        return {"accuracy": 1.0}  # Placeholder for evaluation logic
