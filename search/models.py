from django_localflavor_us.models import USStateField
from django.contrib import admin
from django.db import models
GENDER = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Other'),
    (3, 'None')
)

PROFIT_STATUS = (
    (0, 'Public'),
    (1, 'Private nonprofit'),
    (2, 'For-profit')
)

ETHNICITIES = (
    (0, 'American Indian/Alaska Native'),
    (1, 'Asian'),
    (2, 'Black/African American'),
    (3, 'Native Hawaiian/Pacific Islander'),
    (4, 'White/Caucasian'),
    (5, 'International'),
    (6, 'Hispanic')
)

STATUS = (
    (0, 'active'),
    (1, 'expired')
)

DEADLINE_TYPES = (
    (0, 'Regular'),
    (1, 'Weekly'),
    (2, 'Monthly'),
    (3, 'Unknown')
)


class University(models.Model):
    homepage_url = models.URLField()
    city = models.CharField(max_length=100)
    state = USStateField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    student_population = models.IntegerField(null=True)
    undergrad_tuition_resident = models.IntegerField()
    undergrad_tuition_nonresident = models.IntegerField()
    profit_status = models.SmallIntegerField(choices=PROFIT_STATUS, null=True)

    def __unicode__(self):
        return self.name

# Create your models here.
class Scholarship(models.Model):
    title = models.CharField(max_length=400)
    third_party_url = models.URLField()
    street_address = models.TextField(blank=True, null=True)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True, blank=True)
    deadline = models.DateField(blank=True, null=True)
    deadline2 = models.DateField(blank=True, null=True)
    deadline3 = models.DateField(blank=True, null=True)
    deadline_type = models.SmallIntegerField(choices=DEADLINE_TYPES, default=0)
    essay_required = models.BooleanField()
    amount_usd = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=200)
    high_school_eligible = models.BooleanField(default=True)
    undergrad_eligible = models.BooleanField(default=True)
    graduate_eligible = models.BooleanField(default=True)
    min_age_restriction = models.SmallIntegerField(blank=True, null=True)
    state_restriction = USStateField(blank=True)
    essay_length_words = models.IntegerField(blank=True, null=True)
    gpa_restriction = models.FloatField(blank=True, null=True)
    additional_restriction = models.TextField(blank=True)
    major_restriction = models.CharField(max_length=1000, blank=True)
    university_restriction = models.ManyToManyField(University, null=True, blank=True)
    ethnicity_restriction = models.SmallIntegerField(choices=ETHNICITIES, blank=True, null=True)
    gender_restriction = models.SmallIntegerField(choices=GENDER, blank=True, null=True)
    sponsored = models.BooleanField()
    status = models.SmallIntegerField(choices=STATUS, blank=True, null=True, editable=False, default=0)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class SubmittedLink(models.Model):
    third_party_url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    email = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title


# make models available in admin
admin.site.register(University)
admin.site.register(Scholarship)
admin.site.register(SubmittedLink)


