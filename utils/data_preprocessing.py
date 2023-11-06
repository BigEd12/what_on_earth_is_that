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

def plant_info_df(df):
    """
    Returns a Pandas Dataframe with three columns.
    
    Column names:
    
    plant_name: str
        Plant name in DF
    
    image_type: str
        The type of image (bark, flower, fruit, leaf)
        
    count: int64
        The number of images that plant has for that image type
    """
    grouped_df = df.groupby(['plant_name', 'image_type']).size().reset_index(name='count')
        
    return grouped_df

def image_type_range(df):
    """
    Returns a dictionary containing information on image types.
    
    Arguments:
    
    df: DataFrame
        Must be the DF generated from plant_info_df()
        
    Returns:
    
    min: int64
        The minimum number of images for the type
        
    max: int64
        The maxiimum number of images for the type
        
    mean: float64
        The mean number of images for the type
    """
    img_types = ['bark', 'fruit', 'flower', 'leaf']
    count_dict = {}

    for img in img_types:
        tmp = df[df.image_type ==  img]
        tmp_min = tmp['count'].min()
        tmp_max = tmp['count'].max()
        tmp_mean = round(tmp['count'].mean(),0)

        count_dict[img] = {'min': tmp_min,
                           'max': tmp_max,
                           'mean': tmp_mean
                          }
    
    return count_dict