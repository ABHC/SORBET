# -*- coding: utf8 -*-

import sys
from operator import itemgetter

import modusOperandi
import sorbetBox

######### MAIN

######### CONNECTION TO PyHinge DATABASE
database = sorbetBox.databaseConnection()

#############################################
######### STEP 0 : CHOOSE THE MODUS OPERANDI
############################################

print ("Welcome to PyHinge ! Please choose choose how to create your lattice hinge :\n")
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
	results_list = sorted(results_list, key=itemgetter(0, 1))

	for results in results_list:
		print (u'delta: '+str(results[0])+u'')
		print (u'Number of legs : '+str(results[1])+u'')
		print (u'Theta of each leg : '+str(results[2])+u'°')
		print (u'Leg Clearance (k) : '+str(results[3])+u' mm')
		print (u'Legs length : '+str(results[4])+u' mm')
		print (u'Lmin : '+str(results[5])+u' mm')
		print (u'Hinge width : '+str(results[6])+u' mm\n')

else :

	print("ERROR : Please select 1,2 or 3\n")
