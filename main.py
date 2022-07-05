import gzip
import json
from typing import Optional, Dict, Any

import prior
from tqdm import tqdm


# import pickle

# from datasets import load_dataset

# dataset = load_dataset("allenai/houses", use_auth_token=True)

# houses = {
#     "train": [],
#     "validation": [],
#     "test": [],
# }
# for split in ["train", "validation", "test"]:
#     for house_entry in dataset[split]:
#         house = pickle.loads(house_entry["house"])
#         houses[split].append(house)

# houses["val"] = houses["validation"]
# del houses["validation"]


# with gzip.open("train.json.gz", "wb") as f:
#     f.write(json.dumps(houses["train"]).encode("utf-8"))

# with gzip.open("val.json.gz", "wb") as f:
#     f.write(json.dumps(houses["val"]).encode("utf-8"))

# with gzip.open("test.json.gz", "wb") as f:
#     f.write(json.dumps(houses["test"]).encode("utf-8"))


def load_dataset(config: Optional[Dict[str, Any]] = None) -> prior.DatasetDict:
    """Load the houses dataset."""

    if config is None:
        config = {}

    train_size = config.get("train_size", 10_000)
    val_size = config.get("val_size", 1_000)
    test_size = config.get("test_size", 1_000)

    assert 1 <= train_size <= int(1e4)
    assert 1 <= val_size <= int(1e3)
    assert 1 <= test_size <= int(1e3)

    data = {}
    for split, size in [("train", train_size), ("val", val_size), ("test", test_size)]:
        with gzip.open(f"{split}.jsonl.gz", "r") as f:
            houses = []
            for line in tqdm(f, total=size, desc=f"Loading {split}"):
                if len(houses) == size:
                    break
                houses.append(json.loads(line))

        data[split] = prior.Dataset(
            data=houses, dataset="procthor-dataset", split=split
        )
    return prior.DatasetDict(**data)
