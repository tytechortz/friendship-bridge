from django.shortcuts import render, redirect, HttpResponse
from .models import Member
from .forms import MemberForm
from tablib import Dataset



# Create your views here.

def simple_upload(request):
    if request.method == 'POST':
        member_resource = MemberResource()
        dataset = Dataset()
        new_members = request.FILES['myfile']

        imported_data = dataset.load(new_memberss.read())
        result = member_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            member_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')


def core_email(request):
    core_email = Member.objects.filter(member_type='Core')
    print(core_email)
    return render(request, 'members/core_members.html', {'members': core_email})

def core_members(request):
    core_members = Member.objects.filter(member_type='Core')
    return render(request, 'members/core_members.html', {'members': core_members})

def outer_core_members(request):
    outer_core_members = Member.objects.filter(member_type='Outer Core')
    return render(request, 'members/outer_core_members.html', {'members': outer_core_members})

def event_members(request):
    event_members = Member.objects.filter(member_type='Events')
    return render(request, 'members/event_members.html', {'members': event_members})

def member_list(request):
    members = Member.objects.order_by('last_name')
    return render(request, 'members/member_list.html', {'members': members})

def member_detail(request, pk):
    #pk is short for primary key, 
    member = Member.objects.get(id=pk)
    return render(request, 'members/member_detail.html', {'member': member})

def member_create(request):
  if request.method == 'POST':
    form = MemberForm(request.POST)
    if form.is_valid():
      member = form.save()
      return redirect('member_detail', pk=member.pk)
  else:
    form = MemberForm()
  return render(request, 'members/member_form.html', {'form': form})

def member_edit(request, pk):
  member = Member.objects.get(pk=pk)
  if request.method == 'POST':
    form = MemberForm(request.POST, instance=member)
    if form.is_valid():
      member = form.save()
      return redirect('member_detail', pk=member.pk)
  else:
    form = MemberForm(instance=member)
  return render(request, 'members/member_form.html', {'form': form})

# Member Delete
def member_delete(request, pk):
  Member.objects.get(id=pk).delete()
  return redirect('member_list')