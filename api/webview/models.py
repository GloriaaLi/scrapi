from django.db import models
from django_pgjson.fields import JsonField


class Document(models.Model):
    source = models.CharField(max_length=100)
    docID = models.CharField(max_length=100)

    providerUpdatedDateTime = models.DateTimeField(null=True)

    raw = JsonField()
    normalized = JsonField()


class HarvesterResponse(models.Model):

    key = models.TextField(primary_key=True)

    method = models.CharField(max_length=8)
    url = models.TextField()

    # Raw request data
    ok = models.NullBooleanField(null=True)
    content = models.BinaryField(null=True)
    encoding = models.TextField(null=True)
    headers_str = models.TextField(null=True)
    status_code = models.IntegerField(null=True)
    time_made = models.DateTimeField(auto_now=True)