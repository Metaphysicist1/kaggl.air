import os
from pathlib import Path


class Kaggle_air:
    def __init__(self, name):
        self.name = name
        self.default_destination = str(Path('~/Downloads').expanduser())

    def download(self, kaggle_link: str, destination: str = None, filename: str = 'dataset.zip') -> None:
        """
        Downloads a file from Kaggle using curl command.
        
        Args:
            kaggle_link (str): The Kaggle dataset download link
            destination (str, optional): Download destination path. Defaults to ~/Downloads/
            filename (str, optional): Output filename. Defaults to 'dataset.zip'
        """
        destination = destination or self.default_destination
        dest_path = str(Path(destination).expanduser())
        command = f'curl -L -o {dest_path}/{filename} {kaggle_link}'
        print(f"Downloading to: {command}")
        os.system(command)

    def unpack(self, filepath: str, destination: str = None) -> None:
        """
        Unzips a file to the specified destination.
        
        Args:
            filepath (str): Path to the zip file
            destination (str, optional): Extraction destination path. Defaults to ~/Downloads/
        """
        destination = destination or self.default_destination
        filepath = str(Path(filepath).expanduser())
        dest_path = str(Path(destination).expanduser())
        command = f'unzip {filepath} -d {dest_path}'
        print(f"Extracting: {command}")
        os.system(command)

    def remove_zip(self, path: str) -> None:
        """
        Removes a zip file.
        
        Args:
            path (str): Path to the zip file to remove
        """
        path = str(Path(path).expanduser())
        command = f'rm {path}'
        print(f"Removing: {command}")
        os.system(command)

# Example usage (should be in a separate file)
if __name__ == "__main__":
    downloader = Kaggle_air("KaggleDownloader")
    link = "https://www.kaggle.com/api/v1/datasets/download/arpitsinghaiml/most-visited-country-dataset"
    downloader.download(link)
    downloader.unpack("~/Downloads/dataset.zip")
    downloader.remove_zip("~/Downloads/dataset.zip")