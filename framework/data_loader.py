"""Data loader for loading datasets"""


class DataLoader:
    """Data loader class for managing datasets"""

    def __init__(self, dataset):
        """Initialize with a dataset"""
        self.dataset = dataset

    def get_data(self):
        """Return the dataset"""
        return self.dataset