import os


def delete_files():
    directory = '/home/dhon_bobis/Downloads'
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an Excel file
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Remove the file
            os.remove(file_path)



# delete_files()