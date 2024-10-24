from fonctions import sigmoide, tangente
class Reseau:
    def __init__(self, name='Network_1', learn='sigmoide', error=0.001):
        """
            ENGLISH
            # We initialise the network, with theses parameters:
                - a name, just for information purposes
                - the activation fonction wanted at the start
                - the error wanted during learning phases
 
            FRENCH
            # On initialise le réseau, avec pour paramètres:
                - un nom, à titre informatif
                - la fonction d'activation voulu au début
                - l'erreur désirée lors des phases d'apprentissage   
        """

        self.name = name # Network name
        if 'tangente' == str.lower(learn):
            self.fun_learn = tangente
            self.name_fun_learn = 'tangente'
        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = 'sigmoide'
        self.error = error # learning error
        self.couche = [] # Tab of layer with the nbr of neurons per layers
        self.link = [] # Tab with every weights
        self.values = [] # Tab with the differents neurons values
        self.control = 0 # Controler is adding layers/neurons after initialisation

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
            return [self.get_name(),self.get_name_fun_learn(),self.get_erreur(),self.get_nbr_layer()]
        
        def get_nbr_layer(self):
            return len(self.layer)
        
        def get_last_layer(self):
            return self.values[-1]
        
        def set_layer(self, value=2):
            if (self.control==0):
                if(value>=2):
                    for i in range (0,value):
                        self.layer.append(0)
                else:
                    print("Must have at least 2 layers")
            else:
                print("Network is already existing, you cant edit it")

        def add_layer(self,pos):
            if (self.control == 0):
                if (pos>=0 and pos<len(self.layer)):
                    self.layer.insert(pos,0)
                else:
                    print("You can add a layer between [0,",len(self.layer),"]")
            else:
                print("Network is already existing, you cant edit it")

        def add_neurone(self,layer,nbr=1):
            if (self.control==0):
                if(layer>=0 and layer <=len(self.layer)-1 and nbr>0):
                    self.layer[layer] += nbr
            else:
                print("Network is already existing, you cant edit it")
        
        def add_all_neurone(self,tab):
            if (self.control==0):
                if(len(tab) == len(self.layer)):
                    for i in range (0, len(tab)):
                        self.add_neurone(i,tab[i])
                else:
                    print("Tab must be ",len(self.layer)," long")
            else:
                print("Network is already existing, you cant edit it")