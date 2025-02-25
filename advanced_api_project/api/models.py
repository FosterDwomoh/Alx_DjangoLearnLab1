from django.db import models

# Create your models here.
class Author(models.models):
    """
    Model to represent an author with a name field.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Book(models.Model):
        """
        Model to represent a book with a title, publication year, and a foreign key to Author.
        """
        title = models.CharField(max_length=200)
        publication_year = models.IntegerField()
        author = models.ForeignKey(Author, related_name = 'books', on_delete=models.CASCADE)

        def __str__(self):
            return self.title
            