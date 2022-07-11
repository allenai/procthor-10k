import gzip
import json
from typing import Any

import prior
from attr import field
from attrs import define
from tqdm import tqdm


@define
class LazyDataset(prior.Dataset):
    """Lazily load the json house data."""

    cached_data: dict = field(init=False)

    def __attrs_post_init__(self):
        self.cached_data = {}

    def __getitem__(self, index: int) -> Any:
        """Return the item at the given index."""
        if index not in self.cached_data:
            self.cached_data[index] = json.loads(self.data[index])
        return self.cached_data[index]

    def __len__(self) -> int:
        """Return the number of items in the dataset."""
        return super().__len__()

    def __repr__(self):
        """Return a string representation of the dataset."""
        return super().__repr__()

    def __str__(self):
        """Return a string representation of the dataset."""
        return super().__str__()


def load_dataset() -> prior.DatasetDict:
    """Load the houses dataset."""
    data = {}
    for split, size in [("train", 10_000), ("val", 1_000), ("test", 1_000)]:
        with gzip.open(f"{split}.jsonl.gz", "r") as f:
            houses = [line for line in tqdm(f, total=size, desc=f"Loading {split}")]
        data[split] = LazyDataset(data=houses, dataset="procthor-dataset", split=split)
    return prior.DatasetDict(**data)
