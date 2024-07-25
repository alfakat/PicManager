import os


class GradioViewerConfig(str):
    """
    inputs for gradio_viewer
    """
    current_dir = os.getcwd()

    """absolute path to folder with images"""
    folder_path = r'C:\workspace\20201125-165445-85AE13F9'

    """validation of images not done on original folder, but on its replica"""
    backup_folder_name = os.path.join(current_dir, 'backup')

    """folder to where move frames, not stand in conditions"""
    dest_folder = os.path.join(current_dir, 'not_valid_frames')

