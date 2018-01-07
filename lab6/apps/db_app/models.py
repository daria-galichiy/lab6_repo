from django.db import models

# Create your models here.


class Actors(models.Model):
    actor_id = models.AutoField(primary_key=True)
    actor_name = models.CharField(max_length=100)


class Filmmakers(models.Model):
    filmmaker_id = models.AutoField(primary_key=True)
    filmmaker_name = models.CharField(max_length=100)


class Film_writers(models.Model):
    film_writer_id = models.AutoField(primary_key=True)
    film_writer_name = models.CharField(max_length=100)


class Producers(models.Model):
    producer_id = models.AutoField(primary_key=True)
    producer_name = models.CharField(max_length=100)


class Cameramen(models.Model):
    cameraman_id = models.AutoField(primary_key=True)
    cameraman_name = models.CharField(max_length=100)


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)


class Films(models.Model):
    film_id = models.AutoField(primary_key=True)
    film_name = models.CharField(max_length=100)
    release_date = models.DateField()
    in_the_lead_role = models.ManyToManyField(Actors)
    filmmaker = models.ForeignKey(Filmmakers, on_delete=models.CASCADE)
    film_writer = models.ForeignKey(Film_writers, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producers, on_delete=models.CASCADE)
    cameraman = models.ForeignKey(Cameramen, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    box_office_results = models.IntegerField()
