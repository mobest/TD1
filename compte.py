"""Fichier compte.py"""

import httplib
import time
import sys
import pdb

LOGGER = sys.argv[2]
if len(sys.argv) > 3:
    LOGGER = True


def connexion(fichier, site):
    """fonction connexion"""
    fichier_log(fichier, "Connexion au site")
    
    pdb. set_trace() # point d arret dans le script
    git config --global user.name "Jeremy.Vacher"
    git config --global user.email "mobestdu42@hotmail.fr"
    
    ht1 = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
    ht1.request("GET", site)
    re1 = ht1.getresponse()

    fichier_log(fichier, "%s, %s " % (re1.status, re1.reason))

    fichier_log(fichier, "Recuperation du texte")

    texte = re1.read()

    fichier_log(fichier, "Decoupage du texte")

    liste = texte.split(" ")

    fichier_log(fichier, "Il y a %d mots" % (len(liste)))

    print re1.status, re1.reason
    print len(liste)


def fichier_log(fichier, chaine):
    """fonction fichierLog"""
    if (LOGGER == True):
        fichier.write(time.strftime('%d/%m/%y %H:%M : ', time.localtime()))
        fichier.write(chaine + " \n")


LOG = open("prog.log", "a")

fichier_log(LOG, "Lancement du programme")

if (len(sys.argv) > 3):
    fichier_log(LOG, "Erreur nombre d arguments")
else:
    connexion(LOG, sys.argv[1])

fichier_log(LOG, "Fermeture du programme")

LOG.close()
