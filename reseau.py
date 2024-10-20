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
        
        def set_couche(self, value=2):
            if (self.control==0):
                if(value>=2):
                    for i in range (0,value):
                        self.couche.append(0)
                else:
                    print("Must have at least 2 layers")
            else:
                print("Network is already existing, you cant edit it")

        def add_couche(self,pos):
            if (self.control == 0):
                if (pos>=0 and pos<len(self.couche)):
                    self.couche.insert(pos,0)
                else:
                    print("You can add a layer between [0,",len(self.couche),"]")
            else:
                print("Network is already existing, you cant edit it")

        def add_neurone(self,couche,nbr=1):
            if (self.control==0):
                if(couche>=0 and couche <=len(self.couche)-1 and nbr>0):
                    self.couche[couche] += nbr
            else:
                print("Network is already existing, you cant edit it")
        
        def add_all_neurone(self,tab):
            if (self.control==0):
                if(len(tab) == len(self.couche)):
                    for i in range (0, len(tab)):
                        self.add_neurone(i,tab[i])
                else:
                    print("Tab must be ",len(self.couche)," long")
            else:
                print("Network is already existing, you cant edit it")