from django import forms

g=[('male','MALE'),('female','FEMALE')]


c=[('python','python'),('django','django'),('api','api'),('selenium','selenium')]


class RegistrationForm(forms.Form):
    Name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)

    #choose one element using dropdown list
    #gender=forms.ChoiceField(choices=g)

    #choose one input element by using radioselect
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)

    #choose multiple input elements by using dropdown list
    #courses=forms.MultipleChoiceField(choices=c)

    #choose multiple input element by using checkbox
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)