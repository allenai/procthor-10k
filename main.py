import gzip
import json

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


def load_dataset() -> prior.DatasetDict:
    """Load the houses dataset."""
    data = {}
    for split, size in [("train", 10_000), ("val", 1_000), ("test", 1_000)]:
        with gzip.open(f"{split}.jsonl.gz", "r") as f:
            houses = [
                json.loads(line)
                for line in tqdm(f, total=size, desc=f"Loading {split}")
            ]
        data[split] = prior.Dataset(
            data=houses, dataset="procthor-dataset", split=split
        )
    return prior.DatasetDict(**data)
