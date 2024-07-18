import requests
import os

# Directory where the downloaded files will be saved
save_dir = 'downloaded_datasets'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Read the URLs from the text file
with open('URLs.txt', 'r') as file:
    urls = file.readlines()

# Download each file
for url in urls:
    url = url.strip()
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = url.split('/')[-1]  # Extracts filename from URL
        filepath = os.path.join(save_dir, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f'Downloaded {filename}')
    else:
        print(f'Failed to download {url}')

print('All files have been downloaded.')
