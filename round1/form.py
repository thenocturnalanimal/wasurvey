from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, AccordionGroup, Accordion, TabHolder, Tab
from django import forms
from django.urls import reverse_lazy

yn=[('Y', 'Yes'),('N', 'No')]
ynm=[('Y', 'Yes'),('N', 'No'), ('X','Maybe')]
num=[(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
lik=[(0,'NO Chance (Definitely False)'),(1,'LOW chance'),(2,'LESS than 50% chance'),(3,'50-50 chance'),(4,'MORE than 50% chance'),(5,'HIGH chance'),(6, '100% chance (Definitely True)')]

class SurveyForm(forms.Form):
	iid=forms.IntegerField(label="",min_value=0)#Image ID ")
	gid=forms.IntegerField(label="",min_value=0)#Game ID ")
	uid=forms.IntegerField(label="",min_value=0)#User ID ")
	share=forms.ChoiceField(label="Would you like to share this story with participants in the next round? ", widget=forms.RadioSelect, choices=yn)
	reason=forms.CharField(label="", widget=forms.Textarea)
	recall=forms.ChoiceField(label="Do you recall seeing this story on social media (or elsewhere) before seeing it now, in the lab? ",
		widget=forms.RadioSelect, choices=ynm)
	likely=forms.ChoiceField(label="How likely do you think the story above is true? ",
		widget=forms.RadioSelect, choices=lik)
	nextp=forms.ChoiceField(label="There are 5 participants in the next round. How many of them, do you think, have seen this story before? ",
		choices=num)


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

#		self.helper=FormHelper
#		self.helper.form_method='post'
		
#		super(SurveyForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.form_id = 'id-survey-data-form'
		self.helper.form_method='post'
#		self.helper.form_action = reverse_lazy('submit')
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
		self.helper.form_class = 'form-horizontal'
		self.helper.layout = Layout(
			Accordion(
				AccordionGroup('IDs', 
					TabHolder(Tab('Image ID', 'iid'),Tab('Game ID', 'gid'),Tab('User ID', 'uid'))),
				AccordionGroup('Why did you choose to share/not share the picture?',
						InlineRadios('share'),
						Div('reason')),
#			Fieldset('Contact data', 'email', 'phone', style="color: brown;"),
				AccordionGroup('Additonal Info',
					InlineRadios('recall'),
					InlineRadios('likely'),
					Fieldset('Next', 'nextp'))))
#			AccordionGroupHolder(AccordionGroup('Address', 'address'),AccordionGroup('More Info', 'more_info')))