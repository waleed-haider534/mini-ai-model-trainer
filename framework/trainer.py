"""Trainer class for training models"""

from .base_model import BaseModel
from .data_loader import DataLoader


class Trainer:
    """Trainer class that coordinates model training and evaluation"""

    def __init__(self, model: BaseModel, data_loader: DataLoader):
        """Initialize trainer with a model and data loader"""
        self.model = model
        self.data_loader = data_loader

    def run(self):
        """Run training and evaluation"""
        data = self.data_loader.get_data()
        self.model.train(data)
        self.model.evaluate(data)