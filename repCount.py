import operator
import os
import string
import sys

dirname = sys.argv[1]
path = dirname + '/songs/'
reps = []

def removePunctuation(strList):
	translator = str.maketrans('', '', string.punctuation)
	newList = []
	
	for item in strList:
		newList.append(item.translate(translator))

	return newList

def saveReps():
	output = open("%s/repetitiveness.txt" % dirname, "w+")

	for rep in reps:
		output.write('%s\n' % rep)
		
	output.close

def countSong(originalLyrics, fileName):
	words = []
	occurencies = {}
	lyrics = removePunctuation(originalLyrics.split())

	for word in lyrics:
		if word in words:
			occurencies[word] += 1
		else:
			words.append(word)
			occurencies[word] = 1

	maxkey = str(max(occurencies.items(), key=operator.itemgetter(1))[0])
	minkey = str(min(occurencies.items(), key=operator.itemgetter(1))[0])

	badElements = 0
	treshold = int((occurencies[maxkey] + occurencies[minkey]) / 4)

	if treshold <= 2:
		treshold = (occurencies[maxkey] + occurencies[minkey]) / 2

	for key in occurencies:
		if occurencies[key] >= treshold:
			badElements += occurencies[key]

	repetitiveness = (len(lyrics) - (len(lyrics) - badElements)) / len(lyrics)
	print("\t " + fileName + " repetitiveness: {0:.2%}".format(repetitiveness))

	reps.append(fileName.split('.')[0] + ": {0:.2%}".format(repetitiveness))

def getLyrics(file):
	f = open(os.path.join(path,file),'r')
	lyrics = f.read()
	f.close()
	return lyrics

def main():
	files = os.listdir(path)
	indexes = map(lambda x: (x.split('.'))[0], files)
	zipped = zip(indexes, files)

	for (idx,file) in sorted(zipped, key = lambda f: int(f[0])):
		if os.path.isfile(path + file):
			lyrics = getLyrics(file)
			countSong(lyrics, file)
		else:
			print('\t os.path.isfile returned False.')

	saveReps()

if __name__ == '__main__':
    main()
