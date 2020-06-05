import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length= 200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    articler = models.ForeignKey(Article, on_delete = models.CASCADE)
    autor_name = models.CharField('имя автора', max_length= 200)
    comment_text = models.CharField('текст коментария', max_length= 150)

    def __str__(self):
        return self.autor_name

