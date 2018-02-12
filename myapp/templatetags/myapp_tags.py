from django import template
from ..models import Post, Category


register = template.Library()

# 装饰，将 get_recent_post 装饰为 register.simple_tag
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')#降序Descending

@register.simple_tag
def get_categories():
	return Category.objects.all()