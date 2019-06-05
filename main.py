from vagalume import lyrics

class SongPair(object):
	"""A pair containing an Artist and a Song"""
	def __init__(self, artist, song):
		super(SongPair, self).__init__()
		self.artist = artist
		self.song = song
		

def printResult(pair):
	result = lyrics.find(pair.artist, pair.song)
	if result.is_not_found():
		print('Song not found')
	else:
		print(result.song.name)
		print(result.artist.name)
		print()
		print(result.song.lyric)
		print()

def printTranslation(pair):
	result = lyrics.find(pair.artist, pair.song)
	translation = result.get_translation_to('pt-br')
	if not translation:
		print('Translation not found')
	else:
		print(translation.name)
		print(translation.lyric)

# MAIN
pairs = []

while True:
	try:
		artist = input()
		if not artist: 
			break

		song = input()
		if not song:
			break
		else:
			pairs.append(SongPair(artist, song))
	except:
		break

for pair in pairs:
	printResult(pair)
