from django.db import models

class Match(models.Model):
    code = models.CharField(max_length=10, unique=True)
    teamBlue = models.CharField(max_length=250)
    teamRed = models.CharField(max_length=250)
    scoreB = models.IntegerField(default=0)
    scoreR = models.IntegerField(default=0)

    def pointR(self, points):
        self.scoreR += int(points)

    def pointB(self, points):
        print(points)
        print(self.scoreB)
        self.scoreB = self.scoreB+int(points)
        print(self.scoreB)

    def __str__(self) -> str:
        return self.code