import torch
import torch.nn as nn


class Swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)


class ShallowCNN(nn.Module):
    def __init__(self, hidden_features=32, num_classes=42, **kwargs):
        super().__init__()
        c_hid1 = hidden_features
        c_hid2 = hidden_features * 2
        c_hid3 = hidden_features * 4

        self.cnn_layers = nn.Sequential(
            nn.Conv2d(1, c_hid1, kernel_size=5, stride=2, padding=4),
            Swish(),
            nn.Conv2d(c_hid1, c_hid2, kernel_size=3, stride=2, padding=1),
            Swish(),
            nn.Conv2d(c_hid2, c_hid3, kernel_size=3, stride=2, padding=1),
            Swish(),
            nn.Conv2d(c_hid3, c_hid3, kernel_size=3, stride=2, padding=1),
            Swish(),
            nn.Conv2d(c_hid3, c_hid3, kernel_size=3, stride=2, padding=1),
            Swish(),
        )
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(c_hid3, num_classes)
        )

    def get_logits(self, x):
        # TODO (3.2): Implement classification procedure that outputs the logits across the classes
        x = self.cnn_layers(x)
        x = nn.AdaptiveAvgPool2d((1, 1))(x)
        x = self.fc_layers(x)
        return x

    def forward(self, x, y=None) -> torch.Tensor:
        # TODO (3.2): Implement forward function for (1) EBM, (2) Unconditional JEM, (3) Conditional JEM.
        #  Consider using F.adaptive_avg_pool2d to convert between the 2D features and a linear representation.
        #  (You can also reuse your implementation of 'self.get_logits(x)' if this helps you.)
        if y is None:
            # EBM or unconditional JEM: LOG-SUM-EXP
            return torch.logsumexp(self.get_logits(x), dim=1)
        else:
            # Conditional JEM
            y_logits = torch.gather(self.get_logits(x), 1, y.unsqueeze(1))
            return torch.exp(y_logits)