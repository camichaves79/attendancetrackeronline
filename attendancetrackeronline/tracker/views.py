from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.shortcuts import render
from .forms import FileUploadForm
from .utilities import add_time

def index(request):
    return HttpResponse("This is where the tracker will be.")

def tracker(request):
    Student.objects.all().delete()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file'] 
            uploaded_file = uploaded_file.read() 
            uploaded_file = uploaded_file.decode()
            line = uploaded_file.replace("\r", "").split("\n")
        students = []
        for instruction in line:
            student_to_update = ""
            if instruction:
                instruction_set = instruction.split(" ")
                student_name = instruction_set[1]
                if instruction_set[0] == "Student":
                    student = Student.objects.filter(pk=student_name).first()
                    if not student:
                        student = Student.objects.create(pk=student_name, minutes=0, days=[])
                elif instruction_set[0] == "Presence":
                    student_to_update = Student.objects.filter(pk=student_name).first()
                    if student_to_update:
                        student_to_update.minutes += add_time(instruction_set[3],instruction_set[4])
                        if instruction_set[2] not in student_to_update.days:
                            student_to_update.days.append(instruction_set[2])
                            student_to_update.days_count += 1    
                        student_to_update.save()
                    else:
                        continue
            students = Student.objects.all()
            students = sorted(students, key=lambda student: student.minutes, reverse=True)
            
        context = {
            "students": students
        }
        return render(request, 'results.html', context)
    else:
        form = FileUploadForm()
    
    return render(request, 'form.html', {'form': form})
