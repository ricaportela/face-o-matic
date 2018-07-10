from __future__ import unicode_literals
from cloudinary.models import CloudinaryField
from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # imageCloud = CloudinaryField('image')
    image = models.ImageField(upload_to='imagens/', blank=True)

    def __str__(self):
        return self.description if self.description != "" else "No Title"
