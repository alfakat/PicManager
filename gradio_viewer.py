import os
import shutil
import gradio as gr
from gradio_viewer_config import GradioViewerConfig


def main():
    input = save_backup(GradioViewerConfig.folder_path)
    image_paths = [os.path.join(input, f) for f in os.listdir(input)]
    grid = create_image_grid(image_paths)
    grid.launch()


def save_backup(images_folder):
    shutil.copytree(images_folder, GradioViewerConfig.backup_folder_name, dirs_exist_ok=True)
    return os.path.join(os.path.abspath(os.getcwd()), GradioViewerConfig.backup_folder_name)


def move_images(selected_images, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    for image in selected_images:
        shutil.move(image, os.path.join(dest_folder, os.path.basename(image)))


def create_image_grid(images):
    def update_selected_images(selected_images, image_path, checked):
        if checked:
            selected_images.append(image_path)
        else:
            selected_images.remove(image_path)
        return selected_images

    def save_selected_images(selected_images):
        move_images(selected_images, GradioViewerConfig.dest_folder)
        return f"Moved {len(selected_images)} images to {GradioViewerConfig.dest_folder}"

    with gr.Blocks() as demo:
        selected_images = gr.State([])
        with gr.Row():
            for j in range(4):  # 4 columns
                with gr.Column():
                    for i in range(0, len(images), 5):  # 5 rows
                        image = images[i + j]
                        gr.Image(value=image, show_label=False, show_download_button=False)
                        checkbox = gr.Checkbox(label=os.path.basename(image), container=False)
                        checkbox.change(fn=update_selected_images, inputs=[selected_images, gr.State(image), checkbox], outputs=selected_images)

        with gr.Row():
            inv_btn = gr.Button("Move to invalid")
            clear_btn = gr.Button("Clear selections")  # to do

        inv_btn.click(fn=save_selected_images, inputs=[selected_images], outputs=[])

    return demo


if __name__ == "__main__":
    main()
