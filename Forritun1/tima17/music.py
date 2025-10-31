class MusicAlbum:
    def __init__(self, band = "unknown band", title = "unknown", year = "unknown year"):
        self.band = band
        self.title = title
        self.year = year

    def set_album(self, band = "unknown band", title = "unknown", year = "unknown year"):
        self.band = band
        self.title = title
        self.year = year
        return  

    def __str__(self) -> str:
        return f"Album {self.title} by {self.band}, released in {self.year}."

# album = MusicAlbum()
# print(album)

# album.set_album("Talking Heads", "Remain in Light", 1980)
# print(album)

# album.set_album("AC/DC", "Back in Black")
# print(album)

# album_beatles = MusicAlbum("The Beatles", "Abbey Road")
# album_london_calling = MusicAlbum(title="London Calling", year=1979)
# album_beyonce = MusicAlbum(band="Beyonce", year=2016)

# print(album_beatles)
# print(album_london_calling)
# print(album_beyonce)