from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Livre
from .forms import LivreForm, RegistrationForm, LoginForm

def home(request):
    livres = Livre.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Vous êtes connecté.')
            return redirect('home')
        else:  
            messages.error(request, 'Erreur de connexion, veuillez réessayer.')
            return redirect('login_user')
    else:
        return render(request, 'home.html', {'livres': livres})

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Utilisateur enregistré avec succès!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Email ou mot de passe incorrect')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté.")
    return redirect('home')

def add(request):
    form = LivreForm(request.POST, files=request.FILES)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Livre ajouté avec succès.')
                return redirect('home')
        return render(request, 'add.html', {'form': form})
    else:
        messages.error(request, 'Vous devez être connecté.')
        return redirect('home')

def supprimer(request, livre_id):
    if request.user.is_authenticated:
        livre = Livre.objects.get(id=livre_id)
        livre.delete()
        messages.success(request, 'Livre supprimé avec succès.')
        return redirect('home')
    else:
        messages.error(request, 'Vous devez être connecté pour effectuer cette action.')
        return redirect('home')



def delete_livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    livre.delete()
    return redirect('liste_livres')

def modifier(request, livre_id):
    if request.user.is_authenticated:
        livre = Livre.objects.get(id=livre_id)
        form = LivreForm(request.POST or None, request.FILES or None, instance=livre)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,'Livre mis à jour avec succès.')
                return redirect('home')
        return render(request, 'modifier.html', {'form': form})
    else:
        messages.error(request, 'Désolé, veuillez vous connecter.')
        return redirect('home')

def search(request):
    mot_cle = request.GET.get('mot_cle', '')
    livres = Livre.objects.filter(nom__icontains=mot_cle)
    return render(request, 'search.html', {'livres': livres})
