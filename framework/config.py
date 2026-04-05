"""Configuration module for model settings"""


class ModelConfig:
    """Configuration class for model parameters"""

    def __init__(self, model_name, learning_rate=0.01, epochs=10):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.epochs = epochs

    def __repr__(self):
        return f"[Config] {self.model_name} | lr={self.learning_rate} | epochs={self.epochs}"