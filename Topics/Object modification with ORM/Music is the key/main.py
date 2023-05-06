beatles_albums = Album.objects.filter(artist='Beatles')
create_nirvana = Album.objects.create(artist="Nirvana", title="Nevermind", genre='rock')
artists_exclude_nirvana = Album.objects.exclude(artist='Nirvana')
del_smashing_pumpkins = Album.objects.filter(artist='Smashing Pumpkins', title='Siamese Dream').delete()
