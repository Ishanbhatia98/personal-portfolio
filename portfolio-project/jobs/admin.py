from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Education
from .models import Skills
from .models import Tskills
from .models import Project
from .models import Course
from .models import Profile
from .models import Profilefooter
from .models import Introduction
from .models import Summary
from .models import WorkSummary
from .models import Status

admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Tskills)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Profilefooter)
admin.site.register(Introduction)
admin.site.register(Summary)
admin.site.register(WorkSummary)
admin.site.register(Status)
