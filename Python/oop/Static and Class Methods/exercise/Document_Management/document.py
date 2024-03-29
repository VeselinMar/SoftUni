from Document_Management.category import Category
from Document_Management.topic import Topic


class Document:

    def __init__(self, id_: int, category_id: int, topic_id: int, file_name: str):
        self.id = id_
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id_: int, category: Category, topic: Topic, file_name: str):
        return cls(id_, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        try:
            self.tags.remove(tag_content)
        except ValueError:
            pass

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return (f"Document {self.id}: {self.file_name}; category {self.category_id},"
                f" topic {self.topic_id}, tags: {', '.join(self.tags)}")
