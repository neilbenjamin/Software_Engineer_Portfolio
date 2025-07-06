from django.db import models

# Create your models here.

# Write the class parameters to the sqlite database using Django's ORM
# inheritence.

# Question Table


class Question(models.Model):  # ORM model as argument
    # sql col:
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # This Choice table's question column is referencing the PK from the
    # Question table.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
