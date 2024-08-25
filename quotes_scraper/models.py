from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    fullname = StringField(required=True)  # Ім'я та прізвище автора
    born_date = StringField()  # Дата народження
    born_location = StringField()  # Місце народження
    description = StringField()  # Опис

class Quote(Document):
    tags = ListField(StringField())  # Теги для цитати
    author = ReferenceField(Author, reverse_delete_rule=4)  # Посилання на автора
    quote = StringField(required=True)  # Текст цитати
