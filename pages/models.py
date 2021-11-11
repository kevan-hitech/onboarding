import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Sheet(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20)
    t_img = models.ImageField(upload_to="static/images/",null=True)
    t_debut = models.CharField(max_length=100, null=True)
    t_form = models.CharField(max_length=30, null=True)
    t_affil = models.CharField(max_length=100, null=True)
    t_bday = models.CharField(max_length=100, null=True)
    t_bplace = models.CharField(max_length=100, null=True)
    t_age = models.IntegerField(null=True)

    body = RichTextField(blank=True, null=True)
    """
    section1 = models.TextField()
    section2 = models.TextField()
    section3 = models.TextField()
    section4 = models.TextField()
    section5 = models.TextField()
    """
    rank_s = models.IntegerField(null=True)
    rank_e = models.IntegerField(null=True)
    rank_m = models.IntegerField(null=True)
    rank_i = models.IntegerField(null=True)
    rank_r = models.IntegerField(null=True)
    rank_t = models.IntegerField(null=True)
    section6 = models.TextField()
    pub_date = models.DateTimeField('date published',auto_now_add=True, editable=False, null=False, blank=False)
    edit_date = models.DateTimeField('date of last edit',auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.title

    # Test if updated recently
    def was_edited_recently(self):
        return self.edit_date >= timezone.now() - datetime.timedelta(days=7)

    def get_absolute_url(self):
        return u'/%d' % self.id