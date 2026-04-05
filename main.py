"""Main entry point for the Mini AI Model Trainer Framework"""

from framework.config import ModelConfig
from framework.models import LinearRegressionModel, NeuralNetworkModel
from framework.data_loader import DataLoader
from framework.trainer import Trainer


def main():
    # Create two ModelConfig objects
    config_lr = ModelConfig("LinearRegression", learning_rate=0.01, epochs=10)
    config_nn = ModelConfig("NeuralNetwork", learning_rate=0.001, epochs=20)

    # Print configs
    print(config_lr)
    print(config_nn)

    # Create both models
    lr_model = LinearRegressionModel(config_lr)
    nn_model = NeuralNetworkModel(config_nn)

    # Print model count
    print(f"Models created: {lr_model.model_count}")

    # Create DataLoader with dummy data
    data_loader = DataLoader([1, 2, 3, 4, 5])

    # Train both models through Trainer
    print("--- Training LinearRegression ---")
    trainer_lr = Trainer(lr_model, data_loader)
    trainer_lr.run()

    print("--- Training NeuralNetwork ---")
    trainer_nn = Trainer(nn_model, data_loader)
    trainer_nn.run()


if __name__ == "__main__":
    main()