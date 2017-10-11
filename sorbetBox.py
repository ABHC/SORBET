# -*- coding: utf8 -*-

import MySQLdb


def databaseConnection():
	"""Connexion to PyHinge database"""

	passSQL = open("password.txt", "r")
	passSQL = passSQL.read().strip()

	database = MySQLdb.connect(host="localhost", user="PyHinge", passwd=passSQL, db="PyHinge", use_unicode=1, charset="utf8mb4")

	return database


def hbRelation(min_b, sup_h):

    ######### CONNECTION TO PyHinge DATABASE
    database = databaseConnection()

    #############################################
    ######### STEP 3 : CALCULATION OF THE h/b RELATION
    ############################################

    frac_hb = (sup_h/min_b)

    if frac_hb < 11 :
    	frac_hb = round(frac_hb,2)
    	argk = (frac_hb,)

    	query_k = ("SELECT k1, k2 FROM k_constant WHERE wt_relation = %s")

    	call_k = database.cursor()
    	call_k.execute(query_k, argk)
    	constants = call_k.fetchone()
    	call_k.close()

    	if constants is None:
    		frac_hb = round(frac_hb,1)
    		argk = (frac_hb,)

    		query_k = ("SELECT k1, k2 FROM k_constant WHERE wt_relation = %s")

    		call_k = database.cursor()
    		call_k.execute(query_k, argk)
    		constants = call_k.fetchone()
    		call_k.close()

    	if constants is None:
    		frac_hb = round(frac_hb)
    		argk = (frac_hb,)

    		query_k = ("SELECT k1, k2 FROM k_constant WHERE wt_relation = %s")

    		call_k = database.cursor()
    		call_k.execute(query_k, argk)
    		constants = call_k.fetchone()
    		call_k.close()

    else :
    	frac_hb = 1000
    	argk = (frac_hb,)

    	query_k = ("SELECT k1, k2 FROM k_constant WHERE wt_relation = %s")

    	call_k = database.cursor()
    	call_k.execute(query_k, argk)
    	constants = call_k.fetchone()
    	call_k.close()

    k1 = constants[0]
    k2 = constants[1]

    k_coefficients = [k1,k2]

    return k_coefficients
