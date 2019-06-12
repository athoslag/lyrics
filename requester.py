import json
import requests

apiKey = '7011800b8ae38866c80b2afcdf5660c7'
url = 'https://api.vagalume.com.br/radio.php'
payload = { 'type': 'mus', 'radio': 'coca-cola-fm', 'apikey': apiKey} 
radio = payload['radio'] + '.json'

# Performs the request
response = requests.get(url, params=payload)
print(response)

try:
	# Writes to file
	with open(radio, 'wb') as fd:
		for chunk in response.iter_content(chunk_size=128):
			fd.write(chunk)
		
	with open(radio, 'a') as fd:
		fd.write('\n')

	print('Successfully written to %s' % radio)
	print()
except:
	print('JSON operation was ill-fated.')
	print()
