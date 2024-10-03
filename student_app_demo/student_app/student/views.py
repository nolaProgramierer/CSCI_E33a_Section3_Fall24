from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.contrib import messages


from .models import Student, Advisor, Course


#---------------------------------------------
# Model forms
#---------------------------------------------
# Inherits from ModelForm, form fields, validation, & save logic
class CourseForm(ModelForm):
    
    # Defines metadata for CourseForm
    class Meta:
        model = Course
        fields = ['dept','course_num', 'subject', 'description']

    # Customize initialization of CourseForm 
    def __init__(self, *args, **kwargs):
        # Call parent class (ModelForm) __init__ method
        super().__init__(*args, **kwargs)
        # 'visible_fields()' method provided by the form class
        for field in self.visible_fields():
            # Update HTML attributes on widget
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })
                

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'student_advisor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })


class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })


#---------------------------------------------
# Form form
#---------------------------------------------
class CourseSelectionForm(forms.Form):
    # Define field for selecting an object from a queryset
    course = forms.ModelChoiceField(queryset=Course.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))


#---------------------------------------------
# Function views
#---------------------------------------------
def index(request):
    students = Student.objects.order_by("lname")
    return render(request, "student/index.html", {"students": students})


def course_list(request):
    courses = Course.objects.all()
    return render(request, "student/course_list.html", {"courses": courses})


def course_detail(request, id):
    # Return object, if exists, or 404
    course = get_object_or_404(Course, pk=id)
    return render(request, "student/course_detail.html", {"course": course})


def advisor_list(request):
    advisors = Advisor.objects.all()
    return render(request, "student/advisor_list.html", {"advisors": advisors})


def advisor_detail(request, id):
    advisor = get_object_or_404(Advisor, pk=id)
    return render(request, "student/advisor_detail.html", {"advisor": advisor})


def add_student(request):
    if request.method == "POST":
        # Bind user input to the form
        student_form = StudentForm(request.POST)
        # Server-side validation
        if student_form.is_valid():
            # Save new student object
            new_student = student_form.save(commit=True)
            # Call 'student_page' path, pass it an argument
            return HttpResponseRedirect(reverse("student_page", args=(new_student.id,)))
    else:
        # Empty form
        student_form = StudentForm()

    return render(request, "student/add_student.html", {"form": student_form})       


def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        # Form bound with input data, form associated with 'student' object
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("student_page", args=(student.id,)))
    else:
        form = StudentForm(instance=student)

    return render(request, "student/edit_student.html", {"form": form, "student": student})


def student_page(request, student_id):
    student = Student.objects.get(pk=student_id)
    courses = Course.objects.all()
    registered_courses = student.courses.all()
    context = {"student": student, "registered_courses": registered_courses, "courses": courses}
    return render(request, "student/student_page.html", context)


def course_page(request, course_id):
    course = Course.objects.get(pk=course_id)
    course_students = course.students.all()
    context = {"course": course, "students": course_students}
    return render(request, "student/course_page.html", context)


def new_course(request):
    if request.method == "POST":
        # Form is populated with input data 
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_list"))
    else:
        form = CourseForm()
    return render(request, "student/add_course.html", {"form": form})


def edit_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            updated_course = form.save()
            return HttpResponseRedirect(reverse("course_page", args=(updated_course.id,)))
    form = CourseForm(instance=course)

    return render(request, "student/edit_course.html", {"form": form, "course": course})


def remove_course(request, id):
    course = get_object_or_404(Course, pk=id)
    
    if request.method == "POST":
        course.delete()
        return HttpResponseRedirect(reverse("course_list"))
    
    return render(request, "student/remove_course.html", {"course": course})


def new_advisor(request):
    if request.method == "POST":
        form = AdvisorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("advisor_list"))
    else:
        form = AdvisorForm()

    return render(request, "student/add_advisor.html", {"form": form})


def edit_advisor(request, id):
    advisor = get_object_or_404(Advisor, pk=id)

    if request.method == "POST":
        # Bind the POST with the current advisor instance
        form = AdvisorForm(request.POST, instance=advisor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("advisor_detail", args=(advisor.id,)))
    else:
        # Pre-populate form with advisor instance data
        form = AdvisorForm(instance=advisor)

    return render(request, "student/edit_advisor.html", {"form": form, "advisor": advisor})


def add_student_to_course(request, id):
    student_obj = get_object_or_404(Student, pk=id)
    
    if request.method == "POST":
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            # Accessing the data from the 'course' field of the form
            course = form.cleaned_data['course']
            # Check if student already registered for course
            if course in student_obj.courses.all():
                message = f"You've already registered for '{course.subject}'"
                context = {"message": message, "student": student_obj}
                return render(request, 'student/duplicate_course.html', context)
            
            course.students.add(student_obj)
            # course.save()
            return HttpResponseRedirect(reverse('student_page', args=(student_obj.id,)))
    else:
        form = CourseSelectionForm()
        
    context = {"form": form, "student": student_obj}
    return render(request, "student/add_student_to_course.html", context)


def deactivate_student(request, id):
    student_obj = get_object_or_404(Student, pk=id)
    student_obj.active = False
    student_obj.save()
    messages.success(request, f'Student {student_obj.fname} {student_obj.lname} has been deactivated.')
    return HttpResponseRedirect(reverse('index'))
