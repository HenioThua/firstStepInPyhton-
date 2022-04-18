class tela:
    def __init__(self):
        self.x = 1
        self.y = 1 
        self.m=[[' ' for i in range(20)] for j in range(20)]
    def exibe_tela(self):
        for i in self.m:
            for j in i:
                print(j,sep='')
            print()
    def posiciona(self, x, y):
        self.x = x
        self.y = y
    def print(self, prompt):
        for i in prompt:
            self.m[self.x-1][self.y-1]=i
            self.x+=1
            
t = tela()
t.print("banana")
t.posiciona(2,5)
t.print("maça")
t.exibe_tela()
