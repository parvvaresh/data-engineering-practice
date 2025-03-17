import requests
import os
import zipfile
import glob


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_file(url, path, name):
    response = requests.get(url, stream=True)


    if response.status_code == 200:
        with open(path + name, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"File downloaded successfully: {name}")



def unzip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Files extracted to: {extract_to}")



def main():

    folder_name = "downloads"


    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"The folder '{folder_name}' was created successfully.")
    else:
        print(f"The folder '{folder_name}' already exists.")


    for url in download_uris:
        name = url.split("/")[-1].split(".")[0]
        download_file(url, "downloads/", name)
        unzip(f"downloads/{name}", "downloads")
        os.remove(f"downloads/{name}")



        
    

if __name__ == "__main__":
    main()
