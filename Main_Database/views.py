from locale import currency
from multiprocessing import context
from django.shortcuts import render,redirect
from . models import ActivityDetail, AddParticipant,Participant,Poll,Post
from .forms import ParticipantForm,CreatePollForm,CreateActivityForm,CreateOrganizationForm,CreateProjectForm,CreateParrticipantForm
from django.views.generic import ListView,DetailView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import pandas as pd
from django.views.generic import ListView, DetailView,CreateView
# Create your views here.
class ActivityView(ListView):
    model=AddParticipant
    template_name='all_activity.html'

def Activities(request):
    alld=AddParticipant.objects.all()
    return render(request,'activities_folder/all_activities.html',{'alld':alld})
 
    
def add_participant(request,pk):
    activity_name=AddParticipant.objects.get(pk=pk)

    participants=Participant.objects.filter(activity=activity_name)
    form= ParticipantForm(request.POST or None)

    if request.method=='POST':
        if form.is_valid():
            form.save()
            participant=form.save(commit=False)
            participant.activity=activity_name
            participant.save()
   

            return redirect('participant-detail',pk=participant.id)

        else:
            return render(request,'activities_folder/partial/participant_form.html',{form:form})


    context={
        'formset':form,
        'detail':activity_name,
        'participants':participants
    }


    return render(request,'activities_folder/add_participant.html', context)

def home(request):
    all_data=Participant.objects.all().values()
    df=pd.DataFrame(all_data)
    
    return render(request,'home.html',{'df':df.to_html})
def create_activity_form(request):
    form=ParticipantForm()
    return render(request,'activities_folder/partial/participant_form.html',{'form':form})


def detail_participant(request,pk):


    participant=Participant.objects.get(pk=pk)
    return render(request,'activities_folder/partial/participant_detail.html',{'participant':participant})
def register_participant(request,pk):
    participant=Participant.objects.get(pk=pk)
    participant.save()

    return render(request,'activities_folder/registered_participant.html',{'participant':participant})
def update_participant(request,pk):
    participant=Participant.objects.get(pk=pk)
    form=ParticipantForm(request.POST or None,instance=participant)

    if request.method=='POST':
        if form.is_valid():
            form.save()
            participant=form.save(commit=False)        
            return redirect('participant-detail',pk=participant.id)

    context={
        'form':form,
        'participant':participant
    }
    return render(request,'activities_folder/partial/participant_form.html',context)
def delete_participant(request,pk):
    participant=Participant.objects.get(pk=pk)
    participant.delete()
    return HttpResponseRedirect('')

def homepoll(request):
    polls=Poll.objects.all()
    return render(request,'poll/home.html', {'polls':polls})
def create_poll(request):
    if request.method== 'POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-poll')
        
    else:

        form=CreatePollForm()
    context={
        'form':form
    }
    return render(request,'poll/create_poll.html',context)

def result_poll(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request,'poll/result_poll.html',context)

def vote_poll(request,poll_id):

    poll = Poll.objects.get(pk=poll_id)
    polls=Poll.objects.get(pk=poll_id)
  
    if request.method == 'POST':
      
        selected_option = request.POST['poll']
        
        if selected_option == 'option1':
            poll.option_one_count += 1
            
        elif selected_option == 'option2':
            poll.option_two_count += 1
            
        elif selected_option == 'option3':
            poll.option_three_count += 1
            
        elif selected_option == 'option4':
            poll.option_four_count += 1
            
        elif selected_option == 'option5':
            poll.option_five_count += 1
            
        elif selected_option == 'option6':
            poll.option_six_count += 1
           
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()
        

      
        
        return redirect('result-poll', poll.id)

    context = {
        'poll' : poll,
        'polls' : polls,
        
    }  
    
    return render(request,'poll/vote_poll.html',context)


# input fields

def homeinput(request):
    polls=Poll.objects.all()
    return render(request,'input_fields/home.html', {'polls':polls})

def register_activity(request):
    forms=CreateActivityForm
    if request.method== 'POST':
        forms=CreateActivityForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home-input')
        
    else:

        forms=CreateActivityForm()
    context={
        'forms':forms
    }
    return render(request,'input_fields/register_activity.html',context)

def register_project(request):
    forms=CreateProjectForm
    if request.method== 'POST':
        forms=CreateProjectForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home-input')
        
    else:

        forms=CreateProjectForm()
    context={
        'forms':forms
    }
    return render(request,'input_fields/register_project.html',context)

def register_organization(request):
    forms=CreateOrganizationForm
    if request.method== 'POST':
        forms=CreateOrganizationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home-input')
        
    else:

        forms=CreateOrganizationForm()
    context={
        'forms':forms
    }
    return render(request,'input_fields/register_organization.html',context)
def register_participant(request):
    alld=AddParticipant.objects.all()
    return render(request,'input_fields/register_participant.html',{'alld':alld})

class AddArticleView(CreateView):
    model=Post
    template_name='articles/add_article.html'
    fields='__all__'