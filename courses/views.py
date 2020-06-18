from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course


# Base View Class = VIEW

class CourseListView(View):
    template_name = 'course/course_list.html'
    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'object_list': self.queryset})


class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


# HTTP METHODS

# Create your views here.
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
