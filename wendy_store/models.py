from django.db import models


class Post(models.Model):
    # 제목(title)
    title = models.CharField(max_length=30)
    # 내용(content)
    content = models.TextField()

    # 작성일(created_at)
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일(updated_at)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자 정보(author): 아직 안만듬

    def __str__(self):
        return f'[{self.pk}] {self.title}'

