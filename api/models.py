from slugify import slugify
# Django
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class APIModel(models.Model):
    """
        Model base for all model in this app,
        here we set created field and the last time record
        it was save. Both are DateTimeField
    """
    created = models.DateTimeField(
        auto_now_add=True,
    )
    last_write = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
        ordering = ['-id']


class Team(APIModel):
    """Team model. """
    name = models.CharField(
        max_length=255
    )
    slug_name = models.SlugField(
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name)
        super(Team, self).save(*args, **kwargs)


class Client(APIModel):
    """Client model definitions   """
    name = models.CharField(
        max_length=120,
    )
    last_name = models.CharField(
        max_length=120,
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Profile(APIModel):
    """
        Profile store data additional user data, here we can find team,
        sales and other important fields.
        An user must have a profile and a profile must have a user.
        Relation is OneToOneFiled
   """

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name='users',
        null=True
    )

    def __str__(self):
        return str(self.user)


class Sales(APIModel):
    """User sales """
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='sales',
    )
    date = models.DateField(
        verbose_name='Date sale',
    )
    amount = models.FloatField(
        verbose_name='Sale amount',
        default=0
    )

    def __str__(self):
        return f"{str(self.client)} - {str(self.date)}  ${self.amount}"
