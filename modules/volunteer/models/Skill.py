from django.db import models

class Skill(models.Model):
    class Meta:
        db_table='mst_skills'
    
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
