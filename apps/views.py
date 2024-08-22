from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .forms import imagesForm
from .models import Program, Category, Stage, Student, Result, Team, Image
from django.db.models import Q


def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        students = Student.objects.filter(multiple_q)
        
        if students.count() > 1:
            return render(request, 'apps/students.html', {'students': students}) 
        elif students.count() == 1:
            return render(request, 'apps/student_detail.html', {'student': students.first()})  
        else:
            return redirect('home')  
    else:
        return render(request, 'apps/home.html')  

def destino(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        students = Student.objects.filter(multiple_q)
        
        if students.count() > 1:
            return render(request, 'apps/students.html', {'students': students}) 
        elif students.count() == 1:
            return render(request, 'apps/student_detail.html', {'student': students.first()})  
        else:
            return redirect('destino')  
    else:
        return render(request, 'apps/destino.html')

def students(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        students = Student.objects.filter(multiple_q)
        
        if students.count() > 1:
            return render(request, 'apps/students.html', {'students': students})
        elif students.count() == 1:
            return render(request, 'apps/student_detail.html', {'student': students.first()})
        else:
            students = Student.objects.all()
            return render(request, 'apps/students.html', {'students': students})
    else:
        students = Student.objects.all()
    return render(request, 'apps/students.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'apps/student_detail.html', context)
def programs(request):
    if 'q' in request.GET:
        q = request.GET['q']
        programs = Program.objects.filter(name__icontains=q)
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
            students = Student.objects.filter(multiple_q)
        
            if students.count() > 1:
                return render(request, 'apps/students.html', {'students': students})
            elif students.count() == 1:
                return render(request, 'apps/student_detail.html', {'student': students.first()})
    else:
        programs = Program.objects.all()
    return render(request, 'apps/programs.html', {'programs': programs})

def stages(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        students = Student.objects.filter(multiple_q)
        
        if students.count() > 1:
            return render(request, 'apps/students.html', {'students': students})
        elif students.count() == 1:
            return render(request, 'apps/student_detail.html', {'student': students.first()})
        else:
            stages = Stage.objects.all()
            return render(request, 'apps/stages.html', {'stages': stages})
    else:
        stages = Stage.objects.all()
        return render(request, 'apps/stages.html', {'stages': stages})

def categories(request):
    if 'q' in request.GET:
        q = request.GET['q']
        categories = Category.objects.filter(name__icontains=q)
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
            students = Student.objects.filter(multiple_q)
        
        if students.count() > 1:
            return render(request, 'apps/students.html', {'students': students})
        elif students.count() == 1:
            return render(request, 'apps/student_detail.html', {'student': students.first()})
        else:
            categories = Category.objects.all()
            return render(request, 'apps/category_details.html', {'categories': categories})
    else:
        categories = Category.objects.all()
        return render(request, 'apps/category_details.html', {'categories': categories})



def teams(request):
    teams = Team.objects.all()  # Get all teams
    students = Student.objects.all()  # Get all students
    
    # Create a dictionary to map team names to their students
    team_students = {team.name: [] for team in teams}
    for student in students:
        if student.team.name in team_students:
            team_students[student.team.name].append(student)
    
    # Add empty lists for teams with no students
    for team in teams:
        if team.name not in team_students:
            team_students[team.name] = []
    
    # Divide teams into four groups
    team_list = list(team_students.items())
    num_teams = len(team_list)
    
    # Handle the case when there are no teams
    if num_teams == 0:
        split_teams = []
    else:
        # Ensure that the step value is not zero
        step = max(1, (num_teams + 3) // 4)
        split_teams = [team_list[i:i + step] for i in range(0, num_teams, step)]
    
    context = {'split_teams': split_teams}
    return render(request, 'apps/teams.html', context)



def results(request):
    results = Result.objects.all()
    teams = Team.objects.all().order_by('-points').values()
    return render(request, 'apps/results.html', {'results': results,'teams':teams})


def upload_image(request):
    if request.method == 'POST':
        form = imagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = imagesForm()
    return render(request, 'apps/upload_image.html', {'form': form})


def success(request):
    return render(request, 'apps/success.html')

def images(request,pk):
    image = images.objects.get(pk)  # Example: fetching by primary key
    return render(request, 'my_template.html', {'image': image})

def about_us(request):
    return render(request, 'apps/about_us.html')

def contact_us(request):
    return render(request, 'apps/contact_us.html')

def submit_contact(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # You can add logic to save the message or send an email here
        
        return HttpResponse("Thank you for contacting us!")
    return redirect('contact_us')

