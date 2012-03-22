from django.contrib import admin

from uploads.models import Folder, FileUpload

class FolderAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class FileUploadAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Folder, FolderAdmin)
admin.site.register(FileUpload, FileUploadAdmin)