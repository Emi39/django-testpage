from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Section"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True, verbose_name="Project URL")
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return f"Contact - {self.email}"