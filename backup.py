import schedule
import time
import shutil
import datetime
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create the PyDrive client
def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("/home/krishna/Desktop/LinkedInScraping/client_secrets.json")
    gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
    return GoogleDrive(gauth)

def upload_to_drive(file_path, drive_folder_id, drive):
    try:
        file_drive = drive.CreateFile({'parents': [{'id': drive_folder_id}]})
        file_drive.SetContentFile(file_path)
        file_drive.Upload()
        print(f"File uploaded: {file_path}")
    except Exception as e:
        print(f"An error occurred while uploading the file: {e}")

def download_and_save(drive):
    source_file_path = '/home/krishna/Desktop/LinkedInScraping/continuous_data_scrape.csv'  # Replace with your CSV file path
    backup_file_path = f'backup_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    try:
        # Copy the file to a new location
        shutil.copy2(source_file_path, backup_file_path)
        print(f"File copied: {backup_file_path}")

        # Upload the backup to Google Drive
        drive_folder_id = '1gnNthit2RahIOswp-9l1GGSUbAVYg5cd'  # Replace with your Google Drive folder ID
        upload_to_drive(backup_file_path, drive_folder_id, drive)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    drive = authenticate_google_drive()
    download_and_save(drive)

if __name__ == "__main__":
    main()