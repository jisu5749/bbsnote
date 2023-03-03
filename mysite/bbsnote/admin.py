from django.contrib import admin
from .models import Board
# Register your models here.
# admin.site.register(Board)

#제목검색
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Board,BoardAdmin)