from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__ (self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category (self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
        
    def add_topic (self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
    
    def add_document (self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
    
    def edit_category (self, category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name
                return
    
    def edit_topic (self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder
                return
    
    def edit_document (self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.file_name = new_file_name
                return
    
    def delete_category (self, category_id):
        catToBeDel = [category for category in self.categories if category.id == category_id]
        if catToBeDel is not None:
            self.categories.remove(catToBeDel[0])

    def delete_topic (self, topic_id):
        topToBeDel = [topic for topic in self.topics if topic.id == topic_id]
        if topToBeDel is not None:
            self.topics.remove(topToBeDel[0])

    def delete_document (self, document_id):
        docToBeDel = [document for document in self.documents if document.id == document_id]
        if docToBeDel is not None:
            self.documents.remove(docToBeDel[0])
    
    def get_document (self, document_id):
        docToBeReturned = [document for document in self.documents if document.id == document_id]
        if docToBeReturned is not None:
            return docToBeReturned[0]
    
    def __repr__ (self):
        listToOutput = []

        for document in self.documents:
            listToOutput.append(f"{document.__repr__()}")
        
        return '\n'.join(listToOutput)
