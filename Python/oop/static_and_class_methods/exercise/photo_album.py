class PhotoAlbum:
    NUMBER_OF_DASHES = 11
    SEPARATOR_SYMBOL = '-'

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        total_pages = (photos_count + 3) // 4
        return cls(total_pages)

    def add_photo(self, label: str):
        page_count = 0
        for page in self.photos:
            page_count += 1
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {page_count} slot {len(page)}"

        return "No more free slots"

    def display(self):
        result_string = []
        line = PhotoAlbum.NUMBER_OF_DASHES * PhotoAlbum.SEPARATOR_SYMBOL
        page_count = 0
        for page in self.photos:
            if page_count == 0:
                result_string.append(f"{line}\n{' '.join(['[]' for _ in page])}\n{line}")
                page_count += 1
            else:
                result_string.append(f"{' '.join(['[]' for _ in page])}\n{line}")

        return "\n".join(result_string)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
