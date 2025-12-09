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
        no.altura = 1 + max(self.get_altura(no.esq), self.get_altura(no.dir))

    def rotacao_dir(self, y):
        x = y.esq
        t2 = x.dir

        x.dir = y
        y.esq = t2

        self.atualiza_altura(y)
        self.atualiza_altura(x)

        return x
    
    def rotacao_esq(self, x):
        y = x.dir
        t2 = y.esq

        y.esq = x
        x.dir = t2

        self.atualiza_altura(x)
        self.atualiza_altura(y)

        return y
    
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
        if balance < -1 and key > no.dir.key:
            return self.rotacao_esq(no)
        
        #Balanco Esquerda-Direita
        if balance > 1 and key > no.esq.key:
            no.esq = self.rotacao_esq(no.esq)
            return self.rotacao_dir(no)
        
        #Balanco Direita-Esquerda
        if balance < -1 and key < no.dir.key:
            no.dir = self.rotacao_dir(no.dir)
            return self.rotacao_esq(no)
        
        return no
    
    def delete(self, key):
        self.raiz = self._delete(self.raiz, key)

    def _delete(self, no, key):
        if not no:
            return no
        
        if key < no.key:
            no.esq = self._delete(no.esq, key)
        
        elif key > no.key:
            no.dir = self._delete(no.dir, key)

        else:
            if not no.esq:
                return no.dir
            elif not no.dir:
                return no.esq
            
            temp = self._get_valor_min_no(no.dir)
            no.key = temp.key
            no.dir = self._delete(no.dir, temp.key)

        if not no:
            return no
        
        self.atualiza_altura(no)

        balance = self.get_balance(no)

        #Esquerda-Esquerda
        if balance > 1 and self.get_balance(no.esq) >= 0:
            return self.rotacao_dir(no)
        
        #Esquerda-Direita
        if balance > 1 and self.get_balance(no.esq) < 0:
            no.esq = self.rotacao_esq(no.esq)
            return self.rotacao_dir(no)
        
        #Direita-Direita
        if balance < -1 and self.get_balance(no.dir) <= 0:
            return self.rotacao_esq(no)
        
        #Direita-Esquerda
        if balance < -1 and self.get_balance(no.dir) > 0:
            no.dir = self.rotacao_dir(no.dir)
            return self.rotacao_esq(no)
        
        return no
    
    def _get_valor_min_no(self, no):
        atual = no
        while atual.esq:
            atual = atual.esq
        return atual
    
    def procura(self, key):
        return self._procura(self.raiz, key)
    
    def _procura(self, no, key):
        if not no or no.key == key:
            return no
        
        if key < no.key:
            return self._procura(no.esq, key)
        return self._procura(no.dir, key)
    
    def inorder(self):
        result = []
        self._inorder(self.raiz, result)
        return result

    def _inorder(self, no, result):
        if no:
            self._inorder(no.esq,result)
            result.append(no.key)
            self._inorder(no.dir,result)

    def preorder(self):
        result = []
        self._preorder(self.raiz, result)
        return result

    def _preorder(self, no, result):
        if no:
            result.append(no.key)
            self._preorder(no.esq, result)
            self._preorder(no.dir, result)

    def display(self):
        self._display(self.raiz, 0)

    def _display(self, no, level):
        if no:
            self._display(no.dir,level + 1)
            print(' ' * 4 * level + f'->{no.key} (h={no.altura}), b = {self.get_balance(no)})')
            self._display(no.esq, level + 1)


        

def main():
    avl = AVLTree()

    valores = [10,20,30,25,40,50]
    print("Inserindo valores:", valores)
    for valor in valores:
        avl.inserir(valor)
    
    print("\nÁrvore AVL:")
    avl.display()

    print("\nPercurso em ordem:", avl.inorder())
    print("Percurso em pré-ordem:", avl.preorder())

    # Buscar um valor
    busca = 25
    resultado = avl.procura(busca)
    print(f"\nBuscando {busca}:", "Encontrado" if resultado else "Não encontrado")


     # Deletar um valor
    print(f"\nDeletando 30...")
    avl.delete(30)
    avl.display()

    print("\nPercurso em ordem após deletar:", avl.inorder())


if __name__ == "__main__":
    main()
