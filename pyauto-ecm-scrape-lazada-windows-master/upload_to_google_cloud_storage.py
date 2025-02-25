from google.cloud import storage
import os


def upload_folder_to_gcs(local_folder_path, bucket_name, destination_folder):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for root, dirs, files in os.walk(local_folder_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            blob_name = os.path.relpath(local_file_path, local_folder_path)
            blob_name = os.path.join(destination_folder, blob_name).replace(os.sep, '/')

            blob = bucket.blob(blob_name)
            blob.upload_from_filename(local_file_path)

            print(f'Uploaded {local_file_path} to gs://{bucket_name}/{blob_name}')

if __name__ == "__main__":
    local_folder_path = "downloads"
    bucket_name = "fgi-ecm-web-scraping"
    destination_folder = "LAZ"

    upload_folder_to_gcs(local_folder_path, bucket_name, destination_folder)

