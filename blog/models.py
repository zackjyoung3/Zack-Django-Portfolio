from django.db import models

# category model very simple, just going to store the name of a category
class Category(models.Model):
    name = models.CharField(max_length=20)

# now the post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # auto_now_add to assign when created
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now to assign whenever saved
    last_modified = models.DateTimeField(auto_now=True)
    # the relationship between categories and posts is many to many
    # ie a post can have many categories and a category can have many posts
    categories = models.ManyToManyField('Category', related_name='posts')

# model for a comment
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # use the foreign key for a many to one relationship
    # ie many comments can be assigned to one post
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
