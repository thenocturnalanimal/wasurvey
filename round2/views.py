from django.shortcuts import render
from django.http import HttpResponse
from .form import SurveyForm

# Create your views here.
def survey(request):
	
	if request.method == 'POST':
		form = SurveyForm(request.POST)
		if form.is_valid():

			iid=form.cleaned_data['iid']
			gid=form.cleaned_data['gid']
			uid=form.cleaned_data['uid']
			share=form.cleaned_data['share']
			reason=form.cleaned_data['reason']
			recall=form.cleaned_data['recall']
			likely=form.cleaned_data['likely']
			nextp=form.cleaned_data['nextp']
			
			final=str(iid)+','+str(gid)+','+str(uid)+','+str(share)+','+str(reason)+','+str(recall)+','+str(nextp)+','+str(likely)

			print(final)
			file=open('round2-responses.csv', 'a')
			file.write("\n")
			file.write(final)
			file.close()

	form = SurveyForm()

	return render(request, 'form.html', {'form': form})