import time
from django.views import View, generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse
import json
from django.core import serializers
from . import models
from . import forms
from django.forms import modelformset_factory
# Create your views here.


class ClothesRegisterView(generic.CreateView):
	form_class = forms.ClothesForm
	template_name = 'closet/clothes_form.html'


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.title = self.object.color + self.object.category
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())


def clothes_reg(request):
	form = forms.ClothesForm()
	formset = forms.Clothes_Formset(queryset=models.Clothes.objects.none())
	if request.method == 'POST':
		formset = forms.Clothes_Formset(request.POST, request.FILES, queryset=models.Clothes.objects.none())
		if formset.is_valid():
			clothes = formset.save(commit=False)
			for piece in clothes:
				piece.user = request.user
				piece.photo = get_object_or_404(models.Photo, pk=piece.photoid)
				piece.save()
			return HttpResponseRedirect(reverse('closet:closet'))
	return render(request, 'closet/clothes_form.html', {'formset':formset})


def closet(request):
	form = forms.ClothesForm()
	return render(request, "closet/closet.html", {'form':form, 'closet':closet})


def closet2(request):
	cg_list = request.GET.getlist('cg_checked', None)
	ss_list = request.GET.getlist('ss_checked', None)
	co_list = request.GET.getlist('co_checked', None)
	pt_list = request.GET.getlist('pt_checked', None)
	q_objects1 = Q()
	q_objects2 = Q()
	q_objects3 = Q()
	q_objects4 = Q()
	print(cg_list)
	if cg_list:
		for item in cg_list:
			q_objects1.add(Q(category__icontains=item), Q.OR)
		closet2 = models.Clothes.objects.filter(q_objects1)
		print(cg_list)
	if ss_list:
		for item in ss_list:
			q_objects2.add(Q(season__icontains=item), Q.OR)
		print(ss_list)	
	if co_list:
		for item in co_list:
			q_objects3.add(Q(color__icontains=item), Q.OR)
	if pt_list:
		for item in pt_list:
			q_objects4.add(Q(pattern__icontains=item), Q.OR)

	closet = models.Clothes.objects.filter(q_objects1).filter(q_objects2).filter(q_objects3).filter(q_objects4)
		
	values_list = list(closet.values())
	data = {
            "values_list" : values_list
    }
	return JsonResponse(data)


def ootdview(request):
	form = forms.ClothesForm()
	clothes = models.Clothes.objects.all()
	return render(request, 'closet/ootd.html', {'form':form, 'clothes':clothes})


class ClosetView(generic.ListView):
	model = models.Clothes
	context_object_name="closet"
	template_name = "closet/closet.html"

	def get_queryset(self):
		if not self.request.user.is_superuser:
			return self.model.objects.filter(user=self.request.user)
		return self.model.objects.all()


class DetailView(generic.DetailView):
	model = models.Clothes
	template_name = "closet/clothes_info.html"


class BasicUploadView(View):
    def get(self, request):
        photos_list = models.Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = forms.PhotoForm(self.request.POST, self.request.FILES)
        print("here1")
        if form.is_valid():
            photo = form.save()
            print("did it add?")
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url, 'photo_id': photo.id}
        else:
        	print("it's here")
        	data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))

