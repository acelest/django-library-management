from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Livre, User

class RegistrationForm(UserCreationForm):
    ville = forms.CharField(
        label='Ville',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'})
    )
    age = forms.IntegerField(
        label='Âge',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Âge'})
    )
    sexe = forms.ChoiceField(
        label='Sexe',
        choices=[('male', 'Homme'), ('female', 'Femme')],
        widget=forms.RadioSelect
    )
    photo = forms.ImageField(
        label='Photo de profil',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User  
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'ville', 'age', 'sexe', 'photo')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field_name != 'sexe' and field:
                field.widget.attrs.update({'class': 'form-control'})

# def __init__(self, *args, **kwargs):
# 		super(RegistrationForm, self).__init__(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
# 		self.fields['username'].label = ''
# 		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

# 		self.fields['password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
# 		self.fields['password1'].label = ''
# 		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

# 		self.fields['password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
# 		self.fields['password2'].label = ''
# 		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



class LivreForm(forms.ModelForm):
    nom = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'})
    )
    auteur = forms.CharField(
        label='Auteur',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur'})
    )
    pages = forms.IntegerField(
        label='Pages',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pages'})
    )
    categorie = forms.CharField(
        label='Catégorie',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Catégorie'})
    )
    image = forms.ImageField(
        label='Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Livre
        fields = ('nom', 'auteur', 'pages', 'categorie', 'image')



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'})
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )

  
