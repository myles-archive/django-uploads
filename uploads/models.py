from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

try:
	from taggit.managers import TaggableManager
except ImportError:
	TaggableManager = False

try:
	from django_markup.fields import MarkupField
except ImportError:
	MarkupField = False

class Folder(models.Model):
	title = models.CharField(_('title'), max_length=200)
	slug = models.SlugField(_('slug'), max_length=25)
	
	parent = models.ForeignKey('self', blank=True, null=True,
		limit_choices_to={ 'parent': None })
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		verbose_name = _('folder')
		verbose_name_pluarl= _('folders')
		db_tables = 'uploads_folders'
		ordering = ('title',)
	
	@property
	def full_title(self):
		if self.parent:
			return u"%s/%s" % (self.parent.title, self.title)
		else:
			return u"%s" % self.title
	
	@property
	def full_slug(self):
		if self.parent:
			return u"%s/%s" % (self.parent.slug, self.slug)
		else:
			return u"%s" % self.slug
	
	def __unicode__(self):
		return u"%s" % self.full_title
	
	@permalink
	def get_absolute_url(self):
		return ('uploads_folder_detail', None, {
			'slug': self.full_slug
		})

class FileUpload(models.Model):
	title = models.CharField(_('title'), max_length=200)
	slug = models.SlugField(_('slug'), max_length=25)
	
	folder = models.ForeignKey(Folder, blank=True, null=True)
	
	upload = FileField(upload_to="uploads/files/%Y-%m-%d")
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		verbose_name = _('file upload')
		verbose_name_pluarl = _('file uploads')
		db_table = 'uploads_file_uploads'
		ordering = ('title',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@permalink
	def get_absolute_url(self):
		return ('uploads_file_detail', None, {
			'folder': self.full_slug,
			'slug': self.slug,
		})