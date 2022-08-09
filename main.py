import gzip

from tqdm import tqdm

try:
    from prior import LazyJsonDataset, DatasetDict
except:
    raise ImportError("Please update the prior package (pip install --upgrade prior).")


def load_dataset(train_size=10_000, val_size=1_000, test_size=1_000) -> LazyJsonDataset:
    """Load the houses dataset."""

    data = {}
    for split, size in [("train", train_size), ("val", val_size), ("test", test_size)]:
        with gzip.open(f"{split}.jsonl.gz", "r") as f:
            houses = [line for line in tqdm(f, total=size, desc=f"Loading {split}")]

        if len(houses) != size:
            raise ValueError(
                f"Number of loaded houses for split {split} did not equal"
                f" the requested number ({len(houses)} != {size})."
            )

        data[split] = LazyJsonDataset(
            data=houses, dataset="procthor-dataset", split=split
        )
    return DatasetDict(**data)
