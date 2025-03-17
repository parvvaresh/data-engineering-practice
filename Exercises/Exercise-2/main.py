import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_file(target_date = "2024-01-19 10:27"):
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

    response = requests.get(url)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, "html.parser")

    

    # Find all table rows
    rows = soup.find_all("tr")

    file_name = None  

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            if target_date in cells[1].get_text(strip=True):
                link_tag = cells[0].find("a")
                if link_tag and link_tag.get("href"):
                    file_name = link_tag.get("href")
                    break


    if file_name:
        print("Found file:", file_name)
        # Construct the full URL to download the file
        download_url = url + file_name
        print("Download URL:", download_url)
        
        # If you want to actually download the file:
        file_content = requests.get(download_url).content
        with open(file_name, "wb") as f:
            f.write(file_content)
        
        print(f"File '{file_name}' has been downloaded successfully.")
    else:
        print("No file found for the specified date.")
    
    return file_name


def main():
    file_name = get_file()
    df = pd.read_csv(file_name)
    print(df[df["HourlyDryBulbTemperature"] == df["HourlyDryBulbTemperature"].max()])

if __name__ == "__main__":
    main()
