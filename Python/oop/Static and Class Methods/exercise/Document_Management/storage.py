from typing import List

from Document_Management.category import Category
from Document_Management.document import Document
from Document_Management.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

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
        category = next((category for category in self.categories if category.id == category_id), None)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next((topic for topic in self.topics if topic.id == topic_id), None)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((document for document in self.documents if document.id == document_id), None)
        document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = next((category for category in self.categories if category.id == category_id), None)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = next((topic for topic in self.topics if topic.id == topic_id), None)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = next((document for document in self.documents if document.id == document_id), None)
        self.documents.remove(document)

    def get_document(self, document_id: int):
        document = next((document for document in self.documents if document.id == document_id), None)
        return document

    def __repr__(self):
        result = [document.__repr__() for document in self.documents]
        return '\n'.join(result)


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize Document_Management")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
