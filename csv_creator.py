import os
import csv
import datetime
import pandas as pd


class CSVCreator():
    """The purpose of the class, create initial csv with paths to images"""

    def __init__(self, images_folder: str, output_folder: str):

        self.images_folder = images_folder
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        images_csv = self.images_folder_to_csv(images_folder=self.images_folder)
        num_of_images = self.folder_size(images_folder=self.images_folder)
        if num_of_images >= 50:
            self._batch_dir = self.images_folder_to_batch_csv(images_csv=images_csv)

    def folder_size(self, images_folder: str) -> int:
        """count only images in folder"""
        count = 0
        for image_path in os.listdir(images_folder):
            if image_path.endswith(('.png', '.jpg', 'jpeg')):
                count += 1
        return count

    def images_folder_to_csv(self, images_folder: str) -> str:
        """list and save absolute pathes to images, such as backup"""

        csv_file = os.path.join(self.output_folder, 'images_path.csv')
        with open(csv_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["image_path"])
            for image in os.listdir(images_folder):
                writer.writerow([os.path.join(images_folder, image)])

        return csv_file

    def images_folder_to_batch_csv(self, images_csv: str) -> str:
        """large csv devided into smaller for further easier work with images"""

        batch_dir = os.path.join(self.output_folder, f'csv_batch')
        os.makedirs(batch_dir, exist_ok=True)
        df = pd.read_csv(images_csv)

        # Divide into smaller csv of 50 rows
        chunk_size = 50
        for i in range(0, len(df), chunk_size):
            chunk = df.iloc[i:i + chunk_size]
            batch_csv = f"{batch_dir}/images_path_{i // chunk_size + 1}.csv"
            chunk.to_csv(batch_csv, index=False)

        return batch_dir

    @property
    def result(self):
        return self._batch_dir


class FilteredCSV():
    def __init__(self):
        return


class UpdateOrgCSV():
    def __init__(self):
        return
    #
    # # Update the original CSV to remove invalid paths
    # with open(csv_file, mode="r") as file:
    #     rows = list(csv.reader(file))
    #
    # with open(csv_file, mode="w", newline="") as file:
    #     writer = csv.writer(file)
    #     for row in rows:
    #         if row[0] not in selected_images:
    #             writer.writerow(row)