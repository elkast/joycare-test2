def mauvais_choix(reponse):
    
    mots_cles_negatifs = ["non", "désolé", "impossible", "jamais", "pas"]

    # Vérifier si un des mots clés négatifs est dans la réponse
    for mot in mots_cles_negatifs:
        if mot in reponse.lower():
            return True
    
    return False

# Exemple de réponse
reponse = "Désolé, je ne suis pas intéressée."

# Vérifier si c'est un mauvais choix
if mauvais_choix(reponse):
    print("C'est un mauvais choix de me répondre ainsi.")
else:
    print("Ce n'est pas un mauvais choix de me répondre ainsi.")
