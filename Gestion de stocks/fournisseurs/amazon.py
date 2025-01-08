from fournisseur import Fournisseur

class Amazon(Fournisseur):
    def __init__(self, nom_fournisseur, num_telephone, email, adresse):
        super().__init__(nom_fournisseur, num_telephone, email, adresse)
    
    def informations(self):
        super().information_fournisseur()