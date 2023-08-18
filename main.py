import requests, sys, art
from progress_bar import *
from typingstyle import *

sys.stdout.write(art.text2art("Downloader"))
print(displaytext("1. Download from URL\n2. Settings\n3. EXIT", custom_border_length=65))




while True:
	option = input('')
	if option == '1':
		file_url = input('URL: ')

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
			