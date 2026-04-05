"""Base model abstract class"""

from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Abstract Base Class for all models"""

    model_count = 0

    def __init__(self, config):
        """Initialize the model with a ModelConfig object"""
        BaseModel.model_count += 1
        self.config = config

    @abstractmethod
    def train(self, data):
        """Train the model on the provided data"""
        pass

    @abstractmethod
    def evaluate(self, data):
        """Evaluate the model on the provided data"""
        pass