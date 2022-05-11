def make_album(artist_name, album_title, num_tracks = ''):
	"""Makes a dictionary of information about an album with given inputs"""
	album = {'artist_name': artist_name, 'album_title': album_title}
	if num_tracks:
		album['num_tracks'] = num_tracks
	return album

print("We are making a list of albums."
	  "\nPlease enter 'q' at any prompt to quit.")

while True:
	print("\nLet's start a new album:")
	artist_name = input("Input album's artist:")
	if artist_name == 'q':
		break
	album_title = input("Input album title:")
	if album_title == 'q':
		break
	num_tracks = input("Input integer number of tracks on album or press enter to skip:")
	if num_tracks == 'q':
		break
	if num_tracks != '':
		num_tracks = int(num_tracks)
	print(make_album(artist_name, album_title, num_tracks))





