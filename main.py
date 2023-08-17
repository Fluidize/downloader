import requests
from progress_bar import *

file_url = "https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/random.pdf"

#request data
r = requests.get(file_url, stream=True)
total_size_in_bytes= int(r.headers.get('content-length', 0))
block_size = 1024
progress_bar = progress_bar_manual(total_size_in_bytes)



with open("file.pdf", "wb") as file:

	for chunk in r.iter_content(block_size):
		if chunk:
			file.write(chunk)
			progress_bar.update(len(chunk))

progress_bar.close()
			