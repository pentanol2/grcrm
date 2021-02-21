from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead,SalesAgents
from .forms import LeadForm,LeadModelForm

#view: landing page
def landing_page(request):

    return render(request,'landing.html')

# view : lead_list
def lead_list(request):
    #return HttpResponse('Hello World!')
    leads = Lead.objects.all()
    context = {
        'leads':leads
    }
    return render(request, 'lead_list.html', context)

#view : lead detail
def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        'lead': lead
    }
    return render(request, 'lead_detail.html', context)

#view a form to create leads
'''
def lead_create(request):
    form = LeadForm()
    print(request.POST)
    if request.method == 'POST':
        print('Recieving a post request!')
        form = LeadForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = SalesAgents.objects.first()
            Lead.objects.create(
                first_name = first_name ,
                last_name = last_name ,
                age = age ,
                agent = agent
            )
            return redirect('/leads')

    context = {
        'form' : form
    }
    return render(request,'lead_create.html',context)
'''
def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        'form': form
    }
    return render(request, 'lead_create.html', context)

def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        'lead':lead,
        'form':form
    }
    return render(request, 'lead_update.html', context)

'''
def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm()
    form.data(lead)
    print(request.POST)
    if request.method == 'POST':
        print('Recieving a post request!')
        form = LeadForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = SalesAgents.objects.first()
            lead.first_name=first_name
            lead.last_name=last_name
            lead.age=age
            lead.agent=agent
            lead.save()

            return redirect('/leads')

    context= {
        'lead':lead,
        'form':form
    }
    return render(request, 'lead_update.html',context)
'''
def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')