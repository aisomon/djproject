from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=25)
    message = models.TextField()
    Action_TAKEN = (
        ("NEW","New"),
        ("SEEN","Seen"),
        ("ACCEPTED","Accepted"),
        ("IN PROGRESS", "In Progress"),
        ("DONE", "Done"),
    )
    action = models.CharField(max_length=11,
    choices=Action_TAKEN, default="NEW")

    def __str__(self):
        return '{} | {} | {}'.format(self.name,self.subject,self.action)
    
