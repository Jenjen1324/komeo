from django.contrib.auth.models import User
from django.db import models
from django.template import Context, loader
from django_markdown.models import MarkdownField
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.signals import saved_file


class RegUser(models.Model):
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=255, null=True)
	profile_image = ThumbnailerImageField(upload_to="profile_images/", resize_source=dict(size=(500, 500)), null=True, blank=True)
	date_registered = models.DateField(auto_now_add=True)
	about = models.TextField(default="I'm a metalface", null=True, blank=True)

	def __str__(self):
		return self.user.name


class Project(models.Model):
	idname = models.SlugField()
	name = models.CharField(max_length=40, unique=True)
	description = MarkdownField()
	downloads = models.PositiveIntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	author = models.ManyToManyField(User)
	version = models.CharField(max_length=10, blank=True)
	ispublic = models.BooleanField(default=True)
	thumbnail = ThumbnailerImageField(upload_to="thumbnails/", resize_source=dict(size=(1920, 1080)))

	file = models.FileField(upload_to="projects/", null=True, blank=True)
	file_apk = models.FileField(upload_to="projects/apks/", null=True, blank=True)
	url_playstore = models.CharField(max_length=255, null=True, blank=True)
	url_appstore = models.CharField(max_length=255, null=True, blank=True)
	url_winstore = models.CharField(max_length=255, null=True, blank=True)
	url_website = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name

	def get_desc(self):
		return loader.get_template('table/name_field.html').render({'project': self})

	def get_thumb(self):
		t = loader.get_template('table/thumb_field.html')
		c = Context({'project': self})
		return t.render(c)

	def get_pretty_authors(self):
		return loader.get_template('table/author_field.html').render({'authors': self.author.all()})


class ProjectVote(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	is_upvote = models.BooleanField()


class Comment(models.Model):
	author = models.ForeignKey(User)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	project = models.ForeignKey(Project)
	replyto = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

	def __str(self):
		return 'Comment on: ' + self.project.name

	def get_replies(self):
		return Comment.objects.filter(project=self.project, replyto=self)


saved_file.connect(generate_aliases_global)
