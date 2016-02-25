from django.db import models
from django.conf import settings
import decimal, datetime 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	#inherited from AbstractUser:
	#first_name
	#last_name
	#username
	#email
	#is_active
	#is_staff
	#date_joined
	#password?
	lemail = models.TextField(blank = True, null=True)
	school = models.TextField(blank=True, null=True)
	grade = models.PositiveSmallIntegerField(blank = True, null=True)
	def __str__(self):
		return self.username
class Tablet(models.Model):
    name = models.TextField(blank=True, null=True)
    imagePath = models.TextField(blank = True, null = True)
    history = models.TextField(blank = True, null=True)
    def __str__(self):
        return self.history
class Line(models.Model):
    #Lookup the rest of these options. And get them from stratford
    SIDE_CHOICES = (
        ('OBV', 'Obverse'),
        ('FR', 'FRONT'), #add the other sides
    )
    tablet = models.ForeignKey(Tablet, related_name = "TabletNum")
    side = models.TextField(blank= True, null=True)
    lineNumber = models.PositiveSmallIntegerField(blank= True, null=True)
    def __str__(self):
        return str(self.lineNumber)
class Sign(models.Model):
    filepath = models.TextField(blank=True, null=True)
    name = models.TextField(blank= True, null=True)
    mimeType = models.TextField()
    def __str__(self):
        return self.filepath
class AssyrianChar(models.Model):
    line = models.PositiveSmallIntegerField(blank=True, null=True)
    positionNO = models.PositiveSmallIntegerField(blank= True, null=True)
    Sign = models.ForeignKey(Sign, related_name = "char_sign")
    note = models.TextField(blank= True, null=True)
    def __str__(self):
        return self.note
class IdentifiedCharacter(models.Model): #change this to placement
    user = models.ForeignKey(User)
    sign = models.ForeignKey(Sign, related_name = "Sign", blank=True, null=True)
    date_recorded = models.DateTimeField(auto_now_add=True)
    link = models.TextField(blank = True, null=True)
    hotspot_x = models.PositiveSmallIntegerField(blank=True, null=True)
    hotspot_y = models.PositiveSmallIntegerField(blank=True, null=True)
    hotspot_width = models.PositiveSmallIntegerField(blank=True, null=True)
    hotspot_height = models.PositiveSmallIntegerField(blank=True, null=True)
    def __str__(self):
        return self.date_recorded
'''
Stored Procedures:
-	After a certain amount of user inputs, the database calculates the hotspots and sends the report to us.  
-	Make an admin site that shows the results of the tablets
-	Calculate how effective each user is at identifying characters, and show the user how successful they are at identifying characters.
'''
    