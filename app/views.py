from django.shortcuts import render
from .models import Category, Course
from django.db.models import Q 

def course_list(request):
    """View to display a list of courses."""
    categories = Category.objects.all()
    courses = Course.objects.all()

    query = request.GET.get('q')
    if query:
        courses = courses.filter(
            Q(title__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tutor_name__icontains=query)
        )
    
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    """View to display the details of a specific course."""
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})
