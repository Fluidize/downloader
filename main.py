import requests
from progress_bar import *

file_url = "https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/random.pdf"

r = requests.get(file_url, stream=True)

with open("file.pdf", "wb") as downloading_file:
    total_size_in_bytes= int(r.headers.get('content-length', 0))
    print(total_size_in_bytes)
	# for chunk in r.iter_content(chunk_size = 1024):
	# 	if chunk:
	# 		downloading_file.write(chunk)