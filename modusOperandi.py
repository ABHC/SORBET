# -*- coding: utf8 -*-

import sys
import math

import sorbetBox

def classicMethod(shear_modulus, shear_stress):

	#############################################
	######### STEP 2 : FIX SOME VALUES
	############################################

	print ("\nSet the maximum opening angle in degrees :") #THETA majuscule
	angle = float(raw_input())

	angle = math.radians(angle)

	print ("\nFix the maximum length of the torsion leg in mm : ") #l sur le schéma Lattice Hinge
	legs_length = float(raw_input())

	print ("\nFix the width of the torsion leg in mm : ") #t sur le schéma Lattice Hinge / h section
	legs_width = float(raw_input())

	print ("\nFix the thickness of the torsion leg mm : ") #e sur le schéma Lattice Hinge / b section
	legs_thickness = float(raw_input())

	section_dimension = [legs_width, legs_thickness]
	section_dimension.sort()

	min_b = section_dimension[0]
	sup_h = section_dimension[len(section_dimension)-1]

	#############################################
	######### STEP 3 : CALCULATION OF THE h/b RELATION
	############################################

	k_coefficients = sorbetBox.hbRelation(min_b, sup_h)
	k1 = k_coefficients[0]
	k2 = k_coefficients[1]

	#############################################
	######### STEP 4 : CALCULATION OF THE TORSIONNAL MOMENT
	#############################################

	torsionnal_moment = shear_stress*k1*(math.pow(min_b,2))*sup_h

	#############################################
	######### STEP 5 : CALCULATION OF THE NUMBER OF TORSIONNAL LEGS
	#############################################

	num_legs = (k2*shear_modulus*min_b*angle)/(k1*legs_length*shear_stress)
	num_legs = math.ceil(num_legs) #arrondi au supérieur du nombre de jambes

	#############################################
	######### STEP 6 : CALCULATION OF THE TORSIONNAL ANGLE OF EACH LEG
	#############################################

	theta = angle/num_legs
	#theta_verif = (k1/k2)*((shear_stress*legs_length)/(shear_modulus*min_b))

	#############################################
	######### STEP 7 : CALCULATION OF THE LEG CLEARANCE
	#############################################

	legs_distance = (-legs_width)+(2*math.sqrt(math.pow(legs_width,2)/2))*(math.cos(((math.pi)/4)-(angle/num_legs)))

	#############################################
	######### STEP 8 : CALCULATION OF THE TOTAL HINGE WIDTH
	#############################################

	hinge_width = (num_legs*legs_width)+((num_legs+1)*legs_distance)

	#############################################
	######### STEP 9 : CALCULATION OF THE HINGE RADIUS
	#############################################

	hinge_radius = (180*hinge_width)/((math.degrees(angle))*(math.pi))

	#############################################
	######### STEP 10 : DISPLAY THE RESULTS
	#############################################

	if legs_distance > 0 :
		print (u'Congratulations! The rotation of your hinge is assured :\n')
		print (u'Number of legs : '+str(num_legs)+u'')
		print (u'Theta : '+str(math.degrees(theta))+u'°')
		#print (u'Torsionnal moment : '+str(torsionnal_moment)+u' N/mm')
		print (u'Leg clearance : '+str(legs_distance)+u' mm')
		print (u'Hinge Width : '+str(hinge_width)+u' mm')
		print (u'Hinge radius : '+str(hinge_radius)+u' mm')

	else :
		print (u'Warning : The rotation of your hinge is not ensured with these parameters.\n')


def radiusMethod(shear_modulus, shear_stress):

	#############################################
	######### STEP 2 : FIX SOME VALUES
	############################################

	print ("\nSet the maximum opening angle in degrees :") #THETA majuscule
	angle = float(raw_input())

	angle = math.radians(angle)

	print ("\nFix the radius of your hinge in mm (relative to the neutral fiber) : ") #rayon sur une vue de profil de la charnière
	hinge_radius = float(raw_input())

	print ("\nFix the spacing between two connecting legs in mm : ")
	legs_distance = float(raw_input())

	print ("\nFix the width of the torsion leg in mm : ") #t sur le schéma Lattice Hinge / h section
	legs_width = float(raw_input())

	print ("\nFix the thickness of the torsion leg mm : \n") #e sur le schéma Lattice Hinge / b section
	legs_thickness = float(raw_input())

	section_dimension = [legs_width, legs_thickness]
	section_dimension.sort()

	min_b = section_dimension[0]
	sup_h = section_dimension[len(section_dimension)-1]

	#############################################
	######### STEP 3 : CALCULATION OF THE h/b RELATION
	############################################

	k_coefficients = sorbetBox.hbRelation(min_b, sup_h)
	k1 = k_coefficients[0]
	k2 = k_coefficients[1]

	#############################################
	######### STEP 4 : CALCULATION OF THE TOTAL HINGE WIDTH
	############################################

	hinge_width = (hinge_radius*(math.degrees(angle))*(math.pi))/180

	#############################################
	######### STEP 5 : CALCULATION OF THE NUMBER OF TORSIONNAL LEGS
	############################################

	num_legs = (hinge_width-legs_distance)/(legs_width+legs_distance)
	num_legs = math.ceil(num_legs) #arrondi au supérieur du nombre de jambes

	#############################################
	######### STEP 6 : CALCULATION OF THE TORSIONNAL ANGLE OF EACH LEG
	#############################################

	theta = angle/num_legs

	#############################################
	######### STEP 7 : CALCULATION OF THE TORSIONNAL LEGS LENGTH
	#############################################

	legs_length = (k2*shear_modulus*min_b*angle)/(num_legs*k1*shear_stress)

	#############################################
	######### STEP 8 : DISPLAY THE RESULTS
	#############################################

	print (u'Number of legs : '+str(num_legs)+u'')
	print (u'Theta : '+str(math.degrees(theta))+u'°')
	print (u'Legs length : '+str(legs_length)+u' mm')
	print (u'Hinge Width : '+str(hinge_width)+u' mm')


def advancedMethod(shear_modulus, shear_stress):


	#############################################
	######### STEP 2 : CHOOSE THE VARIABLE VALUE
	############################################

	print ("1. The number of legs is variable.")
	print ("2. The width of torsion leg is variable\n")

	variable_option = int(raw_input())
	print("\n")

	#############################################
	######### STEP 2 : FIX SOME VALUES
	############################################

	print ("\nSet the maximum opening angle in degrees :") #THETA majuscule
	angle = float(raw_input())

	angle = math.radians(angle)

	if variable_option == 1:

		print ("\nFix the radius of your hinge in mm : ") #rayon sur une vue de profil de la charnière
		hinge_radius = float(raw_input())

		print ("\nFix the width of the torsion leg in mm : ") #t sur le schéma Lattice Hinge / h section
		legs_width = float(raw_input())

		print ("\nFix the thickness of the torsion leg mm : \n") #e sur le schéma Lattice Hinge / b section
		legs_thickness = float(raw_input())

		print ("\nFix the minimum leg clearance you could accept in mm : \n") #e sur le schéma Lattice Hinge / b section
		tolerance = float(raw_input())

		print ("\nFix the maximal width of the hinge you could accept in mm : \n") #e sur le schéma Lattice Hinge / b section
		target = int(raw_input())

		#############################################
		######### STEP 3 : CALCULATION OF THE h/b RELATION
		############################################

		section_dimension = [legs_width, legs_thickness]
		section_dimension.sort()
		min_b = section_dimension[0]
		sup_h = section_dimension[len(section_dimension)-1]

		k_coefficients = sorbetBox.hbRelation(min_b, sup_h)
		k1 = k_coefficients[0]
		k2 = k_coefficients[1]

		#############################################
		######### STEP 4 : CALCULATION OF THE POSSIBILITY OF ROTATION FOR THE NUMBER OF LEGS
		############################################

		num_legs = 1
		legs_distance = tolerance+1

		while legs_distance > tolerance:

			theta = angle/num_legs
			legs_distance = (theta*(hinge_radius-(legs_thickness/2)))-(2*legs_width) #calcul de kinf

			#############################################
			######### STEP 5 : CALCULATION OF THE TOTAL WIDTH OF THE HINGE
			#############################################

			hinge_width = (num_legs*legs_width)+((num_legs+1)*legs_distance)

			#############################################
			######### STEP 6 : CALCULATION OF THE TORSIONNAL LEGS LENGTH
			#############################################

			legs_length = (k2*shear_modulus*min_b*angle)/(num_legs*k1*shear_stress)

			#############################################
			######### STEP 7 : DISPLAY THE RESULTS
			#############################################

			if (target-5) <= hinge_width <= (target+5):
				print (u'Number of legs : '+str(num_legs)+u'')
				print (u'Theta of each leg : '+str(math.degrees(theta))+u'°')
				print (u'Legs clearance : '+str(legs_distance)+u' mm')
				print (u'Legs length : '+str(legs_length)+u' mm')
				print (u'Hinge width : '+str(hinge_width)+u' mm\n')

			#print (u'Number of legs : '+str(num_legs)+u'')
			#print (u'Theta of each leg : '+str(math.degrees(theta))+u'°')
			#print (u'Legs clearance : '+str(legs_distance)+u' mm')
			#print (u'Legs length : '+str(legs_length)+u' mm')
			#print (u'Hinge width : '+str(hinge_width)+u' mm\n')

			num_legs = num_legs+1

	elif variable_option == 2:

		print ("\nFix the width of your hinge in mm : ") #rayon sur une vue de profil de la charnière
		hinge_width = float(raw_input())

		print ("\nFix the number of torsion legs in mm : ")
		num_legs = float(raw_input())

		print ("\nFix the thickness of the torsion leg mm : \n") #e sur le schéma Lattice Hinge / b section
		legs_thickness = float(raw_input())

		print ("\nFix the minimal width of the torsion leg in mm : ") #t sur le schéma Lattice Hinge / h section
		legs_width = float(raw_input())

		print ("\nFix the step for the torsion legs width in mm : \n") #e sur le schéma Lattice Hinge / b section
		calculus_step = float(raw_input())

		print ("\nFix the minimum leg clearance you could accept in mm : \n") #e sur le schéma Lattice Hinge / b section
		tolerance = float(raw_input())

		#############################################
		######### STEP 3 : CALCULATION OF THE HINGE RADIUS
		############################################

		hinge_radius = hinge_width/angle

		#############################################
		######### STEP 4 : CALCULATION OF THE POSSIBILITY OF ROTATION FOR THE TORSION LEG WIDTH
		############################################

		legs_distance = tolerance+1

		while legs_distance > tolerance:

			theta = angle/num_legs
			legs_distance = theta*(hinge_radius-(legs_thickness/2)-2*legs_width)

			#############################################
			######### STEP 5 : CALCULATION OF THE h/b RELATION
			############################################

			section_dimension = [legs_width, legs_thickness]
			section_dimension.sort()
			min_b = section_dimension[0]
			sup_h = section_dimension[len(section_dimension)-1]

			k_coefficients = sorbetBox.hbRelation(min_b, sup_h)
			k1 = k_coefficients[0]
			k2 = k_coefficients[1]

			#############################################
			######### STEP 6 : CALCULATION OF THE TORSIONNAL LEGS LENGTH
			#############################################

			legs_length = (k2*shear_modulus*min_b*angle)/(num_legs*k1*shear_stress)

			#############################################
			######### STEP 7 : DISPLAY THE RESULTS
			#############################################

			print (u'Number of legs : '+str(num_legs)+u'')
			print (u'Theta : '+str(math.degrees(theta))+u'°')
			print (u'Legs clearance : '+str(legs_distance)+u' mm')
			print (u'Legs length : '+str(legs_length)+u' mm\n')

			legs_width = legs_width+calculus_step

	else:
		print("ERROR : Please select 1 or 2\n")
