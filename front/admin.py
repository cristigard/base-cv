from django.contrib import admin
from .models import Skill, Language, Work, Education

admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Work)
admin.site.register(Education)