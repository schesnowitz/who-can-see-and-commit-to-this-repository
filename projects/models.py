from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField


    
class Project(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    sub_title_1 = models.CharField(max_length=255, blank=True, null=True)
    tab_title = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(default='media/placeholders/gallery.jpg')
    description = RichTextField(blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)
    github = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    udemy = models.URLField(blank=True, null=True)
    link_1 = models.URLField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:project_detail", kwargs={"pk": self.pk})


"""
Note that there are two main ways to refer to a custom user model: AUTH_USER_MODEL and get_-
user_model143. As general advice:
• AUTH_USER_MODEL makes sense for references within a models.py file
• get_user_model() is recommended everywhere else such as views, tests, etc.
"""


class Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    code_title = models.CharField(max_length=255, blank=True, null=True)
    code_url = models.URLField(blank=True, null=True)
    code_notes = RichTextField(blank=True, null=True)
    code = RichTextField(blank=True, null=True)


    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.project.title

    def get_absolute_url(self):
        return reverse("project:project_list")


class Text(models.Model):

    page_text_1 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_2 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_3 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_4 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_5 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_6 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_7 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_8 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_9 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_10 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_11 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_12 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_13 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_14 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_15 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_16 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_17 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_18 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_19 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_20 = models.CharField(max_length=1000, blank=True, null=True)
    page_text_21 = models.CharField(max_length=1000, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return str(self.id)

  
