import pandas as pd
import os

def df_from_folders():
    """
    Return a Pandas DataFrame with basic columns.
    
    Column names:
    
    plant_name: str
        Plant name in DF
    
    image_type: str
        The type of image (bark, flower, fruit, leaf)
        
    image: str
        The path to the image
    """
    
    plant_names = []
    image_types = []
    images = []


    desired_folders = ['bark', 'flower', 'fruit', 'leaf']

    cwd = os.getcwd()

    for subdir in desired_folders:
        subdir_path = os.path.join(cwd, subdir)

        if os.path.exists(subdir_path):

            for plant_folder in os.listdir(subdir_path):
                plant_folder_path = os.path.join(subdir_path, plant_folder)

                if os.path.isdir(plant_folder_path):

                    for image_file in os.listdir(plant_folder_path):
                        image_file_path = os.path.join(plant_folder_path, image_file)

                        plant_names.append(plant_folder)
                        image_types.append(subdir)
                        images.append(image_file_path)

    data = {'plant_name': plant_names, 'image_type': image_types, 'image': images}
    df = pd.DataFrame(data)
    return df