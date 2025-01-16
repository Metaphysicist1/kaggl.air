# KaggleAir

A lightweight Python utility for downloading and managing Kaggle datasets with ease.

## Features

- Download datasets from Kaggle using direct links
- Automatically unzip downloaded datasets
- Clean up zip files after extraction
- Configurable download and extraction paths

## Installation

Clone the repository:

git clone https://github.com/Metaphysicist1/kaggl.air.git
cd kaggle-air

## Usage

from kaggle_air import KaggleAir

# Initialize KaggleAir
downloader = KaggleAir("MyDownloader")

# Download a dataset
kaggle_link = "https://www.kaggle.com/api/v1/datasets/download/your-dataset-link"
downloader.download(kaggle_link, filename="dataset.zip")

# Unzip the dataset
downloader.unpack("~/Downloads/dataset.zip")

# Clean up the zip file
downloader.remove_zip("~/Downloads/dataset.zip")

### Custom Paths

You can specify custom download and extraction paths:

# Download to a specific location
downloader.download(kaggle_link, destination="/path/to/folder", filename="custom.zip")

# Extract to a specific location
downloader.unpack("~/Downloads/custom.zip", destination="/path/to/extract")

## API Reference

### `KaggleAir(name)`
Initialize a new KaggleAir instance.
- `name`: Identifier for the downloader instance

### `download(kaggle_link, destination=None, filename='dataset.zip')`
Download a dataset from Kaggle.
- `kaggle_link`: Direct download link from Kaggle
- `destination`: Optional download path (defaults to ~/Downloads)
- `filename`: Optional output filename (defaults to 'dataset.zip')

### `unpack(filepath, destination=None)`
Extract a downloaded zip file.
- `filepath`: Path to the zip file
- `destination`: Optional extraction path (defaults to ~/Downloads)

### `remove_zip(path)`
Remove a zip file.
- `path`: Path to the zip file to remove

## Requirements

- Python 3.6+
- Unix-like environment (uses `curl` and `unzip` commands)

## Limitations

- Currently supports Unix-like systems only
- Requires direct Kaggle download links
- No built-in Kaggle API authentication handling


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


