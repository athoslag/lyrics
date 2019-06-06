from vagalume import lyrics

class SongPair(object):
	"""A pair containing an Artist and a Song"""
	def __init__(self, artist, song):
		super(SongPair, self).__init__()
		self.artist = artist
		self.song = song

def main():
	pairs = []

	while True:
		try:
			artist, song = input().split(' -> ')
			if not artist or not song: 
				break
			else:
				pairs.append(SongPair(artist, song))
		except:
			break

	for count,pair in enumerate(pairs):
		result = lyrics.find(pair.artist, pair.song)
		if result.is_not_found():
			print('[%s] Song not found.' % pair.song)
		else:
			output = open("songs/%d.%s.txt" % (count + 1, pair.song), "w+")
			output.write(result.song.lyric)
			output.write("\n")
			output.close

if __name__ == '__main__':
    main()
