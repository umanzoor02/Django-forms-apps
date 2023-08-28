from django import forms

class userforms(forms.Form):
    num1=forms.CharField(required=False, label='input1', max_length=10)
    num2=forms.CharField(required=False, label='input2', max_length=10)

class EvenOddform(forms.Form):
    num=forms.CharField(required=False, label='input1', max_length=10)


class Marksheet(forms.Form):
    sub1=forms.CharField(label='Subject1',widget=forms.TextInput(attrs={'class': 'subject-field'}))
    sub2=forms.CharField(label='Subject2',widget=forms.TextInput(attrs={'class': 'subject-field'}))
    sub3=forms.CharField(label='Subject3',widget=forms.TextInput(attrs={'class': 'subject-field'}))
    sub4=forms.CharField(label='Subject4',widget=forms.TextInput(attrs={'class': 'subject-field'}))
    sub5=forms.CharField(label='Subject5',widget=forms.TextInput(attrs={'class': 'subject-field'}))
    total=forms.CharField(label='Total Marks',widget=forms.TextInput(attrs={'class': 'subject-field'}))