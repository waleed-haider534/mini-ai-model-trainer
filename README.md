# Mini AI Model Trainer

A lightweight AI Model Trainer Framework built using Object-Oriented Programming (OOP) concepts in Python. This framework demonstrates core OOP principles including abstraction, inheritance, encapsulation, and composition while providing a flexible foundation for training machine learning models.

## Features

- **Modular Architecture**: Clean separation of concerns with independent modules for configuration, models, data loading, and training
- **Abstract Base Model**: Define custom models using the `BaseModel` abstract class
- **Multiple Model Types**: Pre-built implementations for Linear Regression and Neural Network models
- **Configurable Training**: Customizable learning rate and epoch settings via `ModelConfig`
- **Extensible Design**: Easily add new model types by extending the `BaseModel` class

## Project Structure

```
mini-ai-model-trainer/
├── framework/
│   ├── __init__.py         # Framework package initialization
│   ├── base_model.py       # Abstract base class for all models
│   ├── config.py           # Model configuration class
│   ├── data_loader.py     # Data loading utility
│   ├── models.py           # Concrete model implementations
│   └── trainer.py           # Training orchestration
├── main.py                 # Main entry point
└── README.md               # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/waleed-haider534/mini-ai-model-trainer.git
```

2. Navigate to the project directory:
```bash
cd mini-ai-model-trainer
```

3. Run the project (Python 3.7+ required):
```bash
python main.py
```

## Usage Example

```python
from framework.config import ModelConfig
from framework.models import LinearRegressionModel, NeuralNetworkModel
from framework.data_loader import DataLoader
from framework.trainer import Trainer

# Create model configuration
config = ModelConfig("LinearRegression", learning_rate=0.01, epochs=10)

# Create a model
model = LinearRegressionModel(config)

# Load data
data_loader = DataLoader([1, 2, 3, 4, 5])

# Train the model
trainer = Trainer(model, data_loader)
trainer.run()
```

## OOP Concepts Demonstrated

### 1. Abstraction
The `BaseModel` abstract class defines a common interface (`train()` and `evaluate()` methods) that all concrete models must implement. This abstraction allows the framework to work with any model type without knowing the specific implementation details.

### 2. Inheritance
`LinearRegressionModel` and `NeuralNetworkModel` inherit from `BaseModel`, reusing its structure while implementing their own training and evaluation logic.

### 3. Encapsulation
`ModelConfig` encapsulates all configuration parameters (model_name, learning_rate, epochs) with controlled access through properties.

### 4. Composition
The `Trainer` class uses composition to coordinate between `BaseModel` and `DataLoader`, promoting loose coupling and flexibility.

### 5. Class Variables
`BaseModel.model_count` is a class variable that tracks the total number of models created, demonstrating shared state across instances.

## API Reference

### framework.config.ModelConfig
Configuration class for model parameters.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| model_name | str | Required | Name of the model |
| learning_rate | float | 0.01 | Learning rate for training |
| epochs | int | 10 | Number of training epochs |

### framework.base_model.BaseModel
Abstract base class for all models.

**Methods:**
- `train(data)`: Train the model on the provided data (abstract)
- `evaluate(data)`: Evaluate the model on the provided data (abstract)

**Class Variables:**
- `model_count`: Total number of models created

### framework.models.LinearRegressionModel
Concrete implementation of a Linear Regression model.

### framework.models.NeuralNetworkModel
Concrete implementation of a Neural Network model with layers [64, 32, 1].

### framework.data_loader.DataLoader
Data loader class for managing datasets.

**Methods:**
- `get_data()`: Returns the loaded dataset

### framework.trainer.Trainer
Trainer class that coordinates model training and evaluation.

**Methods:**
- `run()`: Executes the training and evaluation pipeline

## Extending the Framework

To add a new model type, simply extend the `BaseModel` class:

```python
from framework.base_model import BaseModel
from framework.config import ModelConfig

class MyCustomModel(BaseModel):
    def __init__(self, config: ModelConfig):
        super().__init__(config)

    def train(self, data):
        # Implement custom training logic
        pass

    def evaluate(self, data):
        # Implement custom evaluation logic
        pass
```

 