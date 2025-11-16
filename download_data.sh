#!/bin/bash

# Script to download all MultiTab datasets using download_data.py

# Set your data root directory here
DATA_ROOT="/path/to/data/"

# Create data root if it doesn't exist
mkdir -p "$DATA_ROOT"

echo "Downloading MultiTab datasets to: $DATA_ROOT"
echo "=========================================="

# Download higgs
echo ""
echo "Downloading higgs..."
python3 download_data.py --dataset_name higgs --dest_dir "$DATA_ROOT/higgs"
[ $? -eq 0 ] && echo "✓ higgs download complete" || exit 1

# Download aliexpress
echo ""
echo "Downloading aliexpress..."
python3 download_data.py --dataset_name aliexpress --dest_dir "$DATA_ROOT/AliExpress_NL"
[ $? -eq 0 ] && echo "✓ aliexpress download complete" || exit 1

# Download acs_income
echo ""
echo "Downloading acs_income..."
python3 download_data.py --dataset_name acs_income --dest_dir "$DATA_ROOT/acs_income"
[ $? -eq 0 ] && echo "✓ acs_income download complete" || exit 1

echo ""
echo "=========================================="
echo "All datasets downloaded successfully!"
echo "Data root: $DATA_ROOT"
