from utils.sourcing import extract_plant_data
from utils.page_dict import plant_dict



#extract_plant_data(plant_dict["Astragaluses"], "Astragaluses")
for item, value in plant_dict.items():
    if item == 'Yarrows':
        print(f"Currently extracting {item}")
        extract_plant_data(value, item)