from django.http import HttpResponse
from django.template import loader
from .models import Project


def index(request):
    projects_list = Project.objects.order_by('created_at')[:5]
    template = loader.get_template('projects/index.html')
    context={'projects_list': projects_list}
    # output = ", ".join([p.name for p in projects_list])
    return HttpResponse(template.render(context,request))

def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)


def results(request, project_id):
    response = "You're looking at the results of project %s."
    return HttpResponse(response % project_id)


def vote(request, project_id):
    return HttpResponse("You're voting on project %s." % project_id)
