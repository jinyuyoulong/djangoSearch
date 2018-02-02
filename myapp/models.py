from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()

	objects = models.Manager()
	# 创建时间 最后修改时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	# 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
	excerpt = models.CharField(max_length=200, blank=True);	
	# foreign key 外键，表明一对多关系；
	# manytomanyfield 表明多对多关系
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)

	# 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	#add function
	# 自定义 get_absolute_url 方法
	# 记得从 django.urls 中导入 reverse 函数
	def get_absolute_url(self):
		return reverse('myapp:detail', kwargs={'pk':self.pk})