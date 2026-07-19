from PIL import Image
from torch.utils.data import Dataset


class DeepfakeDataset(Dataset):

    def __init__(self, image_paths, labels, rgb_transform=None, frequency_transform=None):

        self.image_paths = image_paths
        self.labels = labels
        self.rgb_transform = rgb_transform
        self.frequency_transform = frequency_transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):

        image = Image.open(self.image_paths[idx]).convert("RGB")

        rgb = image.copy()
        freq = image.copy()

        if self.rgb_transform:
            rgb = self.rgb_transform(rgb)

        if self.frequency_transform:
            freq = self.frequency_transform(freq)

        label = self.labels[idx]

        return rgb, freq, label