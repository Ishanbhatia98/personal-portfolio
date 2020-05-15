from django.shortcuts import render, get_object_or_404
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
# Create your views here.

def home(request):
    jobs = Job.objects
    edus = Education.objects
    skills = Skills.objects
    tskills = Tskills.objects
    projects = Project.objects
    courses = Course.objects
    profile = Profile.objects
    profile_f = Profilefooter.objects
    intro = Introduction.objects
    summary = Summary.objects
    status = Status.objects
    ws = WorkSummary.objects
    dict_objects = {'jobs':jobs, 'edus':edus, 'skills':skills, 'tskills':tskills, 'projects':projects, 'courses':courses, 'profile':profile, 'pf':profile_f, 'intro':intro, 'summary':summary, 'ws':ws, 'status':status}
    return render(request, 'jobs/home.html',dict_objects )

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html',{'job':job_detail})
