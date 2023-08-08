from oop.static_and_class_methods_exercise.document_management.topic import Topic
from oop.static_and_class_methods_exercise.document_management.category import Category
from oop.static_and_class_methods_exercise.document_management.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):

        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cur_category = next(filter(lambda k: k.id == category_id, self.categories))
        cur_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        cur_topic = next(filter(lambda k: k.id == topic_id, self.topics))
        cur_topic.topic = new_topic
        cur_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        cur_document = next(filter(lambda k: k.id == document_id, self.documents))
        cur_document.file_name = new_file_name

    def delete_category(self, category_id):
        cur_category = next(filter(lambda k: k.id == category_id, self.categories))
        self.categories.remove(cur_category)

    def delete_topic(self, topic_id):
        cur_topic = next(filter(lambda k: k.id == topic_id, self.topics))
        self.topics.remove(cur_topic)

    def delete_document(self, document_id):
        cur_document = next(filter(lambda k: k.id == document_id, self.documents))
        self.documents.remove(cur_document)

    def get_document(self, document_id):
        cur_document = next(filter(lambda k: k.id == document_id, self.documents))
        return cur_document

    def __repr__(self):
        result = [str(x) for x in self.documents]
        return '\n'.join(result)
