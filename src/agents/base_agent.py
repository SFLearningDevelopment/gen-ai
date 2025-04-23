class BaseAgent:
    def __init__(self):
        self.model = None

    def initialize(self, model):
        self.model = model

    def act(self, observation):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def learn(self, experience):
        raise NotImplementedError("This method should be overridden by subclasses.")