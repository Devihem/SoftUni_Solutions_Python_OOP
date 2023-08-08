from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        needed_pages = photos_count / cls.MAX_PHOTOS_PER_PAGE
        return cls(ceil(needed_pages))

    def add_photo(self, label):
        for page_number in range(len(self.photos)):
            photos_index = len(self.photos[page_number])
            if photos_index < self.MAX_PHOTOS_PER_PAGE:
                self.photos[page_number].append(label)
                return f"{label} photo added successfully on page " \
                       f"{page_number + 1} slot {photos_index + 1}"

        else:
            return "No more free slots"

    def display(self):
        result = []
        for page_index in range(len(self.photos)):
            result.append(11*'-')
            photo_line = [len(self.photos[page_index]) * ['[]']]
            result.append(' '.join(*photo_line))
        else:
            result.append(11 * '-')
        return '\n'.join(result)