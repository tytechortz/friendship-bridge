from django.shortcuts import render, redirect, HttpResponse
from .models import Member
from .forms import MemberForm

# Create your views here.



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