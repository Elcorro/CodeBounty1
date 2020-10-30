from djongo import models

class Language(models.Model):
    CODE_LANG_CHOICES = (
        ('en', 'English'),
        ('pt', 'Portuguese'),
    )

    DIRECTION_CHOICES = (
        ('ltr', 'Left-to-right'),
        ('rtl', 'Right-to-left'),
    )

    code = models.CharField(max_length=2, choices=CODE_LANG_CHOICES, default='en')
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES, default='ltr')

    def __str__(self):
        return f'{self.code}'

    class Meta:
        abstract = True


class Campaign(models.Model):
    name = models.TextField()
    language = models.EmbeddedField(model_container=Language)
