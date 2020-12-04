import numpy as np
from tkinter import *
class Matriz:
    def __init__(self, root):
        self.v = root
        self.v.geometry("330x220+300+300")
        self.v.title("Matrices para Circuitos xd")
        self.v.resizable(False, False)
        self.origen = [0, 0]
        self.mlf = Entry(self.v, font=('arial',15,'bold'),width=3, insertwidth=2, justify="right")
        self.mlf.pack()
        self.mlf.place(x=100,y=50)
        self.mlc = Entry(self.v, font=('arial',15,'bold'),width=3, insertwidth=2, justify="right")
        self.mlc.pack()
        self.mlc.place(x=200,y=50)
        self.mzf = Entry(self.v, font=('arial',15,'bold'),width=3, insertwidth=2, justify="right")
        self.mzf.pack()
        self.mzf.place(x=100,y=100)
        self.mzc = Entry(self.v, font=('arial',15,'bold'),width=3, insertwidth=2, justify="right")
        self.mzc.pack()
        self.mzc.place(x=200,y=100)
        self.grf=Button(self.v,text="Generar Matriz", font=('arial', 10, 'italic'),command=self.definirm).place(x=110,y=150)
    def definirm(self):
        mt = Tk()
        mt.title("Matrices")
        mt.geometry("630x630+300+300")
        mt.resizable(False, False)
        m = int(self.mlf.get())
        n = int(self.mlc.get())
        z = int(self.mzf.get())
        t = int(self.mzc.get())

        pap = []
        zap = []
        maxi=0
        maxj=0
        for i in range(0, m):
            for j in range(0,n):
                mal = Entry(mt, font=('arial',15,'bold'),width=3, insertwidth=2, justify="right")
                mal.pack()
                mal.place(x=(1+j)*50,y=(i+1)*50)
                maxi=10+i*50
                maxj=j*50
                pap.append(mal)
        for i in range(0, z):
            for j in range(0,t):
                maz = Entry(mt, font=('arial',15,'bold'),width=3, insertwidth=2, justify="right")
                maz.pack()
                maz.place(x=maxj+200+(j)*50,y=(i+1)*50)
                zap.append(maz)
        sv=Button(mt,text="Reales", font=('arial', 10, 'italic'),command=lambda l=pap, a=zap, fl=m, fz=z,cl=n,cz=t, k=mt: solver(l, a, fl, fz, cl, cz, k)).place(x=maxi+3*maxi/2,y=2*maxj)
        v=Button(mt,text="Complejos", font=('arial', 10, 'italic'),command=lambda l=pap, a=zap, fl=m, fz=z,cl=n,cz=t, k=mt: solvec(l, a, fl, fz, cl, cz, k)).place(x=maxi+100+3*maxi/2,y=2*maxj)

class solver:
    def __init__(self, M, A, m, z, n, t, k):
        P = np.zeros((m*n), dtype=int)
        N = np.zeros((z*t), dtype=int)
        c=0
        x=0
        l=0
        lp=0
        lc=0
        mx=0
        for entry in M:
            P[c]=int(entry.get())
            c=c+1
        P.resize(m,n)
        for entry in A:
            N[l]=int(entry.get())
            l=l+1
        N.resize(z,t)
        print(P)
        try:
            x=np.linalg.solve(P,N)
            print(x)
            zx.destroy()
        except UnboundLocalError:
            x=np.linalg.solve(P,N)
            zx=Tk()
            print(x.size)
            sz=x.size*100
            zx.title("Resultado")
            zx.geometry(f"{sz}x{sz}+300+300")
            zx.resizable(False, False)
            for r in x:
                lc=0
                for c in r:
                    celula = Label(zx,text='{}'.format(round(c, 4)))
                    celula.pack()
                    celula.place(x=(1+lc)*50,y=(lp+1)*50)
                    mx=10+lp*50
                    lc=lc+1
                    
                lp=lp+1
class solvec:
    def __init__(self, M, A, m, z, n, t, k):
        P = np.zeros((m*n), dtype=complex)
        N = np.zeros((z*t), dtype=complex)
        c=0
        x=0
        l=0
        lp=0
        lc=0
        mx=0
        for entry in M:
            P[c]=complex(entry.get())
            c=c+1
        P.resize(m,n)
        for entry in A:
            N[l]=complex(entry.get())
            l=l+1
        N.resize(z,t)
        print(P)
        try:
            x=np.linalg.solve(P,N)
            print(x)
            zx.destroy()
        except UnboundLocalError:
            x=np.linalg.solve(P,N)
            zx=Tk()
            print(x.size)
            sz=x.size*100
            zx.title("Resultado")
            zx.geometry(f"{sz}x{sz}+300+300")
            zx.resizable(False, False)
            for r in x:
                lc=0
                for c in r:
                    celula = Label(zx,text='{}'.format(round(c, 4)))
                    celula.pack()
                    celula.place(x=(1+lc)*50,y=(lp+1)*50)
                    mx=10+lp*50
                    lc=lc+1
                    
                lp=lp+1
        
root = Tk()
main = Matriz(root)
root.mainloop()
