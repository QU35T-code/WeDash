from django import forms

# To do : Remove this here
class Lyrics(forms.Form):
    author = forms.CharField(label="author", help_text="Enter an author", max_length=30, required=True)
    song = forms.CharField(label="song", help_text="Enter a song", max_length=30, required=True)
    def clean(self):
        cleaned_data = super(Lyrics, self).clean()
        author = cleaned_data.get('author')
        song = cleaned_data.get('song')
        if not author or not song:
            raise forms.ValidationError('You have to write something!')

class SettingsOptions(forms.Form):
    mail = forms.BooleanField(required=False)
    sms = forms.BooleanField(required=False)
    sound = forms.BooleanField(required=False)
    cmode = forms.BooleanField(required=False)
    dmode = forms.BooleanField(required=False)

class ProfilOptions(forms.Form):
    username = forms.CharField(max_length=50, required=True, initial="test")
    lastname = forms.CharField(max_length=50, required=False)
    firstname = forms.CharField(max_length=50, required=False)
    email = forms.CharField(max_length=50, required=True)
    phone = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)
    country = forms.CharField(max_length=50, required=False)