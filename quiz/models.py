from tkinter import CASCADE
import uuid
from django.db import models


class Question(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=200)
    choices = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Choice(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    def __str__(self):
        return self.text

class Quiz(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    questions = models.CharField(max_length=1000)
    def __str__(self):
        return self.questions

class Answer(models.Model):
    question_uuid = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.CharField(max_length=200)
    def __str__(self):
        return self.choices

class Answers(models.Model):
    quiz_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answers = models.CharField(max_length=200)
    def __str__(self):
        return self.answers