# -*- coding: utf8 -*-

import sys

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
print ("3. Check the possibility of rotation.\n")

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

shear_modulus = material_spec[2]
shear_stress = material_spec[3]

print ('Shear modulus : '+str(shear_modulus)+' MPa')
print ('Shear stress : '+str(shear_stress)+' MPa')

#############################################
######### STEP 1.1 : GO TO THE CHOSEN MODUS OPERANDI
############################################

if modus == 1 :

	modusOperandi.classicMethod(shear_modulus, shear_stress)

elif modus == 2 :

	modusOperandi.radiusMethod(shear_modulus, shear_stress)

elif modus == 3 :

	modusOperandi.advancedMethod(shear_modulus, shear_stress)

else :

	print("ERROR : Please select 1,2 or 3\n")
