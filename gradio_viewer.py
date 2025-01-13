import os
import csv
import gradio as gr
from typing import List

from gradio import State


class GradioViewer():

    def __init__(self, batch_list: list):
        self.batch_list = batch_list

        tabs = []
        for csv_name in self.batch_list:
            tabs.append(self.create_tab(csv_name))
            print(f'Creating tab for {csv_name}')

        basename_list = [os.path.basename(csv_name) for csv_name in self.batch_list]
        demo = gr.TabbedInterface(tabs, basename_list)

        demo.launch()

    def read_csv(self, images_csv: str) -> List:
        """Read image paths from the CSV file"""
        with open(images_csv, mode="r") as file:
            reader = csv.DictReader(file)
            return [row["image_path"] for row in reader]

    def toggle_image_selection(self, selected_images, image_path, checked):
        if checked:
            selected_images.append(image_path)
        else:
            selected_images.remove(image_path)
        return selected_images

    def process_selected_images(self, selected_images, label: str, csv_id: str) -> State:
        sorted_folder = os.path.join(os.path.dirname(__file__), 'sorted_images')
        os.makedirs(sorted_folder, exist_ok=True)
        sorted_csv = os.path.join(sorted_folder, rf'{label}_{csv_id}.csv')

        with open(sorted_csv, mode="a", newline="") as file:
            writer = csv.writer(file)
            if os.path.getsize(sorted_csv) == 0:
                writer.writerow(["image_path"])
            for image in selected_images:
                writer.writerow([image])

        return gr.State([])

    def create_tab(self, csv_name):
        with gr.Blocks() as tab:
            selected_images = gr.State([])
            checkboxes = []

            images_path = self.read_csv(images_csv=csv_name)

            with gr.Row():
                for image in images_path:
                    with gr.Column():
                        gr.Image(value=image, label=os.path.basename(image))
                        checkbox = gr.Checkbox(label="Select", value=False)
                        checkboxes.append(checkbox)

                        checkbox.change(
                            fn=self.toggle_image_selection,
                            inputs=[selected_images, gr.State(image), checkbox],
                            outputs=[selected_images])

            with gr.Row():
                label = gr.Textbox(label="Label")
                submit_btn = gr.Button("Submit")

            csv_id = gr.State(str(int(csv_name.split('_')[-1].split('.')[0])))

            submit_btn.click(
                fn=self.process_selected_images,
                inputs=[selected_images, label, csv_id],
                outputs=[])

        return tab


