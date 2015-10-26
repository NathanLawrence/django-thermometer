from django.db import models

class Therm(models.Model):
	name = models.CharField(max_length = 50)
	heading = models.CharField(max_length = 140)
	htmlCopy = models.TextField()
	buttonLabel = models.CharField(max_length = 50)
	buttonURL = models.URLField(max_length = 200)
	fundGoal = models.IntegerField()
	fundCurrent = models.IntegerField()

	def getPercent():
		percent = (fundGoal / fundCurrent) * 100
		if percent > 100:
			percent = 100
		return percent
