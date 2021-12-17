from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pedal, Guitar
from .forms import CheckedForm


# class Pedal:
#     def __init__(self, name, brand, description, type, year):
#         self.name = name
#         self.brand = brand
#         self.description = description
#         self.type = type
#         self.year = year

# pedals = [
#     Pedal('Dark Sun', 'Seymour Duncan', 'Dark Sun combines a warm and clean digital delay algorithm with a lush Hall reverb, and the ability to route the two in just about any configuration you could want.', 'Digital Delay + Reverb', 2019),
#     Pedal('Terraform', 'Wampler', '11 custom designed effects blocks, from Flanger to Phaser, Chorus to U-Vibe, Harmonic Tremolo to Envelope Filter, you know everything about it is going to be perfect.', 'Modulation', 2019),
#     Pedal('Cali76 - Stacked Edition', 'Origin Effects', 'The Cali76 Stacked Edition takes compression effect to the next level literally, by stacking two layers of FET compressors in one stompbox.', 'Compressor', 2019)
# ]        

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def pedals_index(request):
    pedals = Pedal.objects.filter(user=request.user)
    return render(request, 'pedals/index.html', { 'pedals': pedals}) 

@login_required
def pedals_detail(request, pedal_id):
    pedal = Pedal.objects.get(id=pedal_id)
    guitars_pedal_doesnt_have = Guitar.objects.exclude(id__in = pedal.guitars.all().values_list('id'))

    checked_form = CheckedForm()
    return render(request, 'pedals/detail.html', {
        'pedal' : pedal, 'checked_form': checked_form,
        'guitars' : guitars_pedal_doesnt_have

    })

@login_required
def add_checked(request, pedal_id):
    # create a ModelForm instance using the data in request.POST
    form = CheckedForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_checked = form.save(commit=False)
        new_checked.pedal_id = pedal_id  
        new_checked.save()
    return redirect('detail', pedal_id=pedal_id)      

class PedalCreate(LoginRequiredMixin, CreateView):
    model = Pedal
    fields = ['name', 'brand', 'description', 'type', 'year']
    # success_url = '/pedals/'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class PedalUpdate(LoginRequiredMixin, UpdateView):
    model =  Pedal
    fields = ['name', 'brand', 'description', 'type', 'year']    #//or the fields wanted

class PedalDelete(LoginRequiredMixin, DeleteView):
    model = Pedal
    success_url = '/pedals/'





class GuitarList(LoginRequiredMixin, ListView):
  model = Guitar

class GuitarDetail(LoginRequiredMixin, DetailView):
  model = Guitar

class GuitarCreate(LoginRequiredMixin, CreateView):
  model = Guitar
  fields = ['name', 'description']

class GuitarUpdate(LoginRequiredMixin, UpdateView):
  model = Guitar
  fields = ['name', 'description']

class GuitarDelete(LoginRequiredMixin, DeleteView):
  model = Guitar
  success_url = '/guitars/'   

@login_required
def assoc_guitar(request, pedal_id, guitar_id):
    # Note that you can pass a guitar's id instead of the whole object
    Pedal.objects.get(id=pedal_id).guitars.add(guitar_id)
    return redirect('detail', pedal_id=pedal_id)  

@login_required
def unassoc_guitar(request, pedal_id, guitar_id):
  Pedal.objects.get(id=pedal_id).guitars.remove(guitar_id)
  return redirect('detail', pedal_id=pedal_id)    


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  