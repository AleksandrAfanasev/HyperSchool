def tracklist(**tracks):
    for artists, albums in tracks.items():
        print(artists)
        for album, track in albums.items():
            print(f"ALBUM: {album} TRACK: {track}")
