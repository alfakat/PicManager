# PicManager
Simple tool to review images batches 

# Short about the project
As data lover, I am very much often need to review sets of images for different purposes: categorize, clean, validate. 
Especially it became relevant with generated data, while not accurate prompt or lack of negative might bring 
unexpected set. Manager runs on amazing Gradio interface which easy to use and share. 

# Auditory
Believe that every data busy person might find this repo useful.

# How to Use the Project
1. Clone the project
2. Install missed packages
3. Run run_picmanager.py --images_folder <absolute_path_to_folder_with_images>

PicManager analyses the input folder, list absolute pathes to images in csv backup files and split the smaller batches, 50* images each as preset for tabs. 
Then opens Gradio viewer with tab per batch, images and checkboxes. Once select images, enter the label in field and click 'Submit'. 
Csv file named as label with absolute pathes to selected files will be created in sorted_images folder (with --output and save in another location). 
Recommended refresh Gradio to reset ticked checkboxes. 

*I found this number comfortable for review on one page, you may change it in cvs_creator.py

# Author’s info
Please PM/mail me if you have comments or suggestions.
