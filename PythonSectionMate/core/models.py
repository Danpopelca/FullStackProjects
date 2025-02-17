from django.db import models

class Server(models.Model):
    """Model pentru ospătarii disponibili"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    """Model pentru secțiunile din restaurant"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ShiftAssignment(models.Model):
    """Model care asociază serverii cu secțiunile în fiecare zi"""
    date = models.DateField(auto_now_add=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.server.name} -> {self.section.name} ({self.date})"