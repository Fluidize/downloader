import requests
from progress_bar import *

file_url = ""

#request data
r = requests.get(file_url, stream=True)
total_size_in_bytes= int(r.headers.get('content-length', 0))
block_size = 1024
file_name = file_url.split('/')[-1] #last url directory 








progress_bar = progress_bar_manual(total_size_in_bytes)
with open(file_name, "wb") as file:

	for chunk in r.iter_content(block_size):
		if chunk:
			file.write(chunk)
			progress_bar.update(len(chunk))
progress_bar.close()
			