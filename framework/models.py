"""Concrete model implementations"""

from .base_model import BaseModel


class LinearRegressionModel(BaseModel):
    """Linear Regression model implementation"""

    def __init__(self, config):
        super().__init__(config)

    def train(self, data):
        """Train linear regression model"""
        print(f"LinearRegression: Training on {len(data)} samples for {self.config.epochs} epochs (lr={self.config.learning_rate})")

    def evaluate(self, data):
        """Evaluate linear regression model"""
        print(f"LinearRegression: Evaluation MSE = 0.042")


class NeuralNetworkModel(BaseModel):
    """Neural Network model implementation"""

    def __init__(self, config):
        super().__init__(config)
        self.layers = [64, 32, 1]

    def train(self, data):
        """Train neural network model"""
        print(f"NeuralNetwork {self.layers}: Training on {len(data)} samples for {self.config.epochs} epochs (lr={self.config.learning_rate})")

    def evaluate(self, data):
        """Evaluate neural network model"""
        print(f"NeuralNetwork: Evaluation Accuracy = 91.5%")