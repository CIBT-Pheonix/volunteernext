from django.contrib import admin
from modules.volunteer.models.Skill import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass