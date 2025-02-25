import os
import glob


if __name__ == "__main__":
    folders = ["external_traffic", "new_product_launcher", "sponsored_affiliate", "sponsored_media", "sponsored_solutions"]
    
    for folder in folders:
        # folder_path = f'downloads/{folder}/'
        path_dir = f'downloads/{folder}/*'
        # os.chdir(folder_path)
        files = glob.glob(path_dir)
        for f in files:
            # print(f)
            os.remove(f)

    