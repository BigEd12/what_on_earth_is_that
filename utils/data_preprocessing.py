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

def plants_over_x_images(df):
    """
    Returns a dictionary containing percentages of image types.
    
    Arguments:
    
    df: DataFrame
        Must be the DF generated from plant_info_df()
        
    Returns:
    
    percent: float
        The percentage of plant types that have images count within this band
        
    count: int
        The number of plant types that have images count withing this band
    """
    band_dict = {}

    plant_image_count = df.groupby('plant_name')['count'].sum().reset_index()
    plant_image_count_sorted = plant_image_count.sort_values(by='count', ascending=False)

    total_plants = plant_image_count.shape[0]

    all_images_count = plant_image_count_sorted[plant_image_count_sorted['count'] == 400].shape[0]
    over_300_count = plant_image_count_sorted[(plant_image_count_sorted['count'] >= 300) & (plant_image_count_sorted['count'] < 400)].shape[0]
    over_200_count = plant_image_count_sorted[(plant_image_count_sorted['count'] >= 200) & (plant_image_count_sorted['count'] < 300)].shape[0]
    over_100_count = plant_image_count_sorted[(plant_image_count_sorted['count'] >= 100) & (plant_image_count_sorted['count'] < 200)].shape[0]
    under_100_count = plant_image_count_sorted[(plant_image_count_sorted['count'] >= 0) & (plant_image_count_sorted['count'] < 100)].shape[0]

    all_images_percent = round((all_images_count / total_plants) * 100, 2)
    over_300_percent = round((over_300_count / total_plants) * 100, 2)
    over_200_percent = round((over_200_count / total_plants) * 100, 2)
    over_100_percent = round((over_100_count / total_plants) * 100, 2)
    under_100_percent = round((under_100_count / total_plants) * 100, 2)

    band_dict['400'] = [all_images_percent, all_images_count]
    band_dict['300-399'] = [over_300_percent, over_300_count]
    band_dict['200-299'] = [over_200_percent, over_200_count]
    band_dict['100-199'] = [over_100_percent, over_100_count]
    band_dict['0-99'] = [under_100_percent, under_100_count]

    return band_dict