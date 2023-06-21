from django.contrib import admin
from courses.models import Course,Payment,UserCourse,Tag,Learning,Prerequisite,Video
# Register your modelhere.

class TagAdmin(admin.TabularInline):
    model = Tag
class VideoAdmin(admin.TabularInline):
    model = Video
class LearningAdmin(admin.TabularInline):
    model = Learning
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin,VideoAdmin]
        
admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)