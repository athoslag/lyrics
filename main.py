from vagalume import lyrics
import string

class SongPair(object):
	"""A pair containing an Artist and a Song"""
	def __init__(self, artist, song):
		super(SongPair, self).__init__()
		self.artist = artist
		self.song = song

def removePunctuation(strList):
	translator = str.maketrans('', '', string.punctuation)
	newList = []

	for item in strList:
		newList.append(item.translate(translator))

	return newList

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
			print('\t [%s] Song not found.' % pair.song)
		else:
			output = open("songs/%d.%s.txt" % (count + 1, pair.song), "w+")
			processedLyric = removePunctuation(result.song.lyric.split())
			
			output.write(str(processedLyric))
			output.write("\n")
			output.close
			print('\t [%s] Done.' % pair.song)

if __name__ == '__main__':
	main()
