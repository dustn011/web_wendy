from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # 제목(title)
    title = models.CharField(max_length=30)
    # 내용(content)
    content = models.TextField()

    head_image = models.ImageField(upload_to='wendy_store/images/%Y/%m/%d/', blank=True)
    # 작성일(created_at)
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일(updated_at)
    updated_at = models.DateTimeField(auto_now=True)

    # 작성자 정보(author)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/wendy_store/{self.pk}/'


class Comment(models.Model):
    # 어떤 포스트에 대한 댓글 저장 post 필드
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 작성자를 저장 author 필드
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 댓글 내용 저장 content 필드
    content = models.TextField()
    # 작성일시 저장 created_at 필드
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일시 저장 modified_at 필드
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.author}]::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'