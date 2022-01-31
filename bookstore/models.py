from django.db import models


# TODO: Add functionality to scrape book information from Amazon

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=75)

    # isbn = models.IntegerField(blank=True)
    # publish_date = models.DateField(blank=True)
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)

    def __str__(self):
        return self.review_text
