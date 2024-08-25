from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    name = StringField(required=True)
    birthdate = StringField()
    bio = StringField()

class Quote(Document):
    text = StringField(required=True)
    author = ReferenceField(Author, required=True)
    tags = ListField(StringField())
