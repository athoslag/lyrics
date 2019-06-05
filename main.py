from vagalume import lyrics

artist_name = 'radiohead'
song_name = 'there, there'

result = lyrics.find(artist_name, song_name)

if result.is_not_found():
    print('Song not found')
else:
    print(result.song.name)
    print(result.artist.name)
    print()
    print(result.song.lyric)
    print()
    
    translation = result.get_translation_to('pt-br')
    if not translation:
        print('Translation not found')
    else:
        print(translation.name)
        print(translation.lyric)
