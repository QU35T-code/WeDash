from django import forms

SUBJECTS_CHOICES =(
    ("[SUPPORT][BUG] -- Ticket #", "I have a problem with a bug"),
    ("[SUPPORT][CONNECTION] -- Ticket #", "I have a problem logging in"),
    ("[SUPPORT][WIDGETS] -- Ticket #", "I have a problem with one or more widgets"),
    ("[SUPPORT][OTHER] -- Ticket #", "Other"),
)

class ContactForm(forms.Form):
    subject = forms.ChoiceField(choices=SUBJECTS_CHOICES, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)