from django.contrib import admin
#Estos he añadido
from .resources import CensusResources
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#Hasta aqui
from .models import Census
from django.shortcuts import render
from django.db import IntegrityError


#class CensusAdmin(admin.ModelAdmin):
#    list_display = ('voting_id', 'voter_id')
#    list_filter = ('voting_id', )
#
#    search_fields = ('voter_id', )

#Metodo para exportar
def export_selected(modeladmin, request, queryset):
	#LLamo a censusResource para exportarlo despues
	census_resource = CensusResources()
	#Exporto los censos seleccionados
	dataset = census_resource.export(queryset)
	#Creo una respuesta http con los censos en excel
	response = HttpResponse (dataset.xls, content_type='text/xls')
	#Pongo a disposicion el excel con el nombre census.xls
	response['Content-Disposition'] = 'attachment; filename="census.xls"'
	#Devuelvo la respuesta del metodo
	return response
#Le pongo un nombre para que salga en la lista de acciones
export_selected.short_description = 'Export selected as xls'

def reutVoting(modeladmin, request, queryset):
	if 'apply' in request.POST: 	
		modeladmin.message_user(request, "Created new censuss")          	
		for q in queryset:
			census = Census(voting_id=request.POST.get("selected_voting_id"), voter_id=q.voter_id)
			try:			
				census.save()
			except IntegrityError:
				empty = lambda: None	
		return HttpResponseRedirect(request.get_full_path())
	return render(request, 'order_intermediate.html', context={'censuss': queryset})

reutVoting.short_description = 'Reuse censuss in another voting'

def reutVoter(modeladmin, request, queryset):
	if 'apply' in request.POST: 	
		modeladmin.message_user(request, "Created new censuss")          	
		for q in queryset:
			census = Census(voting_id=q.voting_id, voter_id=request.POST.get("selected_voting_id"))
			try:			
				census.save()
			except IntegrityError:
				empty = lambda: None	
		return HttpResponseRedirect(request.get_full_path())
	return render(request, 'reuseVoter.html', context={'censuss': queryset})

reutVoter.short_description = 'Reuse censuss for a voter'

def removeVoterAllCensus(modeladmin, request, queryset):
	if 'yes' in request.POST: 	
		modeladmin.message_user(request, "Voter/s deleted")          	
		for q in queryset:
			for c in Census.objects.all():
				if c.voter_id==q.voter_id:
					c.delete()
	
				
		return HttpResponseRedirect(request.get_full_path())
	if'no' in request.POST:
		return HttpResponseRedirect(request.get_full_path())
	return render(request, 'removeVoter.html', context={'censuss': queryset})

removeVoterAllCensus.short_description = 'Remove voter/s from all censuss'


#Cambié la entrada del census admin para añadir el boton import/export
class CensusAdmin(ImportExportModelAdmin):
	#Se añade esta linea para añadir los botones import/export
	resource_class = CensusResources
	list_display = ('voting_id', 'voter_id')
	list_filter = ('voting_id', )

	search_fields = ('voter_id', )
	#Se añade el metodo de export a la lista de acciones de django
	actions = [export_selected, reutVoting, reutVoter, removeVoterAllCensus]

admin.site.register(Census, CensusAdmin)
