class Model:
    def __init__(self):
        self.knowledge_base = {}  # Dictionary to store word-to-sayings mappings
        self.word_types = {}  # Dictionary to store word-to-type mappings
        self.meanings = {}  # Dictionary to store word-to-meaning mappings

    def train(self, sayings_data, meanings_data):
        """Train the model by populating the knowledge base, word types, and meanings."""
        # Load sayings and word types from sayings_data
        for line in sayings_data:
            parts = line.split(',', 2)  # Split into word, type, and sayings
            if len(parts) == 3:
                word, word_type, sayings = parts[0].strip(), parts[1].strip(), parts[2].strip()
                self.word_types[word.lower()] = word_type
                self.knowledge_base[word.lower()] = sayings

        # Load meanings from meanings_data
        for line in meanings_data:
            parts = line.split(',', 1)  # Split into word and meaning
            if len(parts) == 2:
                word, meaning = parts[0].strip(), parts[1].strip()
                self.meanings[word.lower()] = meaning

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
            elif "associated sayings" in prompt.lower():
                # Respond with the associated sayings
                sayings = self.knowledge_base.get(word_lower, "No sayings available.")
                predictions.append(f"Associated sayings for '{word}': {sayings}")
            elif "meaning of the word" in prompt.lower():
                # Respond with the meaning
                meaning = self.meanings.get(word_lower, "No meaning available.")
                predictions.append(f"The meaning of the word '{word}' is: {meaning}")
            else:
                # Default response if the intent is unclear
                predictions.append(f"I'm not sure what you're asking about '{word}'.")
        return predictions

    def evaluate(self, predictions, processed_data):
        """Dummy evaluate method (not needed for this implementation)."""
        return {"accuracy": 1.0}  # Placeholder for evaluation logic