# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Analogform

from datetime import datetime
from datetime import timedelta

#formulario = Analogform()

def parametros_analisis(request):
    if request.method == 'POST':
        formulario = Analogform(request.POST)
        if formulario.is_valid():
            inten_lim = formulario.cleaned_data['intentos']
            inter_lim = formulario.cleaned_data['intervalo']
            #context= {"f_intentos":inten_lim, "f_intervalo":inter_lim}
            informe= repetidos(request,inten_lim, inter_lim)
            return render (request, 'ver_para.html',informe)
            #return render(request,'ver_para.html', context)
    else:
        #informe={}
        formulario = Analogform()
    #return render (request, 'ver_para.html',informe)
    return render(request, 'intro_para.html',{'formulario': formulario })

#def parametros_confirma(request,"formulario.cleaned_data['intentos']","formulario.cleaned_data['intervalo']"):
# def parametros_confirma(request):
#     formulario = Analogform(request.POST)
#     f_intentos= formulario.
#     context= {"f_intentos":formulario.cleaned_data.get('intentos'),
#             "f_intervalo": formulario.cleaned_data.get('intervalo')
#             }
#     return render(request, 'ver_para.html', context)

def ana():
	f = open ('/auth.log', 'r')
	ha={}
	for lin in f.readlines():
	    	if 'authentication failure' in lin:
			li=lin.split()
			sfe = li[0]+li[1]+li[2]
			fe = datetime.strptime(sfe,'%b%d%H:%M:%S')
			for ele in li:
				if 'rhost' in ele:
					ip = ele[6:]
			if ip not in ha:
				ha[ip]=[]
			ha[ip].append(fe)
	f.close()
	for ip in ha:
		ha[ip].sort(reverse=True)
	return ha

# y el request ºjº
def repetidos(request, inten,intervalo):
	todo=ana()
    # una linea
	informe_html =["Inicio informe",""]

	for punte in todo:
		informe_html.append('\n\tAnálisis de la Ip : '+ punte+ '\n')
		i=0
		for conexion in todo[punte]:
			informe_html.append('    '+punte+' conectó el '+str(conexion))
			#print(todo[punte][i]-conexion)
			#informe_html.append(timedelta.total_seconds(todo[punte][i]-conexion))
			if (timedelta.total_seconds(todo[punte][i]-conexion) <= intervalo*60):
				informe_html.append('Analizando conexión : '+str(conexion))
				Intento=0
				for SigueComprobando in todo[punte]:
					informe_html.append(str(todo[punte][i])+' --- '+str(SigueComprobando))
					Diferencia = timedelta.total_seconds(todo[punte][i]-SigueComprobando)
					if (Diferencia>0 and Diferencia <= intervalo*60 and Intento<=inten):
						Intento+=1
						informe_html.append('\n'+'Intento núm. : '+str(Intento)+ ' en : '+ str(todo[punte][i]-SigueComprobando))

				i+=1
	print('\n\nSe repite: '+str(inten) + ' en minutos: '+str(intervalo))
	informe_html.append("Fin informe")
	return ({'informe':informe_html})
#	return render (request, 'ver_para.html',{'informe':informe_html})

#
#
#
#	return HttpResponse("hola desde repetidos")

#	return HttpResponse(informe_html)
	#
