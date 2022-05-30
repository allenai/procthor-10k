import gzip
import json

import prior

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
    with gzip.open("train.json.gz", "rb") as f:
        train_houses = json.loads(f.read().decode("utf-8"))
    with gzip.open("val.json.gz", "rb") as f:
        val_houses = json.loads(f.read().decode("utf-8"))
    with gzip.open("test.json.gz", "rb") as f:
        test_houses = json.loads(f.read().decode("utf-8"))
    return prior.DatasetDict(
        train=prior.Dataset(
            data=train_houses, dataset="procthor-dataset", split="train"
        ),
        val=prior.Dataset(data=val_houses, dataset="procthor-dataset", split="val"),
        test=prior.Dataset(data=test_houses, dataset="procthor-dataset", split="test"),
    )
