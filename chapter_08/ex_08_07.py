def make_album(artist_name, album_title, num_tracks = ''):
	album = {'artist_name': artist_name, 'album_title': album_title}
	if num_tracks:
		album['num_tracks'] = num_tracks
	return album

album_1 = make_album('Beatles', 'Revolver')
album_2 = make_album('Kendrick Lamar', 'To Pimp a Butterfly')
album_3 = make_album('Amy Winehouse', 'Back to Black', 11)
album_4 = make_album('Are You Experienced', 'Jimi Hendrix')
print(album_1)
print(album_2)
print(album_3)
print(album_4)
