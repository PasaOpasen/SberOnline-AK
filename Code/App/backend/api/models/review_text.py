from django.db.models import Model, CharField, FloatField


class ReviewText(Model):
    review = CharField(max_length=20000)
