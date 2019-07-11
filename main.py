from vagalume import lyrics
import colorama
from colorama import Fore, Style
import string
import sys

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
	fileName = sys.argv[1]
	found = 0

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
		try:
			result = lyrics.find(pair.artist, pair.song)
		except Exception as err:
			print(Fore.RED + '\t Error: ' + str(err))
		
		if result.is_not_found():
			print(Fore.RED + '\t [%s] Song not found.' % pair.song)
		else:
			output = open("%s/songs/%d.%s.txt" % (fileName, count + 1, pair.song), "w+")
			processedLyric = removePunctuation(result.song.lyric.split())
			
			output.write(str(processedLyric))
			output.write("\n")
			output.close
			print(Fore.GREEN + '\t [%s] Done.' % pair.song)
			found += 1

	percentage = 0 if len(pairs) is 0 else found/len(pairs)
	print(Style.RESET_ALL + '\t Found %d out of %d ' % (found, len(pairs)) + (Fore.GREEN if percentage == 1 else (Fore.RED if percentage == 0 else Fore.YELLOW)) + "({0:.0%})".format(percentage))
	print(Style.RESET_ALL)

if __name__ == '__main__':
	main()
