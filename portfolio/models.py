from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=250, blank=False)
    image = models.ImageField(upload_to='portfolio/images/')  # create a portfolio path
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
