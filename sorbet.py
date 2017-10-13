# -*- coding: utf8 -*-

import sys
from operator import itemgetter
from math import ceil

import modusOperandi
import sorbetBox

######### MAIN

######### CONNECTION TO PyHinge DATABASE
database = sorbetBox.databaseConnection()

#############################################
######### STEP 0 : CHOOSE THE MODUS OPERANDI
############################################

print ("Welcome to SORBET ! Please choose choose how to create your lattice hinge :\n")
print ("1. Create a lattice hinge by minimizing the number of torsional legs required.")
print ("2. Create a lattice hinge according to its intended radius.")
print ("3. Create a lattice hinge by minimizing the width of the hinge.\n")

modus = int(raw_input())
print("\n")


#############################################
######### STEP 1 : CHOOSE MATERIAL
############################################

call_materials = database.cursor()
call_materials.execute("SELECT id, material, class FROM materials_pyhinge")
menu = call_materials.fetchall()
call_materials.close()

print ("Choisissez un matériaux")

for line in menu:
	print (unicode(line[0])+u'. Matériau : '+unicode(line[1])+u', class : '+unicode(line[2])+u'.\n')

material_id = int(raw_input())
argdb = (material_id,)

print (u'ID : '+str(material_id)+u'\n')

query_essence = ("SELECT material, class, shear_modulus, shear_stress FROM materials_pyhinge WHERE id = %s")

call_materials = database.cursor()
call_materials.execute(query_essence, argdb)
material_spec = call_materials.fetchone()
call_materials.close()

#print (u'Vous avez choisi : '+unicode(material_spec[0])+u'\n')
print (u'Your choice : '+unicode(material_spec[0])+u', '+unicode(material_spec[1])+'\n')

G = material_spec[2]
tau = material_spec[3]

print ('Shear modulus : '+str(G)+' MPa')
print ('Shear stress : '+str(tau)+' MPa')

#############################################
######### STEP 1.1 : GO TO THE CHOSEN MODUS OPERANDI
############################################

if modus == 1 :

	modusOperandi.classicMethod(G, tau)

elif modus == 2 :

	modusOperandi.radiusMethod(G, tau)

elif modus == 3 :

	results_list = modusOperandi.methodW(G, tau)
	results_list = sorted(results_list, key=itemgetter(0, 1, 6))

	print (u'\nNumber of possible models: '+str(len(results_list))+u'\n')

	print ("Want to reduce the number of results by choosing a new discriminating criterion ? : \n0. NO\n1. YES")
	discrimination = int(raw_input())
	discrimination = bool(discrimination)

	if discrimination is True:
		print ("\nChoose the parameters to minimizing :")
		print ("1. Set mimimum delta.")
		print ("2. Set minimum number of leg (influences theta)")
		print ("3. Set minimum leg clearance.")

		discrimination_modus = int(raw_input())

		print ("\nChoose the minimum value : ")
		mini = float(raw_input())

		mini_results_list = []

		for results in results_list:
			if discrimination_modus == 1 and results[0] >= int(mini):
				mini_results_list.append(results)

			if discrimination_modus == 2 and results[1] >= mini:
				mini_results_list.append(results)

			if discrimination_modus == 3 and results[3] >= mini:
				mini_results_list.append(results)

		print (u'\nNumber of possible models: '+str(len(mini_results_list))+u'\n')

		print ("Want to reduce the number of results by choosing a new discriminating criterion ? : \n0. NO\n1. YES")
		discrimination_second = int(raw_input())
		discrimination_second = bool(discrimination_second)

		if discrimination_second is True:
			print ("\nChoose the parameters to minimizing :")
			print ("1. Set mimimum delta.")
			print ("2. Set minimum number of leg (influences theta)")
			print ("3. Set minimum leg clearance.")

			discrimination_modus_second = int(raw_input())

			print ("\nChoose the minimum value : ")
			nano = float(raw_input())

			nano_results_list = []

			for results in mini_results_list:
				if discrimination_modus_second == 1 and results[0] >= int(nano):
					nano_results_list.append(results)

				if discrimination_modus_second == 2 and results[1] >= int(nano):
					nano_results_list.append(results)

				if discrimination_modus_second == 3 and results[3] >= nano:
					nano_results_list.append(results)

			print (u'\nNumber of possible models: '+str(len(nano_results_list))+u'\n')

			for results in nano_results_list:
				print (u'delta: '+str(results[0])+u'')
				print (u'Number of legs : '+str(results[1])+u'')
				print (u'Theta of each leg : '+str(ceil(100*results[2])/100)+u'°')
				print (u'Leg Clearance (k) : '+str(ceil(100*results[3])/100)+u' mm')
				print (u'Legs length : '+str(ceil(100*results[4])/100)+u' mm')
				print (u'Lmin : '+str(ceil(100*results[5])/100)+u' mm')
				print (u'Plane Parts : '+str(ceil(100*results[6])/100)+u' mm x '+str(ceil(100*results[6])/100)+u' mm')
				print (u'Hinge width : '+str(ceil(100*results[7])/100)+u' mm\n')

		elif discrimination_second is False:
			for results in mini_results_list:
				print (u'delta: '+str(results[0])+u'')
				print (u'Number of legs : '+str(results[1])+u'')
				print (u'Theta of each leg : '+str(ceil(100*results[2])/100)+u'°')
				print (u'Leg Clearance (k) : '+str(ceil(100*results[3])/100)+u' mm')
				print (u'Legs length : '+str(ceil(100*results[4])/100)+u' mm')
				print (u'Lmin : '+str(ceil(100*results[5])/100)+u' mm')
				print (u'Plane Parts : '+str(ceil(100*results[6])/100)+u' mm x '+str(ceil(100*results[6])/100)+u' mm')
				print (u'Hinge width : '+str(ceil(100*results[7])/100)+u' mm\n')

	elif discrimination is False:
		for results in results_list:
			print (u'delta: '+str(results[0])+u'')
			print (u'Number of legs : '+str(results[1])+u'')
			print (u'Theta of each leg : '+str(ceil(100*results[2])/100)+u'°')
			print (u'Leg Clearance (k) : '+str(ceil(100*results[3])/100)+u' mm')
			print (u'Legs length : '+str(ceil(100*results[4])/100)+u' mm')
			print (u'Lmin : '+str(ceil(100*results[5])/100)+u' mm')
			print (u'Plane Parts : '+str(ceil(100*results[6])/100)+u' mm x '+str(ceil(100*results[6])/100)+u' mm')
			print (u'Hinge width : '+str(ceil(100*results[7])/100)+u' mm\n')

else :

	print("ERROR : Please select 1,2 or 3\n")
