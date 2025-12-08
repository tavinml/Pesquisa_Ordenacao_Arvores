class No:
    def __init__(self, key):
        self.key = key
        self.esq = None
        self.dir = None
        self.altura = 1

class AVLTree:
    def __init__(self):
        self.raiz = None

    def get_altura(self, no):
        if not no:
            return 0
        return no.altura
    
    def get_balance(self, no):
        if not no:
            return 0
        return self.get_altura(no.esq) - self.get_altura(no.dir)
    
    def atualiza_altura(self, no):
        if not no:
            return 0
        no.altura = 1 + max(self.get_altura(no.left), self.get_altura(no.right))

    def rotacao_dir(self, y):
        x = y.esq
        t2 = x.dir

        x.dir = y
        y.left = t2

        self.atualiza_altura(y)
        self.atualiza_altura(x)

        return x
    
    def rotacao_esq(self, y):
        x = y.dir
        t2 = x.esq

        x.esq = y
        y.dir = t2

        self.atualiza_altura(y)
        self.atualiza_altura(x)

        return x
    
    def inserir(self, key):
        self.raiz = self._inserir(self.raiz, key)

    def _inserir(self, no, key):
        if not no:
            return No(key)
        
        if key < no.key:
            no.esq = self._inserir(no.esq, key)
        elif key > no.key:
            no.dir = self._inserir(no.dir, key)
        else:
            return no
        
        self.atualiza_altura(no)

        balance = self.get_balance(no)

        #Balanco Esquerda-Esquerda
        if balance > 1 and key < no.esq.key:
            return self.rotacao_dir(no)
        
        #Balanco Direita-Direita
        if balance < -1 and key < no.dir.key:
            return self.rotacao_es(no)
        
        #Balanco Esquerda-Direita
        if balance > 1 and key > no.esq.key:
            no.esq = self.rotacao_es(no.esq)
            return self.rotacao_dir(no)
        
        #Balanco Direita-Esquerda
        if balance < -1 and key < no.dir.key:
            no.dir = self.rotacao_dir(no.dir)
            return self.rotacao_esq(no)
        
        return no
