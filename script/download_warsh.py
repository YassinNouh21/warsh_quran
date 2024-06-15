import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the page containing SVGZ links
base_url = "https://maknoon.com/quran/warsh/"

# Create a directory to save downloaded SVGZs
os.makedirs("svgzs", exist_ok=True)

# Send a GET request to the page
response = requests.get(base_url)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all SVGZ links
svgz_links = soup.find_all('a', href=True)
svgz_urls = [urljoin(base_url, link['href']) for link in svgz_links if link['href'].endswith('.svgz')]

# Download each SVGZ
for svgz_url in svgz_urls:
    svgz_name = os.path.basename(svgz_url)
    svgz_path = os.path.join("svgzs", svgz_name)
    
    # Download the SVGZ file
    svgz_response = requests.get(svgz_url)
    svgz_response.raise_for_status()
    
    # Save the SVGZ file
    with open(svgz_path, 'wb') as svgz_file:
        svgz_file.write(svgz_response.content)
    
    print(f"Downloaded: {svgz_name}")

print("All SVGZ files have been downloaded.")