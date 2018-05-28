#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Analog con análisis de repeticiones.
# 1º ASIR-LM Juan Pablo Civila
# Uso print() por compatibilidad con Python 3

from datetime import datetime
from datetime import timedelta


def menu():
	nofin=True
	while nofin:
		print('\n'+50*'=')
		print(' \t M E N Ú - principal ')
		print(50*'=')
		print('Análisis de conexiones fallidas al sistema (auth.log)')
		print(30*'-')
		print('1- Todos los intentos fallidos')
		print('2- Los que se repiten en un intervalo de tiempo')
		print('\n0- Para terminar')
		#try:
		opcion= raw_input('Opción: ')
		if opcion==str(1):
			print(dic)
		elif opcion==str(2):
			print('nueva funcion')
			menu_repe()
		elif opcion==str(0):
			print('\tAdios')
			nofin=False
		else:
			print('\t OPCIÓN ERRÓNEA')
		#except:
		#	print('\t Error vuelva a intentarlo')

def menu_repe():
	nofin=True
	while nofin:
		print(50*'=')
		print(' \t M E N Ú - repetición de intentos ')
		print(50*'=')
		try:
			inten = int(raw_input('Número de intentos : '))
			intervalo = int(raw_input('Intervalo en minutos: '))
			nofin=False
		except:
			print('\tERROR - valor no admitido')
			print('\tVuelva a intentarlo')

	repetidos(inten,intervalo)


def ana():
	f = open ('auth.log', 'r')
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

dic = ana()




def repetidos(inten,intervalo):
	todo=ana()
	#
	for punte in todo:
		#print(todo[punte])
		print('\n\tAnálisis de la Ip : '+ punte)
		i=0

		for conexion in todo[punte]:
			print('\n'+punte+' conectó el '+str(conexion))
			#print(todo[punte][i]-conexion)
			raw_input(timedelta.total_seconds(todo[punte][i]-conexion))

			if (timedelta.total_seconds(todo[punte][i]-conexion) <= intervalo*60):
				print('Analizando conexión : '+str(conexion))
				Intento=0

				for SigueComprobando in todo[punte]:
					Diferencia = timedelta.total_seconds(todo[punte][i]-SigueComprobando)
					print(str(todo[punte][i])+' --- '+str(SigueComprobando)+
							' diferencia en segundos : '+ str(Diferencia))

					#print(Diferencia)
					if (Diferencia>0 and Diferencia <= intervalo*60 and Intento<=inten):
						Intento+=1
						raw_input('Intento núm. : '+str(Intento)+ ' en : '+
									str(todo[punte][i]-SigueComprobando))

				i+=1
	print('\n\nSe repite: '+str(inten) + ' en minutos: '+str(intervalo))
	print('\n\nSe repite: '+str(inten) + ' en minutos: '+str(intervalo))
	informe_html += "</html></body>"
    return render(request, 'ver_para.html',{'informe': informe_html })

#
#
#
