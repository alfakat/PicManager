import os
import argparse
import datetime
import threading
from csv_creator import CSVCreator
from gradio_ui import GradioViewer
from multiprocessing import Pool


def argument_parsing() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--images_folder", '--images', type=str, required=True,
                        help="Path to folder with images")
    parser.add_argument("--output", type=str, required=False,
                        help="Path where to save the csv",
                        default=os.path.join(os.path.dirname(os.path.realpath(__file__)), f'{str(datetime.date.today())}_output'))

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # ## parse arguments
    args = argument_parsing()

    create_initial_images_csv = CSVCreator(images_folder = args.images_folder,
                                           output_folder = args.output)

    for batch in os.listdir(create_initial_images_csv.result):
        batch_path = os.path.join(create_initial_images_csv._batch_dir, batch)
        GradioViewer(images_csv=batch_path, id=batch[:-4][12:], output=args.output)


