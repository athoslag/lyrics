from vagalume import lyrics
import colorama
from colorama import Fore, Style
import string
import sys
import time

fileName = sys.argv[1]

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
		newList.append(item.translate(translator).lower())

	return newList

def saveFile(count, pair, lyr):
	output = open("%s/lyrics/%d.%s.txt" % (fileName, count + 1, pair.song), "w+")
	output.write(str(lyr))
	output.write("\n")
	output.close

def main():
	pairs = []
	found = 0

	rejected = []

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
			rejected.append((count, pair))
			print(Fore.RED + '\t [%s] - Error: ' % pair.song + str(err))
			print(Fore.YELLOW + '\n\t Waiting for 30 seconds...')
			time.sleep(30)
			continue
		
		if result.is_not_found():
			print(Fore.RED + '\t %d. [%s] Song not found.' % (count + 1, pair.song))
		else:
			output = open("%s/songs/%d.%s.txt" % (fileName, count + 1, pair.song), "w+")
			lyric = result.song.lyric
			saveFile(count, pair, lyric)
			processedLyric = removePunctuation(lyric.split())
			
			output.write(str(processedLyric))
			output.write("\n")
			output.close
			print(Fore.GREEN + '\t %d. [%s] Done.' % (count + 1, pair.song))
			found += 1

	if len(rejected) > 0:
		print(Fore.YELLOW + '\n\t Retrying %d rejected requests...' % len(rejected))
		for count,pair in rejected:
			try:
				result = lyrics.find(pair.artist, pair.song)
			except Exception as err:
				print(Fore.RED + '\t Error: ' + str(err))
				continue

			if result.is_not_found():
				print(Fore.RED + '\t %d. [%s] Song not found.' % (count + 1, pair.song))
			else:
				output = open("%s/songs/%d.%s.txt" % (fileName, count + 1, pair.song), "w+")
				lyric = result.song.lyric
				saveFile(count + 1, pair, lyric)
				processedLyric = removePunctuation(lyric.split())

				output.write(str(processedLyric))
				output.write("\n")
				output.close
				print(Fore.GREEN + '\t %d. [%s] Done.' % (count + 1, pair.song))
				found += 1

	percentage = 0 if len(pairs) is 0 else found/len(pairs)
	print(Style.RESET_ALL + '\n\t Found %d out of %d ' % (found, len(pairs)) + (Fore.GREEN if percentage == 1 else (Fore.RED if percentage == 0 else Fore.YELLOW)) + "({0:.0%})".format(percentage))
	print(Style.RESET_ALL)

if __name__ == '__main__':
	main()
