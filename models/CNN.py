import torch
import torch.nn as nn

class CNNModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, kernel_size=3):
        super(CNNModel, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv1d(input_dim, hidden_dim, kernel_size),
            nn.ReLU(),
            nn.Conv1d(hidden_dim, hidden_dim, kernel_size),
            nn.ReLU(),
        )
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.output_dim = output_dim

    def forward(self, x):
        x = x.permute(0, 2, 1)
        x = self.cnn(x)
        x = x.mean(2)
        x = self.fc(x)
        return x.view(-1, self.output_dim)