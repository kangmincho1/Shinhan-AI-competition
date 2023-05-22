import torch
import torch.nn as nn

class LinearModel(nn.Module):
    def __init__(self, input_dim, seq_len, output_dim):
        super(LinearModel, self).__init__()
        self.fc = nn.Linear(input_dim * seq_len, output_dim)

    def forward(self, x):
        batch_size = x.size(0)
        x = x.reshape(batch_size, -1)  # flatten the input
        out = self.fc(x)
        return out