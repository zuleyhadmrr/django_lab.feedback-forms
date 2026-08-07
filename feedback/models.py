from django.db import models

class FeedbackEntry(models.Model):

    name = models.CharField(max_length=70, verbose_name='Name Surname')
    email = models.EmailField(max_length=40, verbose_name='Email')

    TOPIC_CHOICES = [
        ('general', 'General'),
        ('bug', 'Error Report'),
        ('feature', 'Features'),
        ('support', 'Support')
    ]
    topic = models.CharField(
        max_length=20, 
        choices=TOPIC_CHOICES, 
        default='general', 
        verbose_name='Topic')

    message = models.TextField(verbose_name='Message')

    RAITING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    rating = models.IntegerField(
        choices=RAITING_CHOICES,
        verbose_name='Evaluation')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Feedback'
    

    def __str__(self):
        return f'{self.name} - {self.get_topic_display()}'