from fonctions import sigmoide, tangente
class Reseau:
    def __init__(self, name='Reseau1', learn='sigmoide', error=0.001):
        """
            # On initialise le réseau, avec pour paramètres:
                - un nom, à titre informatif
                - la fonction d'activation voulu au début
                - l'erreur désirée lors des phases d'apprentissage
        """

        self.name = name # Nom du réseau
        if 'tangente' == str.lower(learn):
            self.fun_learn = tangente
            self.name_fun_learn = 'tangente'
        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = 'sigmoide'
        self.error = error # Erreur d'apprentissage
        self.couche = [] # Tableau de couche pavec le nombre de neurones par couches
        self.link = [] # Tableau avec tous les poids
        self.values = [] # Tableau avec les différentes valeurs des neurones
        self.control = 0 #Controleur d'ajout de couches/neurones après initialisation

        """
            # Getters / Setters
        """

        def get_name(self):
            return self.name
        
        def set_name(self, name):
            self.name = name

        def set_erreur(self, nbr):
            if (nbr>0):
                self.erreur = nbr

        def set_fun_learn(self, name):
            if (str.lower(name) == 'tangente'):
                self.fun_learn = tangente
                self.name_fun_learn = 'tangente'
            else: 
                self.fun_learn = sigmoide
                self.name_fun_learn = 'sigmoide'

        def get_name_fun_learn(self):
            return self.name_fun_learn
        
        def get_data(self):
            return [self.get_name(),self.get_name_fun_learn(),self.get_erreur(),self.get_nbr_couche()]
        
        def get_nbr_couche(self):
            return len(self.couche)
        
        def get_last_couche(self):
            return self.values[-1]
        
        