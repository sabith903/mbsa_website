from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    asstmanager = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    chest_number = models.IntegerField( blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Stage(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100 ,blank=True, null=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=20, decimal_places=2)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.program} - {self.score}"
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):  
        return self.title

