from vagalume import lyrics

class SongPair(object):
	"""A pair containing an Artist and a Song"""
	def __init__(self, artist, song):
		super(SongPair, self).__init__()
		self.artist = artist
		self.song = song

# API Functions

def printHeader(pair):
	print('---')	
	print(result.song.name)
	print(result.artist.name)
	print('---')
	print()
		

def printLyrics(result):
	print('---')
	print(result.song.lyric)
	print('---')
	print()

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
	result = lyrics.find(pair.artist, pair.song)
	if result.is_not_found():
		print('[%s] Song not found.' % pair.song)
	else:
		printHeader(result)
		printLyrics(result)