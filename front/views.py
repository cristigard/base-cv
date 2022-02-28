from django.shortcuts import render
from users.models import CustomUser
from .forms import SkillForm, LanguageForm, WorkForm, EducationForm, ObjectiveForm,AboutForm
from .models import Skill, Language, Work, Education, Objective, About
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.


def home(request):
	return render(request, 'front/home.html')


def cv(request, tk):
	cv_owner = request.path
	cv_owner = cv_owner.replace('/','')
	data = get_object_or_404(CustomUser, tk=tk)
	# data = CustomUser.objects.all().get(tk = tk)
	return render(request, 'front/index.html',{'data':data ,'cv_owner':cv_owner })

@login_required
def skills(request):
	skill_form = SkillForm()
	if request.method == 'POST' or None:
		if "skill" in request.POST:
			skill_form  = SkillForm(request.POST)
			if skill_form.is_valid():
				Skill(author = request.user, sk = request.POST.get("sk"),percent = request.POST.get("percent")).save()
				skill_form = SkillForm()
		if "delete" in request.POST:
			skill_id = request.POST.get("skill.id")
			Skill.objects.get(id=skill_id).delete()

	return render(request, 'front/skills.html',{'skill_form': skill_form})

@login_required
def language(request):
	language_form = LanguageForm()
	if request.method == 'POST' or None:
		if "language" in request.POST:
			language_form  = LanguageForm(request.POST)
			if language_form.is_valid():
				Language(author = request.user, lg = request.POST.get("lg"),percent = request.POST.get("percent")).save()
				language_form = LanguageForm()
		if "delete" in request.POST:
			language_id = request.POST.get("language.id")
			Language.objects.get(id=language_id).delete()

	return render(request, 'front/languages.html',{'language_form': language_form})





@login_required
def work(request):
	work_form = WorkForm()
	if request.method == 'POST' or None:
		if "work" in request.POST:
			work_form  = WorkForm(request.POST)
			if work_form.is_valid():
				work_form.cleaned_data['author']=request.user
				Work.objects.create(**work_form.cleaned_data)
				work_form = WorkForm()
		if "delete" in request.POST:
			work_id = request.POST.get("work.id")
			Work.objects.get(id = work_id).delete()

	return render(request, 'front/works.html',{'work_form': work_form})






# @login_required
# def work(request):
# 	work_form = WorkForm()
# 	if request.method == 'POST' or None:
# 		if "work" in request.POST:
# 			work_form  = WorkForm(request.POST)
# 			if work_form.is_valid():
# 				Work(author = request.user, 
# 					work_description = request.POST.get("work_description"),
# 					position = request.POST.get("position"),
# 					company = request.POST.get("company"),
# 					location = request.POST.get("location"),
# 					start_date = request.POST.get("start_date"),
# 					end_date = request.POST.get("end_date")).save()
# 				work_form = WorkForm()
# 		if "delete" in request.POST:
# 			work_id = request.POST.get("work.id")
# 			Work.objects.get(id = work_id).delete()

# 	return render(request, 'front/works.html',{'work_form': work_form})

@login_required
def education(request):
	education_form = EducationForm()
	if request.method == 'POST' or None:
		if "education" in request.POST:
			education_form  = EducationForm(request.POST)
			if education_form.is_valid():
				Education(author = request.user, 
					institution_name = request.POST.get("institution_name"),
					degree = request.POST.get("degree"),
					location = request.POST.get("location"),
					graduation_year = request.POST.get("graduation_year"),
					description = request.POST.get("description")).save()
				education_form = WorkForm()
		if "delete" in request.POST:
			education_id = request.POST.get("education.id")
			Education.objects.get(id = education_id).delete()

	return render(request, 'front/education.html',{'education_form': education_form})


@login_required
def objective(request):
	objective_form = ObjectiveForm()
	if request.method == 'POST' or None:
		if "objective" in request.POST:
			objective_form  = ObjectiveForm(request.POST)
			if objective_form.is_valid():
				Objective(author = request.user, description = request.POST.get("description")).save()
				objective_form = ObjectiveForm()
		if "delete" in request.POST:
			objective_id = request.POST.get("objective.id")
			Objective.objects.get(id = objective_id).delete()

	return render(request, 'front/objective.html',{'objective_form': objective_form})

@login_required
def about(request):
	about_form = AboutForm()
	if request.method == 'POST' or None:
		if "about" in request.POST:
			about_form  = AboutForm(request.POST)
			if about_form.is_valid():
				About(author = request.user, description = request.POST.get("description")).save()
				about_form = AboutForm()
		if "delete" in request.POST:
			about_id = request.POST.get("about.id")
			About.objects.get(id = about_id).delete()

	return render(request, 'front/about.html',{'about_form': about_form})