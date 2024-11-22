from django.db import models

class Question(models.Model):
    """
    A model representing a poll question.

    Attributes:
        question_text (str): The text of the question, limited to 200 characters.
        pub_date (datetime): The date and time when the question was published.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        String representation of the Question model.

        Returns:
            str: The text of the question.
        """
        return self.question_text


class Choice(models.Model):
    """
    A model representing a possible answer (choice) for a specific poll question.

    Attributes:
        question (Question): A ForeignKey linking the choice to a specific question.
        choice_text (str): The text of the choice, limited to 200 characters.
        votes (int): The number of votes this choice has received, defaulting to 0.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        String representation of the Choice model.

        Returns:
            str: The text of the choice.
        """
        return self.choice_text
