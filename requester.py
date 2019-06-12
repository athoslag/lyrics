import json
import requests

def saveToFile(filename, items):
	try:
		with open(filename, 'w') as fd:
			for item in items:
				fd.write(item)
				fd.write('\n')

		print('Successfully written to %s' % filename)
	except:
		print('Error: could not write to %s' % filename)

def parseJSON(response):
	infos = []
	try:
		if len(response["mus"]) == 0:
			print('Radio has no musics.')
			return []

		for music in response["mus"]:
			artistName = music["art"]["name"]
			musicName = music["name"]
			infos.append(artistName + ' -> ' + musicName)

		return infos
	except:
		print('Error: could not convert to JSON.')

def main():
	apiKey = '7011800b8ae38866c80b2afcdf5660c7'
	url = 'https://api.vagalume.com.br/radio.php'
	payload = { 'type': 'mus', 'radio': 'coca-cola-fm', 'apikey': apiKey} 
	radio = payload['radio'] + '.txt'

	# Performs the request
	response = requests.get(url, params=payload)

	try:
		responseJSON = response.json()

		if responseJSON["status"] == 'error':
			print('Error: ' + responseJSON["message"])
			print()
			return
		else:
			# Parses info from JSON
			data = parseJSON(responseJSON)
			
			# Writes to file
			saveToFile(radio, data)
			print()
	except:
		print('Error: could not convert to JSON.')

if __name__ == '__main__':
    main()
