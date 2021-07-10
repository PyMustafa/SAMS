from django.db import models
from SAMS.models import Professor


# Create your models here.


class Fourth_Year_Subjects(models.Model):
    choice = [
        ('CS1', 'CS1'),
        ('CS2', 'CS2'),
        ('CS3', 'CS3'),
        ('CS4', 'CS4'),
        ('CS5', 'CS5'),
        ('CS6', 'CS6'),
        ('CS7', 'CS7'),
    ]
    professor_name = models.ForeignKey(Professor, to_field='Name', on_delete=models.CASCADE)
    subject = models.CharField(max_length=20, choices=choice, unique=True)

    def __str__(self):
        return self.subject


class LectureSchedule(models.Model):
    days = [
        ('Sat', 'Sat'),
        ('Sun', 'Sun'),
        ('Mon', 'Mon'),
        ('Tue', 'Tue'),
        ('Wed', 'Wed'),
        ('Thu', 'Thu'),
        ('Fri', 'Fri'),
    ]
    times = [
        ('9', '9'),
        ('10.30', '10.30'),
        ('12', '12'),
        ('13.30', '13.30'),
        ('15', '15'),
    ]

    subject = models.ForeignKey(Fourth_Year_Subjects, to_field='subject', on_delete=models.CASCADE)
    hall = models.IntegerField()
    day = models.CharField(max_length=10, choices=days)
    time = models.CharField(max_length=10, choices=times)

    def __str__(self):
        return str(self.subject)


class CS1(models.Model):
    student_id = models.CharField(max_length=50, default='0')
    week_1 = models.CharField(max_length=10, default='0')
    week_2 = models.CharField(max_length=10, default='0')
    week_3 = models.CharField(max_length=10, default='0')
    week_4 = models.CharField(max_length=10, default='0')
    week_5 = models.CharField(max_length=10, default='0')
    week_6 = models.CharField(max_length=10, default='0')
    week_7 = models.CharField(max_length=10, default='0')

    def __str__(self):
        return self.student_id

