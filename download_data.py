import os
import shutil
import argparse
from typing import Literal
from huggingface_hub import hf_hub_download

REPO_ID = "Dimitri-Sinodinos/multitab"
REPO_TYPE = "dataset"

# Map logical dataset name -> filename on the Hub
REMOTE_FILE_MAP = {
    "higgs": "higgs.h5",
    "aliexpress": "aliexpress.h5",
    "acs_income": "acs_incom.h5",
}


def download_multitab_dataset(
    dataset_name: Literal["higgs", "aliexpress", "acs_income"],
    dest_dir: str,
) -> str:
    """
    Download a MultiTab HDF5 file from the Hub and save it to dest_dir/train_val_test.h5.

    Args:
        dataset_name: One of 'higgs', 'aliexpress', 'acs_income'.
        dest_dir: Destination directory where the H5 file will be saved.

    Returns:
        Full path to the local H5 file.
    """
    if dataset_name not in REMOTE_FILE_MAP:
        raise ValueError(
            f"Unknown dataset_name '{dataset_name}'. "
            f"Expected one of {list(REMOTE_FILE_MAP.keys())}"
        )

    remote_filename = REMOTE_FILE_MAP[dataset_name]

    # 1) Download into HF cache; this returns the cached file path
    cached_path = hf_hub_download(
        repo_id=REPO_ID,
        filename=remote_filename,
        repo_type=REPO_TYPE,
    )

    # 2) Copy/rename into your desired directory
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, "train_val_test.h5")
    shutil.copy2(cached_path, dest_path)

    return dest_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download MultiTab datasets from Hugging Face Hub"
    )
    parser.add_argument(
        "--dataset_name",
        required=True,
        choices=["higgs", "aliexpress", "acs_income"],
        help="Name of the dataset to download",
    )
    parser.add_argument(
        "--dest_dir",
        required=True,
        help="Destination directory where the H5 file will be saved",
    )

    args = parser.parse_args()

    dest_path = download_multitab_dataset(
        dataset_name=args.dataset_name,
        dest_dir=args.dest_dir,
    )

    print(f"✓ Successfully downloaded to: {dest_path}")

