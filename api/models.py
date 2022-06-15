from django.db import models

class Images(models.Model):
    ImageData = models.TextField(blank=True)

    def __str__(self):
        return self.ImageData[:15] + "..."
