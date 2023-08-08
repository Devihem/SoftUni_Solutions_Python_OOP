class Category:
    def __init__(self, id_category: int, name: str):
        self.id = id_category
        self.name = name

    def edit(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
