from tkinter import *
from os import *
# no caso do tkinter import *, o asterisco ele importa tudo da biblioteca.
# para criar a interface, preciso criar uma variável que armazena essa interface?
# Sim.... criamos a inteface importanto o tkinter, e import Tk
# Precisa ser criado uma classe, dentro da classe criamos um método com o _init_
# o pass serve para ignorar essa parte.
# Criamos uma variavel chamada pagina para armazenar a biblioteca chamada TK()
# Iniciamos citando a classe calculoIMC e dentro do parametro (pagina)
# e citamos a variavel pagina como: pagina.mainloop()
# Entao preciso importar a biblioteca, instanciar dentro de uma variavel, para poder
# fazer com que essa variavel, possa utilizar das ferramentas da biblieoteca.
# no caso, foi instanciado tk dentro de pagina, e passamos os parametros de pagina
# dentro da classe.
class calculoIMC:
 def __init__(self, master=None): # def init é um construtor da pagina
    self.widget1 = Frame(master)
    self.widget1.pack()
    pagina.geometry("1024x768")
    pagina.minsize(500,500)
    pagina.maxsize(1024,768)
    pagina.config(background="lightgray")
    pagina.title("Calculo IMC")

    self.label=Label(master,text="Calculo IMC",background='lightgray',font=("Arial",30, "bold"))
    self.label.pack()

    self.label2=Label(master,text="Peso: ", background="lightgray",font=("Arial",20, "bold"))
    self.label2.place(x=20,y=100)

    self.label3=Label(master,text="Altura: ", background="lightgray",font=("Arial",20, "bold"))
    self.label3.place(x=20,y=200)

    self.entryPeso=Entry(master, font=("Arial", 16),background="white")
    self.entryPeso.place(x=108,y=105)

    self.entryAltura=Entry(master, font=("Arial", 16),background="white")
    self.entryAltura.place(x=120,y=201)
    self.entryAltura.config(width=19)

    self.botaoCalcular=Button(master,text="Calcular IMC",background="gray", command=self.processar_informacao)
    self.botaoCalcular.place(x=20,y=300)
    self.botaoCalcular.config(width=15,height=3)

    self.resultadolabel=Label(master,text="",background="lightgray",font=("Arial",20,"bold"))
    self.resultadolabel.place(x=20,y=400)
    self.resultadolabel.config(width=40,height=2)
    ''' A partir deste código,
    ele rejeita qualquer entrada que nao sejam números.
    Repare que foi criado um método chamado validade entry, e verifica se o novo valor
    é vazio ou substitui . por vazio e verifica se ponto ou virgula sao digitos, se for, ele retorna verdadeiro e deixa a 
    entrada, mas se nao for, ele retorna falso.'''
    nostring=master.register(self.validate_entry)
    self.entryAltura.config(validate="key",validatecommand=(nostring, "%P"))
    self.entryPeso.config(validate="key", validatecommand=(nostring, "%P"))

 def validate_entry(self,novo_valor):
    if novo_valor=="" or novo_valor.replace(',','').replace('.','').isdigit():
      return True
    else:
      return False

 def processar_informacao(self):
    try:
       peso=float(self.entryPeso.get().replace(',','.'))
       altura=float(self.entryAltura.get().replace(',','.'))
       temporario=peso/altura**2
       if temporario < 17:
        resultadoo="Paciente com anorexia"
       elif temporario > 18.5 and temporario < 25:
        resultadoo="Paciente abaixo do peso!"
       elif temporario >= 25 and temporario < 30:
        resultadoo="Paciente no peso ideal"
       elif temporario >=30 and temporario < 35:
        resultadoo="Paciente acima do peso!"
       elif temporario >= 35 and temporario < 40:
        resultadoo="Paciente com grau de obesidade 1"
       elif temporario > 40:
        resultadoo="paciente com grau de obesidade 2"
       else:
         resultadoo="Paciente com grau de obesidade mórbida"
    except ValueError:
        resultadoo="por favor, insira um número válido"
        
    
    self.resultadolabel.config(text=resultadoo)
    # linha de código com o método delete, que começa do 0 e o "end" que vai até o fim do campo.
    self.entryPeso.delete(0 ,"end")
    self.entryAltura.delete(0, "end")
pagina=Tk()
calculoIMC(pagina)
pagina.mainloop()