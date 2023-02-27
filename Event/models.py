<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3ab9d94c055339275ba825dfc462c43b16398c1a
from django.db import models
from django.utils.timezone import datetime
from Person.models import Person
# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField()
    category_choices=(
        ('Musique','M'),
        ('Cinema','C'),
        ('Sport','S'))
    category=models.CharField(max_length=8,choices=category_choices)
    state=models.BooleanField(default=False)
    nbe_participant=models.IntegerField(default=0)
    event_date=models.DateField()
    creation_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        #on_delete=models.SET_NULL,
        #null=True
        #related_name="organisateur"             
    )
    participation=models.ManyToManyField(
        Person,
        related_name="participations",
        through="Event_Participation"
    )
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(
                    event_date__gte=datetime.now()),
                    name='Date doit être sup à date sys'
                )
        ]
        verbose_name_plural = 'Eventss'
    def __str__(self) -> str:
        return f"evennement est: {self.title}"
class Event_Participation(models.Model):
     person=models.ForeignKey(Person,on_delete=models.CASCADE)
     event=models.ForeignKey(Event,on_delete=models.CASCADE)
     participation_date=models.DateField(auto_now=True)
     class Meta:
<<<<<<< HEAD
         unique_together=('person','event')
=======
         unique_together=('person','event')
=======
from django.utils.timezone import datetime
from django.db import models
from Person.models import Person
# Create your models here.
CATEGORY_CHOICES = (
        ('MUSIC', 'Musique'),
        ('CINEMA', 'Cinema'),
        ('SPORT', 'Sport'),
    )
class Event(models.Model):
    def __str__(self):
        return f'Evenement est {self.title}'
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    
    category = models.CharField(
        max_length=6,
        choices=CATEGORY_CHOICES,
        default='MUSIC',
    )
    state = models.BooleanField(default=False)
    nbe_participant = models.IntegerField(default=0)
    event_date = models.DateTimeField()
    class Meta:
        constraints=[
            models.CheckConstraint(
            check=models.Q(event_date__gte=datetime.now()),
            name='Date doit etre sup à date sys'
            )
        ]
        verbose_name=("Evenement")

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(   #elly tgéri el relation
        Person,
        on_delete=models.CASCADE
        #on_delete=models.SET_NULL,
        #null=True
        #related_name=organizer
    )
    participation=models.ManyToManyField(  #Créer un classe association
         Person,
         related_name="participations",
         through="Event_Participation"
    )
class Event_Participation(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateField(auto_now=True)

    class Meta:
        unique_together=('person','event')
        verbose_name=("Person")
>>>>>>> 3ed9813b3c5878d7b5d3f7df95dcb9e91e62ae72
>>>>>>> 3ab9d94c055339275ba825dfc462c43b16398c1a
