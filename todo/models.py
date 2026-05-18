from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status_choises = [
        ('active', 'Active'), 
        ('in_progress', 'In Progress'),
        ('discontinued', 'Discontinued'),
        ('completed', 'Completed'),]
    status = models.CharField(
        max_length=20,
        choices=status_choises,
        default='active')
    class priority(models.TextChoices):
        LOW = 'Low'
        MEDIUM = 'Medium'
        HIGH = 'High'
    priority = models.CharField(max_length=10, choices=priority.choices, default=priority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.title

class username(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
