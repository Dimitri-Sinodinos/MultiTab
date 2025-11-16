# Manual Dataset Setup Instructions

If you prefer to download the datasets from their original sources and perform the preprocessing yourself, follow these instructions.

## Setting Up Higgs and ACS Income Datasets (OpenML)

For both Higgs and ACS Income datasets, use the provided preprocessing notebook to automatically download, preprocess, and format the data:

### Steps

1. **Open the preprocessing notebook:**
   ```
   preprocess_dataset.ipynb
   ```

2. **Configure the dataset (Step 0: Configuration):**
   - For **Higgs dataset**: Uncomment the Higgs `CONFIG` block
   - For **ACS Income dataset**: Uncomment the ACS Income `CONFIG` block
   - Comment out the configuration you're not using

3. **Set the output directory:**
   - Update the `output_dir` in the `CONFIG` to match the `data_root` used in `main.py`
   - This ensures the processed datasets are saved where the training script expects to find them

4. **Configure target variables (Step 3: Configure Target Variables):**
   - For **Higgs dataset**: Uncomment the Higgs `TARGET_CONFIG` block
   - For **ACS Income dataset**: Uncomment the ACS Income `TARGET_CONFIG` block
   - Comment out the target configuration you're not using

5. **Run all cells in the notebook:**
   - The notebook will automatically download the dataset from OpenML
   - Preprocess and format the data
   - Save it in H5 format compatible with the training pipeline
   - Validate the processed dataset

## Setting Up AliExpress Dataset

For the AliExpress dataset, follow these manual steps:

### Steps

1. **Download the dataset:**
   - Download the dataset from [this Google Drive link](https://drive.google.com/drive/folders/1F0TqvMJvv-2pIeOKUw9deEtUxyYqXK6Y?usp=sharing)
   - Save `AliExpress_NL.zip` to your `data_root` directory

2. **Extract the files:**
   ```bash
   cd <your_data_root>
   unzip AliExpress_NL.zip
   ```
   This should create an `AliExpress_NL` folder with `train.csv` and `test.csv` files.

3. **Preprocess the dataset:**
   - Open `preprocess_aliexpress.ipynb`
   - Update the `data_root` variable in the first cell to point to your data directory
   - Run all cells in the notebook to create the H5 dataset

## Notes

- The manual preprocessing approach gives you full control over the data processing pipeline
- You can customize preprocessing steps in the notebooks if needed
- The output format (H5) will be identical to the preprocessed files available for quick setup
- Ensure your `data_root` directory structure matches the expected format:
  ```
  data_root/
  ├── higgs/
  │   └── train_val_test.h5
  ├── acs_income/
  │   └── train_val_test.h5
  └── AliExpress_NL/
      └── train_val_test.h5
  ```
