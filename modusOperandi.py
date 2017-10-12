# -*- coding: utf8 -*-

import sys
import math

import sorbetBox


def coreCalculation(results_list, angle, G, tau, e, t, V, W):

	#############################################
	######### DEFINE N AND K COEFFICIENTS
	#############################################

	n = 1
	k = (W-(n*t))/(n+1)
	Wmin = (3*k+2*t)

	#############################################
	######### RADIUS AND (FIRST) THETA CALCULATION
	#############################################

	#############################################
	######### CHECK IF THE HINGE WIDTH DOESN'T EXCEED THE WITH DEFINED BY USER AND THE POSSIBILITY OF ROTATION
	#############################################

	theta = angle/n
	R = ((n*t)+((n+1)*k))/angle
	kinf = ((theta*(R-(e/2)))-(2*t))

	while kinf >= 0 and k > 0:  # while Wn <= W and kinf >= 0
		#print (u'W: '+str(W)+u'')
		#print (u'n: '+str(n)+u'')
		#print (u'k: '+str(k)+u'')
		#print (u'kinf: '+str(kinf)+u'\n')

		section_dimension = [t, e]
		section_dimension.sort()
		min_b = section_dimension[0]
		sup_h = section_dimension[len(section_dimension)-1]

		k_coefficients = sorbetBox.hbRelation(min_b, sup_h)
		k1 = k_coefficients[0]
		k2 = k_coefficients[1]

		f = (2*t)+k
		lmin = (k2*G*min_b*angle)/(n*k1*tau)
		lmax = (1./2)*(V-(3*f))
		l = lmin
		delta = 1

		while l >= lmin:
			l = (V-(2*delta*f)-f)/(2*delta)

			if lmin <= l <= lmax:
				hinge_spec = [delta, n, math.degrees(theta), k, l, lmin, W]
				results_list.append(hinge_spec)

			delta = delta+1

		n = n+1
		theta = angle/n
		R = ((n*t)+((n+1)*k))/angle
		k = (W-(n*t))/(n+1)
		Wmin = (3*k+2*t)

def methodW(G, tau):

	#############################################
	######### DEFINE RESULTS LIST
	#############################################

	results_list = []

	#############################################
	######### ASK USER SOME FIXED VALUES
	#############################################

	print ("\nSet the maximum opening angle in degrees :") #THETA majuscule
	angle = float(raw_input())

	print ("\nFix the width of the torsion leg (t) in mm : ") #t sur le schéma Lattice Hinge / h section
	t = float(raw_input())

	print ("\nFix the thickness of the torsion leg (e) in mm : ") #e sur le schéma Lattice Hinge / b section
	e = float(raw_input())

	#print ("\nFix the leg clearance (k) in mm : ") #e sur le schéma Lattice Hinge / b section
	#k = float(raw_input())

	print ("\nFix the total hinge length (V) in mm : ") #hinge LENGHT : largest side of the hinge plate = V
	V = float(raw_input())

	print ("\nFix the maximum width of the hinge (Wmax) in mm : ") #e sur le schéma Lattice Hinge / b section
	Wmax = float(raw_input())

	angle = math.radians(angle)

	#############################################
	######### Wmin AND f CALCULATION
	#############################################

	step = 0.5
	W = 0+step

	while W <= Wmax:
		coreCalculation(results_list, angle, G, tau, e, t, V, W)
		W = W+step

	return results_list


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
