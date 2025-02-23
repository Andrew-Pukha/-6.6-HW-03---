from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.Status.PUBLISHED)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # 1. суммарный рейтинг каждой статьи автора умножается на 3
        post_rating = Post.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum'] or 0
        post_rating *= 3

        # 2. суммарный рейтинг всех комментариев автора
        comment_rating = Comment.objects.filter(user=self.user).aggregate(Sum('rating'))['rating__sum'] or 0

        # 3. суммарный рейтинг всех комментариев к статьям автора
        post_comments_rating = Comment.objects.filter(post__author=self).aggregate(Sum('rating'))['rating__sum'] or 0

        # Итоговый рейтинг
        self.rating = post_rating + comment_rating + post_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})




class Post(models.Model):
    ARTICLE = 'AR'
    NEWS = 'NW'
    POST_TYPES = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость'),
    ]

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=POST_TYPES, default=ARTICLE)
    created_at = models.DateTimeField(auto_now_add=True)
    #categories = models.ManyToManyField(Category, through='PostCategory')       #--
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    objects = models.Manager()
    published = PublishedModel()

    #-- Материал выводится в порядке от более свежей к самой старой:
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...' if len(self.content) > 124 else self.content




class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания
    rating = models.IntegerField(default=0)  # Рейтинг комментария

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
