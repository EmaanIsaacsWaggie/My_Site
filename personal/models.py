from django.db import models

class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the post, limited to 140 characters.
        body (str): The main content of the post.
        signature (str): A default signature for the post, with a maximum length of 140 characters.
        date (datetime): The date and time the post was created or published.
    """

    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(
        max_length=140, 
        default="Emaan Isaacs Waggie"
    )
    date = models.DateTimeField()

    def __str__(self):
        """
        String representation of the Post model.

        Returns:
            str: The title of the post.
        """
        return self.title
