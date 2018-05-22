from functools import partial
import tkinter as tk
from tkinter import *
from tkinter import ttk
from math import *
import time
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from numpy import arange, sin, pi

class cmru(tk.Tk):
    def __init__(self, master=None):
        global bgp
        self.explicar = 0
        self.ren = 0
        bgp = '#111111' #Background Padrão -->  Cinza    
        janela.resizable(width=False, height=False)
        janela['bg'] = '#111111'
        janela.title('Calculadora de Movimentos - Cinemática')
        self.tit = Label(janela, text="Calculadora de Movimento Retílineo Uniforme", bg = bgp)
        self.created = Label(janela, text = 'Created by - Carlos Daniel:', bg = bgp)
        self.created2 = Label(janela, text = 'Desenvolvido em Python', bg = bgp)
        self.tit['font'] = ('Arial Black', '20', 'bold')
        self.tit['fg'] = 'red'
        self.tit.place(x=105, y=10)
        #Label Copwright       
        self.created['font'] = ('Arial', '12', 'bold')
        self.created['fg'] = '#b40101'
        self.created.place(x=230, y=570)               
        self.created2['font'] = ('Arial', '12', 'bold')
        self.created2['fg'] = '#2004f4'
        self.created2.place(x=440, y=570)
        #Titulo
        self.painel()
    def painel(self):
        janela.geometry('900x600+300+100')
        self.tit.place(x=105, y=10)
        self.created.place(x=230, y=570)
        self.created2.place(x=440, y=570)
        self.estdp = Label(janela, text = 'Escolha um estilo de problema', bg = bgp)
        self.menu = Label(janela, text = 'Menu', bg = bgp)
        self.cbestdp = ttk.Combobox(janela, width = 50)
        self.cbestdp['state'] = 'readonly'     
        self.bche = Button(janela, text = 'Aplicar', width=30, height= 1,bd = 0, bg= '#00c6ba',\
            activebackground= '#fff', activeforeground = '#00c6ba', fg = '#fff')
        #Label Menu        
        self.menu['font'] = ('Comic Sans MS', '40', 'bold')
        self.menu['fg'] = 'orange'
        self.menu.place(x=385, y = 100)
        #Label Estilos de Problemas      
        self.estdp['font'] = ('Comic Sans MS', '26', 'bold')
        self.estdp['fg'] = 'green'
        self.estdp.place(x = 220, y = 200)
        #Combobox Estilo de Problemas       
        self.cbestdp['font'] = ('Comic Sans MS', '12', 'bold')
        self.cbestdp['values'] = ('Movimento Retílineo Uniforme', 'Movimento Retilíneo Uniformemente Variado', 'Velocidade Escalar Média')
        self.cbestdp.current(0)
        self.cbestdp.place(x = 210, y = 300)
        #Button Aplicar
        self.bche['font'] = ('Comic Sans MS', '18', 'bold')
        self.bche['command'] = self.chama_funcao
        self.bche.place(x=250, y = 360)
    def chama_funcao(self):
        try:
            valcb = self.cbestdp.get()
            valcb2 = self.cbestdp['values']
            if valcb == valcb2[0]:
                self.estdp.destroy()
                self.menu.destroy()
                self.cbestdp.destroy()
                self.bche.destroy()
                self.ren = 'es1'
                self.estilo1()
            elif valcb == valcb2[1]:
                self.estdp.destroy()
                self.menu.destroy()
                self.cbestdp.destroy()
                self.bche.destroy()
                self.ren = 'es2'
                self.estilo2()                  
            elif valcb == valcb2[2]:
                self.estdp.destroy()
                self.menu.destroy()
                self.cbestdp.destroy()
                self.bche.destroy()
                self.ren = 'es3'
                self.estilo3()              
        except:
            if self.ren == 'es1':
                self.posinic.destroy()
                self.posifin.destroy()
                self.veloc.destroy()
                self.tempo.destroy()
                self.unires.destroy()
                self.lresf.destroy()
                self.eds0.destroy()
                self.eds.destroy()
                self.edv.destroy()
                self.edt.destroy()
                self.cbs0.destroy()
                self.cbs.destroy()
                self.cbv.destroy()
                self.cbt.destroy()
                self.cbur.destroy()
                self.calcular.destroy()
                self.inic.destroy()
                self.restex.destroy()
                self.expl.destroy()
                self.grafico.destroy()
                self.explicar = 0
                self.painel()
            elif self.ren == 'es2':
                self.posinicv.destroy()
                self.posifinv.destroy()
                self.velocv.destroy()
                self.velocv0.destroy()
                self.tempov.destroy()
                self.aceleracao.destroy()
                self.uniresv.destroy()
                self.lresfv.destroy()
                self.eds0v.destroy()
                self.edsv.destroy()
                self.edvv.destroy()
                self.edvv0.destroy()
                self.edtv.destroy()
                self.edacv.destroy()
                self.cbs0v.destroy()
                self.cbsv.destroy()
                self.cbvv.destroy()
                self.cbvv0.destroy()
                self.cbtv.destroy()
                self.cburv.destroy()
                self.cbacv.destroy()
                self.calcularv.destroy()
                self.inicv.destroy()
                self.restexv.destroy()
                self.explv.destroy()
                self.explicarv = 0
                self.painel()            
    def estilo1(self):   
        #Variaveis      
        #Labels de variaveis     
        #Label s0
        self.posinic = Label(janela, text='Posição Inicial', bg = bgp)
        self.posinic['font'] = ('Arial', '12', 'bold')
        self.posinic['fg'] = '#ffb607'
        self.posinic.place(x=60, y= 110)
        #Label s
        self.posifin = Label(janela, text='Posição Final', bg = bgp)
        self.posifin['font'] = ('Arial', '12', 'bold')
        self.posifin['fg'] = '#ffb607'
        self.posifin.place(x=230, y= 110)
        #Label Velocidade
        self.veloc = Label(janela, text='Velocidade', bg = bgp)
        self.veloc['font'] = ('Arial', '12', 'bold')
        self.veloc['fg'] = '#ffb607'
        self.veloc.place(x=400, y= 110)
        #Label Tempo
        self.tempo = Label(janela, text='Tempo', bg = bgp)
        self.tempo ['font'] = ('Arial', '12', 'bold')
        self.tempo ['fg'] = '#ffb607'
        self.tempo.place(x=570, y= 110)
        #Label UnRe
        self.unires = Label(janela, text='Unidade Resultado', bg = bgp)
        self.unires ['font'] = ('Arial', '12', 'bold')
        self.unires ['fg'] = '#00edf0'
        self.unires.place(x=730, y= 110)
        #Label Resultado Final
        self.lresf = Label(janela, text='Resultado Final', bg = bgp, wraplength=1)
        self.lresf['font'] = ('Arial', '12', 'bold')
        self.lresf['fg'] = '#ff00ea'
        self.lresf.place(x=20, y= 200)       
        #Entrys
        #Entry s0
        self.eds0 = Entry(janela, width = 10)
        self.eds0['font'] = ('Comic Sans MS', '10')
        self.eds0['fg'] = 'red'
        self.eds0.place(x=60, y = 140)
        #Entry s
        self.eds = Entry(janela, width = 10)
        self.eds['font'] = ('Comic Sans MS', '10')
        self.eds['fg'] = 'red'
        self.eds.place(x=230, y = 140)
        #Entry Velocidade
        self.edv = Entry(janela, width = 10)
        self.edv['font'] = ('Comic Sans MS', '10')
        self.edv['fg'] = 'red'
        self.edv.place(x=400, y = 140)
        #Entry Tempo
        self.edt = Entry(janela, width = 10)
        self.edt['font'] = ('Comic Sans MS', '10')
        self.edt['fg'] = 'red'
        self.edt.place(x=570, y = 140)
        #Combobox
        #Combobox PosIni
        self.cbs0 = ttk.Combobox(janela, width = 5)
        self.cbs0['state'] = 'readonly'
        self.cbs0['values'] = ('m', 'Km')
        self.cbs0['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbs0.current(0)
        self.cbs0.place(x=150, y = 140)
        #Combobox Posfini
        self.cbs = ttk.Combobox(janela, width = 5)
        self.cbs['state'] = 'readonly'
        self.cbs['values'] = ('m', 'Km')
        self.cbs['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbs.current(0)
        self.cbs.place(x=320, y = 140)
        #Combobox Velo
        self.cbv = ttk.Combobox(janela, width = 5)
        self.cbv['state'] = 'readonly'
        self.cbv['values'] = ('m/s', 'Km/h')
        self.cbv['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbv.current(0)
        self.cbv.place(x=490, y = 140)
        #Combobox Tempo
        self.cbt = ttk.Combobox(janela, width = 5)
        self.cbt['state'] = 'readonly'
        self.cbt['values'] = ('s', 'h')
        self.cbt['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbt.current(0)
        self.cbt.place(x=660, y = 140)      
        #Combobox Unires
        self.cbur = ttk.Combobox(janela, width = 10)
        self.cbur['state'] = 'readonly'
        self.cbur['values'] = ('S.I', 'Km/h - Km')
        self.cbur['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbur.current(0)
        self.cbur.place(x=760, y= 140)        
        #Botoes
        #Inicio
        self.inic = Button(janela, text='Início', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.inic['command'] = self.chama_funcao
        self.inic['font'] = ('Comic Sans MS', '11')
        self.inic.place(x=770, y=510)
        #Botao Calcular
        self.calcular = Button(janela, text='Calcular', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.calcular['command'] = self.calc
        self.calcular['font'] = ('Comic Sans MS', '11')
        self.calcular.place(x=470, y=510)
        #Explicação
        self.expl = Button(janela, text='Explicação', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.expl['command'] = self.expli
        self.expl['font'] = ('Comic Sans MS', '11')
        self.expl.place(x=670, y=510)
        #Gráfico
        self.grafico = Button(janela, text='Gráfico', width = 10, height = 1, bd = 0, bg = '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.grafico['command'] = self.grafic
        self.grafico['font'] = ('Comic Sans MS', '11')
        self.grafico.place(x=570, y= 510)
        #TextBox Resultado Final
        self.restex = Text(janela, width = 80, height = 12)
        self.restex['font'] = ('Comic Sans MS', '12', 'bold')
        self.restex['state'] = 'disable'
        self.restex.place(x= 60, y = 200)
        self.graficse = 0
    def grafic(self):
        if self.graficse == 1:
            f = Figure(figsize=(5, 5), dpi=100)
            gr = f.add_subplot(111)
            x = [i for i in range(0, 101)]
            y = [(self.s0+(self.v*i)) for i in x]
            gr.grid(True)
            gr.plot(x, y)
            gr.set_title('Gráfico das Posições em Função do Tempo - MRU')
            gr.set_xlabel('X Tempo')
            gr.set_ylabel('Y Posição')
            self.canvas = FigureCanvasTkAgg(f, master=janela)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
            self.toolbar = NavigationToolbar2TkAgg(self.canvas, janela)
            self.toolbar.update()
            self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
            self.voltar1 = Button(master=janela, text='Voltar', width = 128, height = 1, command=self.limpgrafic)
            self.voltar1.pack(side=BOTTOM)
        elif self.graficse == 2:
            f = Figure(figsize=(5, 5), dpi=100)
            gr = f.add_subplot(111)
            x = [i for i in range(0, 100)]
            y = [(self.s0+(self.v0*i)+((self.a/2)*(i**2))) for i in x]
            gr.grid(True)
            gr.plot(x, y)
            gr.set_title('Gráfico das Posições em Função do Tempo - MRUV')
            gr.set_xlabel('X Tempo')
            gr.set_ylabel('Y Posição')
            self.canvas = FigureCanvasTkAgg(f, master=janela)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
            self.toolbar = NavigationToolbar2TkAgg(self.canvas, janela)
            self.toolbar.update()
            self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
            self.voltar1 = Button(master=janela, text='Voltar', width = 200, height = 2, bd = 0, bg = '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff', command=self.limpgrafic)
            self.voltar1['font'] = ('Comic Sans MS', '12', 'bold')
            self.voltar1.pack(side=BOTTOM)            
    def limpgrafic(self):
        self.canvas.get_tk_widget().destroy()
        self.toolbar.destroy()
        self.voltar1.destroy()
    def veres(self):
        self.expl['text'] = 'Explicação'
        self.expl['command'] = self.expli
        self.restex['state'] = 'normal'
        self.restex.delete(0.0, 'end')
        self.restex.insert(0.0, self.resulfin)
        self.restex['state'] = 'disable'
        self.restex['foreground'] = 'black'
    def expli(self):
        self.a = self.explicar
        if self.a == 0:
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, 'Pare de tentar achar um bug e coloque o seu problema :)')
            self.restex['state'] = 'disable'
        elif self.a == 1:
            self.mp = float(self.v*self.t)
            self.reexp = float(self.s0+self.mp)
            self.t = round(self.t, 4)
            self.reexp = round(self.reexp, 4)

            self.resulfin2 = ('Primeiro transformamos cada valor na UNIDADE REQUERIDA\n'
                             's0 = '+str(self.s01)+str(self.us01)+' ≡ '+str(self.s0)+str(self.us0)+' ---> m para Km ≡ m ÷ 1000 | Km para m ≡ Km * 1000\n'
                             'v = '+str(self.v1)+str(self.uv1)+' ≡ '+str(self.v)+str(self.uv)+' ---> m/s para Km/h ≡ m/s * 3,6 | Km/h para m/s ≡ Km/h ÷ 3,6\n'
                             't = '+self.t1+str(self.ut1)+' ≡ '+str(self.t)+str(self.ut)+' ---> s para h ≡ s ÷ 3600 | h para s ≡ h * 3600\n\n'
                             'Após isto iremos resolver a seguinte equação: s = '+str(self.s0)+str(self.us0)+' + ('+str(self.v)+str(self.uv)+' * '+str(self.t)+str(self.ut)+')\n'
                             's = '+str(self.s0)+str(self.us0)+' + '+str(self.mp)+str(self.us0)+'\n'
                             's = '+str(self.reexp)+str(self.us0))
            self.expl['text'] = 'Ver Resposta'
            self.expl['command'] = self.veres
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, self.resulfin2)
            self.restex.tag_add('req', '1.45', '1.54')
            self.restex.tag_config("req", foreground="red")
            self.restex.tag_add('uni', '1.36', '1.44')
            self.restex.tag_config('uni', foreground='blue')
            self.restex['state'] = 'disable'
        elif self.a == 2:
            self.mp = float(self.s-self.s0)
            self.reexp = float(self.mp/self.v)
            self.reexp = round(self.reexp, 4)
            self.resulfin2 = ('Primeiro transformamos cada valor na UNIDADE REQUERIDA\n'
                               's0 = '+str(self.s01)+str(self.us01)+' ≡ '+str(self.s0)+str(self.us0)+' ---> m para Km ≡ m ÷ 1000 | Km para m ≡ Km * 1000\n'
                               'v = '+str(self.v1)+str(self.uv1)+' ≡ '+str(self.v)+str(self.uv)+' ---> m/s para Km/h ≡ m/s * 3,6 | Km/h para m/s ≡ Km/h ÷ 3,6\n'
                               's = '+str(self.s1)+str(self.us1)+' ≡ '+str(self.s)+str(self.us)+' ---> m para Km ≡ m ÷ 1000 | Km para m ≡ Km * 1000\n\n'
                               'Após isto iremos resolver a seguinte equação:\nt = ('+str(self.s)+str(self.us)+' - ('+str(self.s0)+str(self.us0)+')/('+str(self.v)+str(self.uv)+')\n'
                               't = '+str(self.mp)+str(self.us0)+'/('+str(self.v)+str(self.uv)+')\n'
                               't = '+str(self.reexp)+str(self.ut)+' (aproximado)')
            self.expl['text'] = 'Ver Resposta'
            self.expl['command'] = self.veres
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, self.resulfin2)
            self.restex.tag_add('req', '1.45', '1.54')
            self.restex.tag_config("req", foreground="red")
            self.restex.tag_add('uni', '1.36', '1.44')
            self.restex.tag_config('uni', foreground='blue')
            self.restex['state'] = 'disable'
        elif self.a == 3:
            self.mp = float(self.s-self.s0)
            self.reexp = float(self.mp/self.t) 
            self.reexp = round(self.reexp, 4)
            self.t = round(self.t, 4)
            self.mp = round(self.mp, 4)
            self.resulfin2 = ('Primeiro transformamos cada valor na UNIDADE REQUERIDA\n'
                               's0 = '+str(self.s01)+str(self.us01)+' ≡ '+str(self.s0)+str(self.us0)+' ---> m para Km ≡ m ÷ 1000 | Km para m ≡ Km * 1000\n'
                               's = '+str(self.s1)+str(self.us1)+' ≡ '+str(self.s)+str(self.us)+' ---> m para Km ≡ m ÷ 1000 | Km para m ≡ Km * 1000\n'
                               't = '+self.t1+str(self.ut1)+' ≡ '+str(self.t)+str(self.ut)+' ---> s para h ≡ s ÷ 3600 | h para s ≡ h * 3600\n\n'
                               'Após isto iremos resolver a seguinte equação:\nv = ('+str(self.s)+str(self.us)+' - ('+str(self.s0)+str(self.us0)+')/('+str(self.t)+str(self.ut)+')\n'
                               'v = '+str(self.mp)+str(self.us0)+'/('+str(self.t)+str(self.ut)+')\n'
                               'v = '+str(self.reexp)+str(self.uv)+' (aproximado)')
            self.expl['text'] = 'Ver Resposta'
            self.expl['command'] = self.veres
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, self.resulfin2)
            self.restex.tag_add('req', '1.45', '1.54')
            self.restex.tag_config("req", foreground="red")
            self.restex.tag_add('uni', '1.36', '1.44')
            self.restex.tag_config('uni', foreground='blue')
            self.restex['state'] = 'disable'
        elif self.a == 4:
            self.mp = float(self.v*self.t)
            self.reexp = float(self.s-self.mp) 
            self.reexp = round(self.reexp, 4)
            self.t = round(self.t, 4)
            self.mp = round(self.mp, 4)
            self.resulfin2 = ('Primeiro transformamos cada valor na UNIDADE REQUERIDA\n'
                               's = '+str(self.s1)+str(self.us1)+' ≡ '+str(self.s)+str(self.us)+' ---> m para Km ≡ m ÷ 1000 | Km para m ≡ Km * 1000\n'
                               'v = '+str(self.v1)+str(self.uv1)+' ≡ '+str(self.v)+str(self.uv)+' ---> m/s para Km/h ≡ m/s * 3,6 | Km/h para m/s ≡ Km/h ÷ 3,6\n'
                               't = '+self.t1+str(self.ut1)+' ≡ '+str(self.t)+str(self.ut)+' ---> s para h ≡ s ÷ 3600 | h para s ≡ h * 3600\n\n'
                               'Após isto iremos resolver a seguinte equação:\ns0 = '+str(self.s)+str(self.us)+' - ('+str(self.v)+str(self.uv)+' * '+str(self.t)+str(self.ut)+')\n'
                               's0 = '+str(self.s)+str(self.us)+' - ('+str(self.mp)+str(self.us)+')\n'
                               's0 = '+str(self.reexp)+str(self.us)+' (aproximado)')
            self.expl['text'] = 'Ver Resposta'
            self.expl['command'] = self.veres
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, self.resulfin2)
            self.restex.tag_add('req', '1.45', '1.54')
            self.restex.tag_config("req", foreground="red")
            self.restex.tag_add('uni', '1.36', '1.44')
            self.restex.tag_config('uni', foreground='blue')
            self.restex['state'] = 'disable'                
    def calc(self):
        programa = 'MRU: '
        s = self.eds.get()
        s0 = self.eds0.get()
        v = self.edv.get()
        t = self.edt.get()
        sc = self.eds.get()
        s0c = self.eds0.get()
        vc = self.edv.get()
        tc = self.edt.get()
        us0 = self.cbs0.get()
        us = self.cbs.get()
        uv = self.cbv.get()
        ut = self.cbt.get()
        urf = self.cbur.get()
        self.s1 = s
        self.s01 = s0
        self.v1 = v
        self.t1 = t
        self.us01 = us0
        self.us1 = us
        self.uv1 = uv
        self.ut1 = ut
        s0c = s0c+us0
        tc = tc+ut
        vc = vc+uv
        sc = sc+us
        if urf == 'S.I':
            if us0 == 'Km':
                try:
                    s0 = float(s0)
                    s0 *= 1000
                    us0 = 'm'
                except ValueError:
                    us0 = 'm'
                    s0 = None
                    None
            elif us0 == 'm':
                try:
                    s0 = float(s0)
                except ValueError:
                    s0 = None             
            if us == 'Km':
                try:
                    s = float(s)
                    s *= 1000
                    us = 'm'
                except ValueError:
                    us = 'm'
                    s = None
                    None
            elif us == 'm':
                try:
                    s = float(s)
                except ValueError:
                    s = None   
            if uv == 'Km/h':
                try:
                    v = float(v)
                    v /= 3.6
                    uv = 'm/s'
                except ValueError:
                    uv = 'm/s'
                    v = None
                    None
            elif uv == 'm/s':
                try:
                    v = float(v)
                except ValueError:
                    v = None    
            if ut == 'h':
                try:
                    t = float(t)
                    t *= 3600
                    ut = 's'
                except ValueError:
                    ut = 's'
                    t = None
                    None
            elif ut == 's':
                try:
                    t = float(t)
                except ValueError:
                    t = None    
        elif urf == 'Km/h - Km':
            if us0 == 'm':
                try:
                    s0 = float(s0)
                    s0 /= 1000
                    us0 = 'Km'
                except ValueError:
                    us0 = 'Km'
                    s0 = None
                    None
            elif us0 == 'Km':
                try:
                    s0 = float(s0)
                except ValueError:
                    s0 = None             
            if us == 'm':
                try:
                    s = float(s)
                    s /= 1000
                    us = 'Km'
                except ValueError:
                    us = 'Km'
                    s = None
                    None
            elif us == 'Km':
                try:
                    s = float(s)
                except ValueError:
                    s = None    
            if uv == 'm/s':
                try:
                    v = float(v)
                    v *= 3.6
                    uv = 'Km/h'
                except ValueError:
                    uv = 'Km/h'
                    v = None
                    None
            elif uv == 'Km/h':
                try:
                    v = float(v)
                except ValueError:
                    v = None    
            if ut == 's':
                try:
                    t = float(t)
                    t /= 3600
                    ut = 'h'
                except ValueError:
                    ut = 'h'
                    t = None
                    None
            elif ut == 'h':
                try:
                    t = float(t)
                except ValueError:
                    t = None
        self.s = s
        self.s0 = s0
        self.v = v
        self.t = t
        self.us0 = us0
        self.us = us
        self.uv = uv
        self.ut = ut
        if s0 != None and v != None and t != None and s == None:
            s = s0 + (v * t)
            self.s = s    
            self.explicar = 1
            self.grafics = 1
            resulfin = ('Função Horária: s = %s + (%s . Δt)'
                       '\nAs variaveis em t = %s serao:'
                       '\ns0 = %s'
                       '\ns = %.2f%s'
                       '\nv = %s'
                       '\nt = %s' % (s0c, vc, tc, s0c, s, us, vc, tc))     
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, resulfin)
            self.restex['state'] = 'disable'
            self.resulfin = resulfin
            self.graficse = 1
        elif s0 != None and v != None and t == None and s != None:
            if s0 >= 0:
                t = (s-s0)/v
            elif s0 < 0:
                s0 *= -1
                t = (s+s0)/v
            if t < 0:
                self.restex['state'] = 'normal'
                self.restex.delete(0.0, 'end')
                self.restex.insert(0.0, 'As informações estão incorretas:\nO resultado do tempo está ficando negativo\nTente colocar a velocidade negativa')
                self.restex['state'] = 'disable'
            else:
                self.t = t
                resulfin = ('Função Horária: s = %s + (%s . Δt)'
                           '\nAs variaveis em s = %.2f%s serao:'
                           '\ns0 = %s'
                           '\ns = %s '
                           '\nv = %s'
                           '\nt = %.4f%s (aproximado)' % (s0c, vc, s, us, s0c, sc,vc, t, ut))               
                self.restex['state'] = 'normal'
                self.restex.delete(0.0, 'end')
                self.restex.insert(0.0, resulfin)
                self.restex['state'] = 'disable'
                self.resulfin = resulfin
                self.explicar = 2
                self.graficse = 1
        elif s0 != None and v == None and t != None and s != None :
            if s0 >= 0:
                v = (s-s0)/t
            elif s0 < 0:
                s0 *= -1
                v = (s+s0)/t            
            self.v = v
            resulfin = ('Função Horária: s = %s + (%.2f%s . Δt)'
                       '\nAs variaveis em t = %s serao:'
                       '\ns0 = %s'
                       '\ns = %s'
                       '\nv = %.2f%s (aproximado)'
                       '\nt = %s' % (s0c, v, uv, tc, s0c, sc, v, uv, tc))
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, resulfin)
            self.restex['state'] = 'disable'
            self.resulfin = resulfin
            self.explicar = 3
            self.graficse = 1
        elif s0 == None and v != None and t != None and s != None:
            if v*t > 0:
                s0 = s-(v*t)
            elif v*t < 0:
                s0 = s-(v*t)
            elif v*t == 0:
                s0 = s
            resulfin = ('Função Horária: s = %.2f%s + (%s . Δt)'
                       '\nAs variaveis em t = %s serao:'
                       '\ns0 = %.2f%s'
                       '\ns = %s'
                       '\nv = %s'
                       '\nt = %s' % (s0, us0, vc, tc, s0, us0, sc, vc, tc))
            self.resulfin = resulfin
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, resulfin)
            self.restex['state'] = 'disable'
            self.explicar = 4
            self.graficse = 1
        else:
            self.explicar = 0
            self.graficse = 0
            self.resulfin = 'Você realmente está tentando achar algum bug em'
            self.restex['state'] = 'normal'
            self.restex.delete(0.0, 'end')
            self.restex.insert(0.0, 'Informe o valor de 3 variáveis')
            self.restex['state'] = 'disable'
        self.s = s
        self.s0 = s0
        self.v = v
        self.t = t        
    def estilo2(self):
        janela.geometry('1300x600+200+100')
        self.tit.place(x=250, y=10)
        self.created.place(x=375, y=570)
        self.created2.place(x=585, y=570)
        #Variaveis
        #Labels de variaveis
        #Label s0
        self.posinicv = Label(janela, text='Posição Inicial', bg = bgp)
        self.posinicv['font'] = ('Arial', '12', 'bold')
        self.posinicv['fg'] = '#ffb607'
        self.posinicv.place(x=60, y= 110)
        #Label s
        self.posifinv = Label(janela, text='Posição Final', bg = bgp)
        self.posifinv['font'] = ('Arial', '12', 'bold')
        self.posifinv['fg'] = '#ffb607'
        self.posifinv.place(x=230, y= 110)
        #Label Velocidade
        self.velocv = Label(janela, text='Velocidade', bg = bgp)
        self.velocv['font'] = ('Arial', '12', 'bold')
        self.velocv['fg'] = '#ffb607'
        self.velocv.place(x=400, y= 110)
        #Label Velocidade Inicial
        self.velocv0 = Label(janela, text = 'Velocidade Inicial', bg = bgp)
        self.velocv0['font'] = ('Arial', '12', 'bold')
        self.velocv0['fg'] = '#ffb607'
        self.velocv0.place(x=570, y= 110)
        #Label Tempo
        self.tempov = Label(janela, text='Tempo', bg = bgp)
        self.tempov ['font'] = ('Arial', '12', 'bold')
        self.tempov ['fg'] = '#ffb607'
        self.tempov.place(x=910, y= 110)
        #Label Aceleração
        self.aceleracao = Label(janela, text='Aceleração', bg = bgp)
        self.aceleracao ['font'] = ('Arial', '12', 'bold')
        self.aceleracao ['fg'] = '#ffb607'
        self.aceleracao.place(x=740, y= 110)
        #Label UnRe
        self.uniresv = Label(janela, text='Unidade Resultado', bg = bgp)
        self.uniresv ['font'] = ('Arial', '12', 'bold')
        self.uniresv ['fg'] = '#00edf0'
        self.uniresv.place(x=1080, y= 110)
        #Label Resultado Final
        self.lresfv = Label(janela, text='Resultado Final', bg = bgp, wraplength=1)
        self.lresfv['font'] = ('Arial', '12', 'bold')
        self.lresfv['fg'] = '#ff00ea'
        self.lresfv.place(x=20, y= 200)
        #Entrys
        #Entry s0
        self.eds0v = Entry(janela, width = 10)
        self.eds0v['font'] = ('Comic Sans MS', '10')
        self.eds0v['fg'] = 'red'
        self.eds0v.place(x=60, y = 140)
        #Entry s
        self.edsv = Entry(janela, width = 10)
        self.edsv['font'] = ('Comic Sans MS', '10')
        self.edsv['fg'] = 'red'
        self.edsv.place(x=230, y = 140)
        #Entry Velocidade
        self.edvv = Entry(janela, width = 10)
        self.edvv['font'] = ('Comic Sans MS', '10')
        self.edvv['fg'] = 'red'
        self.edvv.place(x=400, y = 140)
        #Entry Velocidade Inicial
        self.edvv0 = Entry(janela, width = 10)
        self.edvv0['font'] = ('Comic Sans MS', '10')
        self.edvv0['fg'] = 'red'
        self.edvv0.place(x=570, y = 140)        
        #Entry Tempo
        self.edtv = Entry(janela, width = 10)
        self.edtv['font'] = ('Comic Sans MS', '10')
        self.edtv['fg'] = 'red'
        self.edtv.place(x=910, y = 140)
        #Entry Aceleração
        self.edacv = Entry(janela, width = 10)
        self.edacv['font'] = ('Comic Sans MS', '10')
        self.edacv['fg'] = 'red'
        self.edacv.place(x=740, y = 140)
        #Combobox
        #Combobox PosIni
        self.cbs0v = ttk.Combobox(janela, width = 5)
        self.cbs0v['state'] = 'readonly'
        self.cbs0v['values'] = ('m', 'Km')
        self.cbs0v['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbs0v.current(0)
        self.cbs0v.place(x=150, y = 140)
        #Combobox Posfini
        self.cbsv = ttk.Combobox(janela, width = 5)
        self.cbsv['state'] = 'readonly'
        self.cbsv['values'] = ('m', 'Km')
        self.cbsv['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbsv.current(0)
        self.cbsv.place(x=320, y = 140)
        #Combobox Velo
        self.cbvv = ttk.Combobox(janela, width = 5)
        self.cbvv['state'] = 'readonly'
        self.cbvv['values'] = ('m/s', 'Km/h')
        self.cbvv['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbvv.current(0)
        self.cbvv.place(x=490, y = 140)
        self.cbvv0 = ttk.Combobox(janela, width = 5)
        self.cbvv0['state'] = 'readonly'
        self.cbvv0['values'] = ('m/s', 'Km/h')
        self.cbvv0['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbvv0.current(0)
        self.cbvv0.place(x=660, y = 140)
        #Combobox Tempo
        self.cbtv = ttk.Combobox(janela, width = 5)
        self.cbtv['state'] = 'readonly'
        self.cbtv['values'] = ('s', 'h')
        self.cbtv['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtv.current(0)
        self.cbtv.place(x=1000, y = 140)
        #Combobox Aceleração
        self.cbacv = ttk.Combobox(janela, width = 5)
        self.cbacv['state'] = 'readonly'
        self.cbacv['values'] = ('m/s²')
        self.cbacv['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbacv.current(0)
        self.cbacv.place(x = 830, y = 140)
        #Combobox Unires
        self.cburv = ttk.Combobox(janela, width = 10)
        self.cburv['state'] = 'readonly'
        self.cburv['values'] = ('S.I', 'Km/h - Km')
        self.cburv['font'] = ('Comic Sans MS', '9', 'bold')
        self.cburv.current(0)
        self.cburv.place(x=1110, y= 140)
        #Botoes
        #Inicio
        self.inicv = Button(janela, text='Início', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.inicv['command'] = self.chama_funcao
        self.inicv['font'] = ('Comic Sans MS', '11')
        self.inicv.place(x=1137, y=520)
        #Botao Calcular
        self.calcularv = Button(janela, text='Calcular', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.calcularv['command'] = self.calc2
        self.calcularv['font'] = ('Comic Sans MS', '11')
        self.calcularv.place(x=837, y=520)
        #Explicação
        self.explv = Button(janela, text='Explicação', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.explv['command'] = self.expli2
        self.explv['font'] = ('Comic Sans MS', '11')
        self.explv.place(x=1037, y=520)
        #TextBox Resultado Final
        self.restexv = Text(janela, width = 117, height = 14)
        self.restexv['font'] = ('Comic Sans MS', '12', 'bold')
        self.restexv['state'] = 'disable'
        self.restexv.place(x= 60, y = 180)
        #Gráfico
        self.grafico = Button(janela, text='Gráfico', width = 10, height = 1, bd = 0, bg = '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.grafico['command'] = self.grafic
        self.grafico['font'] = ('Comic Sans MS', '11')
        self.grafico.place(x=937, y= 520)
        self.graficse = 0
    def calc2(self):
        s = self.edsv.get()
        s0 = self.eds0v.get()
        v = self.edvv.get()
        v0 = self.edvv0.get()
        a = self.edacv.get()
        t = self.edtv.get()
        us0 = self.cbs0v.get()
        us = self.cbsv.get()
        uv = self.cbvv.get()
        uv0 = self.cbvv0.get()
        ua = self.cbacv.get()
        ut = self.cbtv.get()
        urf =  self.cburv.get()
        if urf == 'S.I':
            if us0 == 'Km':
                try:
                    s0 = float(s0)
                    s0 *= 1000
                    us0 = 'm'
                except ValueError:
                    us0 = 'm'
                    s0 = None
                    None
            elif us0 == 'm':
                try:
                    s0 = float(s0)
                except ValueError:
                    s0 = None             
            if us == 'Km':
                try:
                    s = float(s)
                    s *= 1000
                    us = 'm'
                except ValueError:
                    us = 'm'
                    s = None
                    None
            elif us == 'm':
                try:
                    s = float(s)
                except ValueError:
                    s = None   
            if uv == 'Km/h':
                try:
                    v = float(v)
                    v /= 3.6
                    uv = 'm/s'
                except ValueError:
                    uv = 'm/s'
                    v = None
                    None
            elif uv == 'm/s':
                try:
                    v = float(v)
                except ValueError:
                    v = None                    
            if uv0 == 'Km/h':
                try:
                    v0 = float(v0)
                    v0 /= 3.6
                    uv0 = 'm/s'
                except ValueError:
                    uv0 = 'm/s'
                    v0 = None
                    None                    
            elif uv0 == 'm/s':
                try:
                    v0 = float(v0)
                except ValueError:
                    v0 = None    
            if ut == 'h':
                try:
                    t = float(t)
                    t *= 3600
                    ut = 's'
                except ValueError:
                    ut = 's'
                    t = None
                    None
            elif ut == 's':
                try:
                    t = float(t)
                except ValueError:
                    t = None
            try:
                a = float(a)
            except ValueError:
                a = None
        elif urf == 'Km/h - Km':
            if us0 == 'm':
                try:
                    s0 = float(s0)
                    s0 /= 1000
                    us0 = 'Km'
                except ValueError:
                    us0 = 'Km'
                    s0 = None
                    None
            elif us0 == 'Km':
                try:
                    s0 = float(s0)
                except ValueError:
                    s0 = None             
            if us == 'm':
                try:
                    s = float(s)
                    s /= 1000
                    us = 'Km'
                except ValueError:
                    us = 'Km'
                    s = None
                    None
            elif us == 'Km':
                try:
                    s = float(s)
                except ValueError:
                    s = None    
            if uv == 'm/s':
                try:
                    v = float(v)
                    v *= 3.6
                    uv = 'Km/h'
                except ValueError:
                    uv = 'Km/h'
                    v = None
                    None
            elif uv == 'Km/h':
                try:
                    v = float(v)
                except ValueError:
                    v = None
            if uv0 == 'm/s':
                try:
                    v0 = float(v0)
                    v0 *= 3.6
                    uv0 = 'Km/h'
                except ValueError:
                    uv0 = 'Km/h'
                    v0 = None
                    None
            elif uv0 == 'Km/h':
                try:
                    v0 = float(v0)
                except ValueError:
                    v0 = None   
            if ut == 's':
                try:
                    t = float(t)
                    t /= 3600
                    ut = 'h'
                except ValueError:
                    ut = 'h'
                    t = None
                    None
            elif ut == 'h':
                try:
                    t = float(t)
                except ValueError:
                    t = None
            try:
                a = float(a)
            except ValueError:
                a = None
        if s0 != None and s == None and a != None and t != None and v == None and v0 != None:
            s = s0 + v0*t + ((a*(t*t))/2)
            v =  v0 + (a*t)
            self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                             '\n\nPara t = {}s'
                             '\ns = {}m'
                             '\ns0 = {}m'
                             '\nv = {}m/s'
                             '\nv0 = {}m/s'
                             '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin)
            self.restexv.tag_add('form', '1.16', '1.end')
            self.restexv.tag_config('form', foreground='purple')
            self.restexv['state'] = 'disable'
            self.graficse = 2
            self.explicar2 = 1
        elif s0 != None and s != None and a != None and t == None and v != None and v0 == None:
            st1 = s - s0
            st = s0 - s
            v0 = (v**2)-(2*a*st1)
            ac = a / 2            
            if v0 >= 0:
                v0 = v0 ** (1/2)
                if v0 == 0:
                    self.estado = 0
                    t = (((2*s) - (2*s0))/a) ** (1/2)
                    self.restexv['state'] = 'normal'
                    self.restexv.delete(0.0, 'end')
                    self.restexv['state'] = 'disable' 
                else:
                    self.estado = 1
                    delta = (v0**2) + (-4*ac*st)
                    if delta > 0:
                        t1 = (-(v0) + sqrt(delta))/(2*ac)
                        t2 = (-(v0) - sqrt(delta))/(2*ac)
                        self.restexv['state'] = 'normal'
                        self.restexv.delete(0.0, 'end')
                        self.restexv['state'] = 'disable' 
                        if t1 > 0:
                            t = t1
                        elif t2 > 0:
                            t = t2
                        else:
                            self.restexv['state'] = 'normal'
                            self.restexv.delete(0.0, 'end')
                            self.restexv.insert(0.0, '\nt1 = {} e t2 = {}, sendo impossivel calcular o tempo'.format(t1, t2))
                            self.restexv['state'] = 'disable' 
                    elif delta == 0:
                        t = (-(v0) + sqrt(delta))/(2*ac)
                        self.restexv.delete(0.0, 'end')
                    elif delta < 0:
                        self.restexv['state'] = 'normal'
                        self.restexv.delete(0.0, 'end')
                        self.restexv.insert(0.0, '\nDelta é negativo, nao tendo como calcular raiz de num negativo')
                        self.restexv['state'] = 'disable'  
                    else:
                        self.restexv['state'] = 'normal'
                        self.restexv.delete(0.0, 'end')
                        self.restexv.insert(0.0, '\nVocê é um ninja e conseguiu fazer com que o delta nao seja positivo, nem negativo nem nulo\n Vc e um novo inventor da matematica')
                        self.restexv.insert('end', '\nDelta = {}'.format(delta))
                        self.restexv['state'] = 'disable'                          
                if t == None:
                    t = 'Não é possível ser calculado'
                self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                                 '\n\nPara t = {}s'
                                 '\ns = {}m'
                                 '\ns0 = {}m'
                                 '\nv = {}m/s'
                                 '\nv0 = {}m/s'
                                 '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
                self.restexv['state'] = 'normal'
                self.restexv.insert(0.0, self.resulfin)
                self.restexv.tag_add('form', '1.16', '1.end')
                self.restexv.tag_config('form', foreground='purple')
                self.restexv['state'] = 'disable'
                self.graficse = 2
                self.explicar2 = 2
            else:
                self.restexv['state'] = 'normal'
                self.restexv.delete(0.0, 'end')
                self.restexv.insert(0.0, 'Não é possível calcular, tente um outro valor')
                self.restexv['state'] = 'disable'      
        elif s0 != None and s!= None and a == None and t == None and v != None and v0 != None:
            ds = s - s0
            a = ((v**2) - (v0**2))/(2*ds)
            ac = a / 2
            st = s0 - s
            delta = (v0**2) + (-4*ac*st)
            if delta > 0:
                t1 = (-(v0) + sqrt(delta))/(2*ac)
                t2 = (-(v0) - sqrt(delta))/(2*ac)
                if t1 > 0:
                    t = t1
                    self.restexv['state'] = 'normal'
                    self.restexv.delete(0.0, 'end')
                    self.restexv['state'] = 'disable'
                elif t2 > 0:
                    t = t2
                    self.restexv['state'] = 'normal'
                    self.restexv.delete(0.0, 'end')
                    self.restexv['state'] = 'disable'
                else:
                    self.restexv['state'] = 'normal'
                    self.restexv.delete(0.0, 'end')
                    self.restexv.insert(0.0, '\nt1 = {} e t2 = {}, sendo impossivel calcular o tempo'.format(t1, t2))
                    self.restexv['state'] = 'disable' 
            elif delta == 0:
                t = (-(v0) + sqrt(delta))/(2*ac)
                self.restexv['state'] = 'normal'
                self.restexv.delete(0.0, 'end')
                self.restexv['state'] = 'disable'
            elif delta < 0:
                self.restexv['state'] = 'normal'
                self.restexv.delete(0.0, 'end')
                self.restexv.insert(0.0, '\nDelta é negativo, nao tendo como calcular raiz de num negativo')
                self.restexv['state'] = 'disable'  
            else:
                self.restexv['state'] = 'normal'
                self.restexv.delete(0.0, 'end')
                self.restexv.insert(0.0, '\nVocê é um ninja e conseguiu fazer com que o delta nao seja positivo, nem negativo nem nulo\n Vc e um novo inventor da matematica')
                self.restexv.insert('end', '\nDelta = {}'.format(delta))
                self.restexv['state'] = 'disable'  
            if t == None:
                t = 'Não foi possivel calcular'
            self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                             '\n\nPara t = {}s'
                             '\ns = {}m'
                             '\ns0 = {}m'
                             '\nv = {}m/s'
                             '\nv0 = {}m/s'
                             '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
            self.restexv['state'] = 'normal'
            self.restexv.insert(0.0, self.resulfin)
            self.restexv.tag_add('form', '1.16', '1.end')
            self.restexv.tag_config('form', foreground='purple')
            self.restexv['state'] = 'disable'
            self.graficse = 2
            self.explicar2 = 3
        elif s0 != None and s != None and v == None and v0 != None and a != None and t == None:
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            ac = a / 2
            st = s0 - s
            st1 = round(s - s0, 9)
            v = sqrt((v0**2) + (2*a*st1))
            if v0 == 0:
                t1 = +((((2*s) - (2*s0))/a) ** (1/2))
                t2 = -((((2*s) - (2*s0))/a) ** (1/2))
                if t1 > 0:
                    t = t1
                elif t2 > 0:
                    t = t2  
                else:
                    self.restexv.delete(0.0, 'end')
                    self.restexv.insert(0.0, '\nt1 = {} e t2 = {}, na física não existe tempo negativo'.format(t1, t2))                                  
            elif v0 != 0:
                delta = (v0**2) + (-4*ac*st)
                if delta > 0:
                    t1 = (-(v0) + sqrt(delta))/(2*ac)
                    t2 = (-(v0) - sqrt(delta))/(2*ac)
                    if t1 > 0:
                        t = t1
                    elif t2 > 0:
                        t = t2
                    else:
                        self.restexv.delete(0.0, 'end')
                        self.restexv.insert(0.0, '\nt1 = {} e t2 = {}, na física não existe tempo negativo'.format(t1, t2))            
                elif delta == 0:
                    t = (-(v0) + sqrt(delta))/(2*ac)    
                elif delta < 0:
                    self.restexv.delete(0.0, 'end')
                    self.restexv.insert(0.0, '\nDelta é negativo, nao tendo como calcular raiz de num negativo')
                else:
                    self.restexv.delete(0.0, 'end')
                    self.restexv.insert(0.0, '\nVocê é um ninja e conseguiu fazer com que o delta nao seja positivo, nem negativo nem nulo\n Vc e um novo inventor da matematica')
                    self.restexv.insert('end', '\nDelta = {}'.format(delta))
            self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                             '\n\nPara t = {}s'
                             '\ns = {}m'
                             '\ns0 = {}m'
                             '\nv = {}m/s'
                             '\nv0 = {}m/s'
                             '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
            self.restexv.insert(0.0, self.resulfin)
            self.restexv.tag_add('form', '1.16', '1.end')
            self.restexv.tag_config('form', foreground='purple')
            self.restexv['state'] = 'disable'
            self.graficse = 2
            self.explicar2 = 4
        elif s0 != None and s == None and v != None and v0 != None and a != None and t == None:
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            t = (v-v0)/a
            s = s0 + (v0*t) + ((a/2)*(t**2))
            self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                             '\n\nPara t = {}s'
                             '\ns = {}m'
                             '\ns0 = {}m'
                             '\nv = {}m/s'
                             '\nv0 = {}m/s'
                             '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
            self.restexv['state'] = 'normal'
            self.restexv.insert(0.0, self.resulfin)
            self.restexv.tag_add('form', '1.16', '1.end')
            self.restexv.tag_config('form', foreground='purple')
            self.restexv['state'] = 'disable'
            self.graficse = 2
            self.explicar2 = 5
        elif s0 == None and s != None and v != None and v0 != None and a != None and t == None:
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            t = (v-(v0))/a
            if t < 0:
                self.restexv.insert(0.0, '\n\nFilhão, você deve ter errado os dados, o tempo está dando negativo\n')
                self.restexv.tag_add('filho', '2.9', '3.90')
                self.restexv.tag_config('filho', foreground='red')
            ac = a/2
            s0 = (-(v0)*t) - (ac*(t**2)) + s
            self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                             '\n\nPara t = {}s'
                             '\ns = {}m'
                             '\ns0 = {}m'
                             '\nv = {}m/s'
                             '\nv0 = {}m/s'
                             '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
            self.restexv.insert(0.0, self.resulfin)
            self.restexv.tag_add('form', '1.16', '1.end')
            self.restexv.tag_config('form', foreground='purple')
            self.restexv['state'] = 'disable'
            self.graficse = 2
            self.explicar2 = 6
        elif s0 == None and s != None and v == None and v0 != None and a != None and t != None:
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            s0 = s - (v0*t) - ((a/2)*(t**2))
            st = s - s0
            v = sqrt((v0**2) + (2*a*st))
            self.resulfin = ('Função Horária: s = {} + {}t + ({}/2)t²'
                             '\n\nPara t = {}s'
                             '\ns = {}m'
                             '\ns0 = {}m'
                             '\nv = {}m/s'
                             '\nv0 = {}m/s'
                             '\na = {}m/s²'.format(s0, v0, a, t, s, s0, v, v0, a))
            self.restexv.insert(0.0, self.resulfin)
            self.restexv.tag_add('form', '1.16', '1.end')
            self.restexv.tag_config('form', foreground='purple')
            self.restexv['state'] = 'disable'
            self.graficse = 2
            self.explicar2 = 7
        else:
            self.graficse = 0
            self.explicar2 = 0
            self.resulfin = 'Você realmente está tentando achar algum bug em'
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, 'Informe o valor de 4 variáveis')
            self.restexv['state'] = 'disable'
        self.s0 = s0
        self.s = s
        self.a = a
        self.t = t
        self.v0 = v0
        self.v = v
    def expli2(self):
        s0 = self.s0
        s = self.s
        a = self.a
        t = self.t
        v0 = self.v0
        v = self.v
        self.abc = self.explicar2
        if self.abc == 0:
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, 'Pare de tentar achar um bug e coloque o seu problema :)')
            self.restexv['state'] = 'disable'
        elif self.abc == 1:
            v0t = v0 * t
            t2 = t**2
            a2 = a/2
            at = a2*t2
            self.resulfin2 = ('Como temos a função horária: s = {} + ({}t) + ({}/2)t²'
                              '\nIremos substituir o "t" pelo coeficiente dado: {}'
                              '\nA equação fica: s = {} + ({})*({}) + ({}/2){}²'
                              '\ns = {} + ({}) + ({})*{}'
                              '\ns = {} + ({}) + ({})'
                              '\ns = {}'.format(s0, v0, a, t, s0, v0, t, a, t, s0, v0t, a2, t2, s0, v0t, at, s))
            self.resulfin2 += ('\n\nPara achar a velocidade final, utilizaremos: v = v0 + at ---> v = {} + {}*{}'
                               '\nv = {} + ({}*{})'
                               '\nv = {}'.format(v0, a, t, v0, a, t, v))
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'
        elif self.abc == 2:
            sf = s - s0
            v2 = v**2
            as2 = a*sf*2
            v2as2 = v2 - as2
            rv2as = sqrt(v2as2)
            ac = a /2
            st1 = s0 - s
            v02 = v0 ** 2
            delta = v02 + (-4*ac*st1)
            rdelta = sqrt(delta)
            v0rd1 = -(v0) + rdelta
            v0rd2 = -(v0) - rdelta
            rt1 = v0rd1 / a
            rt2 = v0rd2 / a
            self.resulfin2 = ('Iremos calcular o Δs = s - s0 ---> Δs = {} - ({})'
                              '\nΔs = {}'
                              '\nA Velocidade Inicial = √(v² - (2*a*Δs)). Substituindo na fórmula temos: v0 = √({}² - (2*{}*{}))'
                              '\nv0 = √({} - ({}))'
                              '\nv0 = √({})'
                              '\nv0 = {}'
                              '\nCom isso teremos a seguinte equação de 2 grau: ({}/2)t² + {}t + ({} - ({})) = 0'
                              '\nt = (-({}) +/- √({}² -4*({})*({})))/(2*{})'
                              '\nt = (-({}) +/- √{})/{}'
                              '\nt = (-({}) +/- {})/{}'
                              '\nt1 = (-({}) + {})/{} || t2 = (-({}) - {})/{}'
                              '\nt1 = {}/{} || t2 = {}/{}'
                              '\nt1 = {} || t2 = {}'.format(s, s0, sf, v, a, sf, v2, as2, v2as2, rv2as, a, v0, s0, s, v0, v0, ac, st1, ac, v0, delta, a, v0, rdelta, a, v0, rdelta, a, v0, rdelta, a, v0rd1, a, v0rd2, a, rt1, rt2))                 
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'
        elif self.abc == 3:
            v2 = v ** 2
            v02 = v0 ** 2
            ds = s - s0
            ds2 = ds * 2
            v2v0 = v2 - v02
            ar = v2v0/ds2
            ac = ar/2
            st = s0 - s
            st1 = st
            delta = v02 + (-4*ac*st1)
            rdelta = sqrt(delta)
            v0rd1 = -(v0) + rdelta
            v0rd2 = -(v0) - rdelta
            rt1 = v0rd1 / a
            rt2 = v0rd2 / a
            self.resulfin2 = ('Função Horária: s = {} + {}t + (a/2)t²'
                              '\nIremos achar a aceleração com a fórmula de Torricelli: v² = v0² + 2.a.Δs'
                              '\n{}² = {}² + 2.a.({}-{})'
                              '\n{} = {} + {}a'
                              '\n{}a = {}'
                              '\na = {}'
                              '\n\nAgora iremos achar o tempo com uma equação de 2² grau'
                              '\n({}/2)t² + {}t + ({} - ({})) = 0'
                              '\n{}t² + {}t + ({}) = 0' 
                              '\nt = (-({}) +/- √({}² -4*({})*({})))/(2*{})'
                              '\nt = (-({}) +/- √{})/{}'
                              '\nt = (-({}) +/- {})/{}'
                              '\nt1 = (-({}) + {})/{} || t2 = (-({}) - {})/{}'
                              '\nt1 = {}/{} || t2 = {}/{}'
                              '\nt1 = {} || t2 = {}'.format(s0, v0, v, v0, s, s0, v2, v02, ds2, ds2, v2v0, ar, a, v0, s0, s, ac, v0, st, v0, v0, ac, st1, ac, v0, delta, a, v0, rdelta, a, v0, rdelta, a, v0, rdelta, a, v0rd1, a, v0rd2, a, rt1, rt2))
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'
        elif self.abc == 4:
            v02 = v0 ** 2
            ds = s - s0
            st = s0 - s
            dsa = ds * 2 * a
            v0dsa = v02 + dsa
            rv0dsa = sqrt(v0dsa)
            ac = a /2
            stpac = (-(st))/ac
            rstpac = sqrt(stpac)
            st1 = st
            delta = v02 + (-4*ac*st1)
            rdelta = sqrt(delta)
            v0rd1 = -(v0) + rdelta
            v0rd2 = -(v0) - rdelta
            rt1 = v0rd1 / a
            rt2 = v0rd2 / a
            self.resulfin2 = ('Função Horária: s = {} + {}t + ({}/2)t²'
                              '\nIremos achar a velocidade final com a fórmula de Torricelli: v² = v0² + 2.a.Δs'
                              '\nv² = {}² + 2*{}*{}'
                              '\nv² = {} + {}'
                              '\nv² = {}'
                              '\nv = +/- √{}'
                              '\nv1 = {} || v2 = {}'
                              '\n\nPara achar t em que s = {}'.format(s0, v0, a, v0, a, ds, v02, dsa, v0dsa, v0dsa, rv0dsa, -(rv0dsa), s))
            if v0 == 0:
                self.resulfin2 += ('\nResolveremos a equação do 2° grau incompleta: ax² + c = 0'
                                   '\n({}/2)t² + 0t + ({}) = 0  --> c = s0 - s'
                                   '\n{}t² = {}'
                                   '\nt² = {}/{}'
                                   '\nt = +/- √{}'
                                   '\nt1 = {} || t2 = {}'.format(a, st, ac, -(st), -(st), ac, stpac, rstpac, -(rstpac)))
            else:
                self.resulfin2 += ('\Resolveremos a equação do 2° grau'
                                   '\n({}/2)t² + {}t + ({} - ({})) = 0'
                                   '\n{}t² + {}t + ({}) = 0' 
                                   '\nt = (-({}) +/- √({}² -4*({})*({})))/(2*{})'
                                   '\nt = (-({}) +/- √{})/{}'
                                   '\nt = (-({}) +/- {})/{}'
                                   '\nt1 = (-({}) + {})/{} || t2 = (-({}) - {})/{}'
                                   '\nt1 = {}/{} || t2 = {}/{}'
                                   '\nt1 = {} || t2 = {}'.format(a, v0, s0, s, ac, v0, st, v0, v0, ac, st1, ac, v0, delta, a, v0, rdelta, a, v0, rdelta, a, v0, rdelta, a, v0rd1, a, v0rd2, a, rt1, rt2))
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'
        elif self.abc == 5:
            self.resulfin2 = ('Para acharmos t, utilizaremos a equação: v = v0 + at'
                              '\n{} = {} + {}.t'
                              '\n{} = {}t'
                              '\nt = {}/{}'
                              '\nt = {}s'.format(v, v0, a, (v-v0), a, (v-v0), a, ((v-v0)/a)))
            self.resulfin2 += ('\n\nPara achar s em que t = {}, iremos utilizar a Função Horária'
                               '\ns = {} + {}*{} + ({}/2)*({})²'
                               '\ns = {} + {} + {}*{}'
                               '\ns = {}'.format(t, s0,v0,t,a,t,s0,(v0*t), (a/2), (t**2), s))
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'
        elif self.abc == 6:
            ac = a /2
            v0t = v0 * t
            at = ac*(t**2)
            t2 = t**2
            v0at = v0t + (ac*t2)
            res = s -v0at
            self.resulfin2 = ('Temos a seguinte equação: {} = s0 + {}t + ({}/2)t²'
                              '\nPara acharmos t, iremos utilizar a equação: v = v0 + at'
                              '\n{} = {} + {}t'
                              '\n{} = {}t'
                              '\nt = {}/{}'
                              '\nt = {}s'.format(s, v0, a, v, v0, a, (v-v0), a, (v-v0), a, ((v-v0)/a)))
            self.resulfin2 += ('\n\nAgora para achar s0 iremos utilizar a Função Horária das Posições: s = s0 + v0t + (a/2)t²'
                               '\n{} = s0 + {}*{} + ({}/2)*({})²'
                               '\n{} = s0 + {} + {} * {}'
                               '\n{} = s0 + {}'
                               '\ns0 = {} - {}'
                               '\ns0 = {}'.format(s, v0, t, a, t, s, v0t, ac, t2, s, v0at, s, v0at, res)) 
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'
        elif self.abc == 7:
            v0t = v0 * t
            ac = a/2
            t2 = t ** 2
            resv0ct = v0t + (ac*t2)
            resf = s - resv0ct
            self.resulfin2 = ('Para acharmos o valor de s0 utilizaremos a função horária das posições:'
                              '\nFunção Horária das posições: s = s0 + v0t + (a/2)t²'
                              '\n{} = s0 + ({})*{} + ({}/2){}²'
                              '\n{} = s0 + ({}) + {}*{}'
                              '\n{} = s0 + ({})'
                              '\ns0 = {} - ({})'
                              '\ns0 = {}'.format(s, v0, t, a, t, s, v0t, ac, t2, s, resv0ct, s, resv0ct, resf))
            self.explv['text'] = 'Ver Resposta'
            self.explv['command'] = self.veres2
            self.restexv['state'] = 'normal'
            self.restexv.delete(0.0, 'end')
            self.restexv.insert(0.0, self.resulfin2)
            self.restexv['state'] = 'disable'            
    def veres2(self):
        self.explv['text'] = 'Explicação'
        self.explv['command'] = self.expli2
        self.restexv['state'] = 'normal'
        self.restexv.delete(0.0, 'end')
        self.restexv.insert(0.0, self.resulfin)
        self.restexv['state'] = 'disable'
    def estilo3(self):
        janela.geometry('1100x700+300+100')
        self.tit.place(x=235, y=10)
        self.created.place(x=300, y=670)
        self.created2.place(x=510, y=670)    
        #Variáveis
        errortra = StringVar(janela)
        #Labels
        #Label N(traj)
        self.traj = Label(janela, bg = bgp, fg = '#ffc600')
        self.traj['text'] = 'N°(Trajetos)'
        self.traj['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj.place(x=60, y = 100)
        #Label M Percurso
        self.percm = Label(janela, bg = bgp, fg = '#ffc600')
        self.percm['text'] = 'Percursos Iguais'
        self.percm['font'] = ('Comic Sans MS', '12', 'bold')
        self.percm.place(x=60, y = 160)
        #Combobox M Percurso
        self.cbpercm = ttk.Combobox(janela, width = 8)
        self.cbpercm['font'] = ('Comic Sans MS', '10', 'bold')
        self.cbpercm['state'] = 'readonly'
        self.cbpercm['values'] = ('Sim', 'Não')
        self.cbpercm.current(0)
        self.cbpercm.place(x=60, y = 190)
        #Entry N(traj)
        self.ntraj = Entry(janela, width =10)
        self.ntraj['font'] = ('Comic Sans MS', '10')
        self.ntraj['fg'] = 'red'
        self.ntraj.place(x=60, y = 140)
        #Traj La
        self.traj1 = Label(janela, bg = bgp, fg = '#fffc00')
        self.traj2 = Label(janela, bg = bgp, fg = '#fffc00')
        self.traj3 = Label(janela, bg = bgp, fg = '#fffc00')
        self.traj4 = Label(janela, bg = bgp, fg = '#fffc00')
        self.traj5 = Label(janela, bg = bgp, fg = '#fffc00')
        self.traj6 = Label(janela, bg = bgp, fg = '#fffc00')
        self.traj1['text'] = ('Trajeto 1º')
        self.traj2['text'] = ('Trajeto 2º')
        self.traj3['text'] = ('Trajeto 3º')
        self.traj4['text'] = ('Trajeto 4º')
        self.traj5['text'] = ('Trajeto 5º')
        self.traj6['text'] = ('Trajeto Total')
        self.traj1['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj2['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj3['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj4['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj5['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj6['font'] = ('Comic Sans MS', '12', 'bold')
        self.traj1.place(x=200, y=100)
        self.traj2.place(x=330, y=100)
        self.traj3.place(x=460, y=100)
        self.traj4.place(x=590, y=100)
        self.traj5.place(x=720, y=100)
        self.traj6.place(x=850, y=100)
        self.vel1 = Label(janela, bg = bgp, fg = '#fffc00')
        self.vel2 = Label(janela, bg = bgp, fg = '#fffc00')
        self.vel3 = Label(janela, bg = bgp, fg = '#fffc00')
        self.vel4 = Label(janela, bg = bgp, fg = '#fffc00')
        self.vel5 = Label(janela, bg = bgp, fg = '#fffc00')
        self.vel6 = Label(janela, bg = bgp, fg = '#fffc00')
        self.vel1['text'] = ('Velocid 1º')
        self.vel2['text'] = ('Velocid 2º')
        self.vel3['text'] = ('Velocid 3º')
        self.vel4['text'] = ('Velocid 4º')
        self.vel5['text'] = ('Velocid 5º')
        self.vel6['text'] = ('Velocid Total')
        self.vel1['font'] = ('Comic Sans MS', '12', 'bold')
        self.vel2['font'] = ('Comic Sans MS', '12', 'bold')
        self.vel3['font'] = ('Comic Sans MS', '12', 'bold')
        self.vel4['font'] = ('Comic Sans MS', '12', 'bold')
        self.vel5['font'] = ('Comic Sans MS', '12', 'bold')
        self.vel6['font'] = ('Comic Sans MS', '12', 'bold')
        self.vel1.place(x=200, y=160)
        self.vel2.place(x=330, y=160)
        self.vel3.place(x=460, y=160)
        self.vel4.place(x=590, y=160)
        self.vel5.place(x=720, y=160)
        self.vel6.place(x=850, y=160)
        #Entry Traj
        self.ent1 = Entry(janela, width = 8)
        self.ent2 = Entry(janela, width = 8)
        self.ent3 = Entry(janela, width = 8)
        self.ent4 = Entry(janela, width = 8)
        self.ent5 = Entry(janela, width = 8)
        self.ent6 = Entry(janela, width = 8)
        self.ent1['font'] = ('Comic Sans MS', '10')
        self.ent2['font'] = ('Comic Sans MS', '10')
        self.ent3['font'] = ('Comic Sans MS', '10')
        self.ent4['font'] = ('Comic Sans MS', '10')
        self.ent5['font'] = ('Comic Sans MS', '10')
        self.ent6['font'] = ('Comic Sans MS', '10')
        self.ent1['fg'] = 'red'
        self.ent2['fg'] = 'red'
        self.ent3['fg'] = 'red'
        self.ent4['fg'] = 'red'
        self.ent5['fg'] = 'red'
        self.ent6['fg'] = 'red'
        self.ent1.place(x=200, y = 140)
        self.ent2.place(x=330, y = 140)
        self.ent3.place(x=460, y = 140)
        self.ent4.place(x=590, y = 140)
        self.ent5.place(x=720, y = 140)
        self.ent6.place(x=850, y = 138)
        self.ent7 = Entry(janela, width = 8)
        self.ent8 = Entry(janela, width = 8)
        self.ent9 = Entry(janela, width = 8)
        self.ent10 = Entry(janela, width = 8)
        self.ent11 = Entry(janela, width = 8)
        self.ent12 = Entry(janela, width = 8)
        self.ent7['font'] = ('Comic Sans MS', '10')
        self.ent8['font'] = ('Comic Sans MS', '10')
        self.ent9['font'] = ('Comic Sans MS', '10')
        self.ent10['font'] = ('Comic Sans MS', '10')
        self.ent11['font'] = ('Comic Sans MS', '10')
        self.ent12['font'] = ('Comic Sans MS', '10')
        self.ent7['fg'] = 'red'
        self.ent8['fg'] = 'red'
        self.ent9['fg'] = 'red'
        self.ent10['fg'] = 'red'
        self.ent11['fg'] = 'red'
        self.ent12['fg'] = 'red' 
        self.ent7.place(x=200, y = 190)
        self.ent8.place(x=330, y = 190)
        self.ent9.place(x=460, y = 190)
        self.ent10.place(x=590, y = 190)
        self.ent11.place(x=720, y = 190)
        self.ent12.place(x=850, y = 190)
        #UN do Resultado
        self.unires2 = Label(janela, text='UN Resultado', bg = bgp)
        self.unires2['font'] = ('Arial', '12', 'bold')
        self.unires2['fg'] = '#00edf0'
        self.unires2.place(x=975, y= 130)
        #Combobox
        #Trajeto/Velocidade 1
        self.cbtr1 = ttk.Combobox(janela, width = 4)
        self.cbtr1['state'] = 'readonly'
        self.cbtr1['values'] = ('m', 'Km')
        self.cbtr1['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtr1.current(1)
        self.cbtr1.place(x=270, y = 140)        
        self.cbve1 = ttk.Combobox(janela, width = 4)
        self.cbve1['state'] = 'readonly'
        self.cbve1['values'] = ('m/s', 'Km/h')
        self.cbve1['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbve1.current(1)
        self.cbve1.place(x=270, y = 190)
        #Trajeto/Velocidade 2
        self.cbtr2 = ttk.Combobox(janela, width = 4)
        self.cbtr2['state'] = 'readonly'
        self.cbtr2['values'] = ('m', 'Km')
        self.cbtr2['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtr2.current(1)
        self.cbtr2.place(x=400, y = 140)        
        self.cbve2 = ttk.Combobox(janela, width = 4)
        self.cbve2['state'] = 'readonly'
        self.cbve2['values'] = ('m/s', 'Km/h')
        self.cbve2['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbve2.current(1)
        self.cbve2.place(x=400, y = 190)
        #Trajeto/Velocidade 3
        self.cbtr3 = ttk.Combobox(janela, width = 4)
        self.cbtr3['state'] = 'readonly'
        self.cbtr3['values'] = ('m', 'Km')
        self.cbtr3['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtr3.current(1)
        self.cbtr3.place(x=530, y = 140)        
        self.cbve3 = ttk.Combobox(janela, width = 4)
        self.cbve3['state'] = 'readonly'
        self.cbve3['values'] = ('m/s', 'Km/h')
        self.cbve3['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbve3.current(1)
        self.cbve3.place(x=530, y = 190)
        #Trajeto/Velocidade 4
        self.cbtr4 = ttk.Combobox(janela, width = 4)
        self.cbtr4['state'] = 'readonly'
        self.cbtr4['values'] = ('m', 'Km')
        self.cbtr4['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtr4.current(1)
        self.cbtr4.place(x=660, y = 140)        
        self.cbve4 = ttk.Combobox(janela, width = 4)
        self.cbve4['state'] = 'readonly'
        self.cbve4['values'] = ('m/s', 'Km/h')
        self.cbve4['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbve4.current(1)
        self.cbve4.place(x=660, y = 190)
        #Trajeto/Velocidade 5
        self.cbtr5 = ttk.Combobox(janela, width = 4)
        self.cbtr5['state'] = 'readonly'
        self.cbtr5['values'] = ('m', 'Km')
        self.cbtr5['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtr5.current(1)
        self.cbtr5.place(x=790, y = 140)        
        self.cbve5 = ttk.Combobox(janela, width = 4)
        self.cbve5['state'] = 'readonly'
        self.cbve5['values'] = ('m/s', 'Km/h')
        self.cbve5['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbve5.current(1)
        self.cbve5.place(x=790, y = 190)
        #Trajeto Total
        self.cbtr6 = ttk.Combobox(janela, width = 4)
        self.cbtr6['state'] = 'readonly'
        self.cbtr6['values'] = ('m', 'Km')
        self.cbtr6['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbtr6.current(1)
        self.cbtr6.place(x=920, y = 138)
        self.cbve6 = ttk.Combobox(janela, width = 4)
        self.cbve6['state'] = 'readonly'
        self.cbve6['values'] = ('m/s', 'Km/h')
        self.cbve6['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbve6.current(1)
        self.cbve6.place(x=920, y = 190)
        #Unidade do Resultado
        self.cbur2 = ttk.Combobox(janela, width = 5)
        self.cbur2['state'] = 'readonly'
        self.cbur2['values'] = ('m/s', 'Km/h')
        self.cbur2['font'] = ('Comic Sans MS', '9', 'bold')
        self.cbur2.current(1)
        self.cbur2.place(x=990, y= 165)
        #Text
        self.restex2 = Text(janela, width = 94, height = 16)
        self.restex2['font'] = ('Comic Sans MS', '12', 'bold')
        self.restex2['state'] = 'disable'
        self.restex2.place(x= 60, y = 230)
        #Botao pega
        self.bpege2 = Button(janela, text='Calcular', width=10, height= 1,bd = 0, bg= '#ff0000',\
            activebackground= '#fff', activeforeground = '#ff0000', fg = '#fff')
        self.bpege2['font'] = ('Comic Sans MS', '13')
        self.bpege2['command'] = self.calc3
        self.bpege2.place(x=870, y=630)
    def calc3(self):
        self.pgtr = self.ntraj.get()
        traj1 = self.ent1.get()
        traj1un = self.cbtr1.get()
        traj2 = self.ent2.get()
        traj2un = self.cbtr2.get()
        vel1 = self.ent7.get()
        vel1un = self.cbve1.get()
        vel2 = self.ent8.get()
        vel2un = self.cbve2.get()
        veltot = self.ent12.get()
        veltotun = self.cbve6.get()
        trajtotal = self.ent6.get()
        trajtotalun = self.cbtr6.get()
        perig = self.cbpercm.get()
        uniresf = self.cbur2.get()
        if uniresf == 'Km/h':
            if traj1un == 'm':
                try:
                    traj1 = float(traj1)
                    traj1 /= 1000
                    utr1 = 'Km'
                except ValueError:
                    utr1 = 'Km'
                    traj1 = None
            elif traj1un == 'Km':
                try:
                    traj1 = float(traj1)
                except ValueError:
                    traj1 = None     
            if traj2un == 'm':
                try:
                    traj2 = float(traj2)
                    traj2 /= 1000
                    utr2 = 'Km'
                except ValueError:
                    utr2 = 'Km'
                    traj2 = None
            elif traj2un == 'Km':
                try:
                    traj2 = float(traj2)
                except ValueError:
                    traj2 = None
            if trajtotalun == 'm':
                try:
                    trajtotal = float(trajtotal)
                    trajtotal /= 1000
                    utrtotal = 'Km'
                except ValueError:
                    utrtotal = 'Km'
                    trajtotal = None
            elif trajtotalun == 'Km':
                try:
                    trajtotal = float(trajtotal)
                except ValueError:
                    trajtotal = None
                    
            if vel1un == 'm/s':
                try:
                    vel1 = float(vel1)
                    vel1 *= 3.6
                    uv1 = 'Km/h'
                except ValueError:
                    uv1 = 'Km/h'
                    vel1 = None
            elif vel1un == 'Km/h':
                try:
                    vel1 = float(vel1)
                except ValueError:
                    vel1 = None

            if vel2un == 'm/s':
                try:
                    vel2 = float(vel2)
                    vel2 *= 3.6
                    uv2 = 'Km/h'
                except ValueError:
                    uv2 = 'Km/h'
                    vel2 = None
            elif vel2un == 'Km/h':
                try:
                    vel2 = float(vel2)
                except ValueError:
                    vel2 = None
            if veltotun == 'm/s':
                try:
                    veltot = float(veltot)
                    veltot *= 3.6
                    uvtot = 'Km/h'
                except ValueError:
                    uvtot = 'Km/h'
                    veltot = None
            elif veltotun == 'Km/h':
                try:
                    veltot = float(veltot)
                except ValueError:
                    veltot = None
        if self.pgtr == '2':            
            if perig == 'Sim':
                if trajtotal == None:
                    if traj1 == None and traj2 == None:
                        if vel1 != None and vel2 != None:
                            a = int(vel1)
                            b = int(vel2)
                            resto = None
                            while resto is not 0:
                                resto = a % b
                                a = b
                                b = resto
                            mmc = (vel1 * vel2) / a
                            numerador1 = mmc / vel1
                            numerador2 = mmc / vel2
                            numeradortot = numerador1 + numerador2
                            resultado = (2 * mmc)/numeradortot
                            resultado = round(resultado, 3)
                            print(resultado)
                        else:
                            print('Precisamos de 2 velocidades')
                    elif traj1 != None and traj2 == None:
                        if vel1 != None and vel2 != None:
                            a = int(vel1)
                            b = int(vel2)
                            resto = None
                            while resto is not 0:
                                resto = a % b
                                a = b
                                b = resto
                            mmc = (vel1 * vel2) / a
                            numerador1 = (mmc / vel1) * traj1
                            numerador2 = (mmc / vel2) * traj1
                            numeradortot = numerador1 + numerador2
                            trajtotal = 2 * traj1
                            resultado = (trajtotal * mmc)/numeradortot
                            resultado = round(resultado, 3)
                            print(resultado)
                        elif vel1 != None and vel2 == None and veltot != None:
                            trajtotal = traj1 * 2
                            traj2 = traj1
                            numerador1 = traj1
                            numerador2 = traj2*vel1
                            denominador = vel1
                            membro1 = (trajtotal*denominador)-(veltot * numerador1)
                            membro2 = veltot * numerador2
                            vel2 = membro2/membro1
                            print('Velocidade no 2 Trajeto=',vel2)
                        elif vel1 == None and vel2 != None and veltot != None:
                            trajtotal = traj1 * 2
                            traj2 = traj1
                            numerador1 = traj1
                            numerador2 = traj2*vel2
                            denominador = vel2
                            membro1 = (trajtotal*denominador)-(veltot * numerador1)
                            membro2 = veltot * numerador2
                            vel1 = membro2/membro1
                            print('Velocidade no 1 Trajeto=',vel1)
                    elif traj2 != None and traj1 == None:
                        if vel1 != None and vel2 != None:
                            a = int(vel1)
                            b = int(vel2)
                            resto = None
                            while resto is not 0:
                                resto = a % b
                                a = b
                                b = resto
                            mmc = (vel1 * vel2) / a
                            numerador1 = (mmc / vel1) * traj2
                            numerador2 = (mmc / vel2) * traj2
                            numeradortot = numerador1 + numerador2
                            trajtotal = 2 * traj2
                            resultado = (trajtotal * mmc)/numeradortot
                            resultado = round(resultado, 2)
                        elif vel2 != None and vel1 == None and veltot != None:
                            trajtotal = traj2 * 2
                            traj1 = traj2
                            numerador1 = traj2
                            numerador2 = traj1*vel2
                            denominador = vel2
                            membro1 = (trajtotal*denominador)-(veltot * numerador1)
                            membro2 = veltot * numerador2
                            vel1 = membro2/membro1
                            print('Velocidade no 1 Trajeto=',vel1)
                        elif vel1 != None and vel2 == None and veltot != None:
                            trajtotal = traj2 * 2
                            traj1 = traj2
                            numerador1 = traj1
                            numerador2 = traj2*vel1
                            denominador = vel1
                            membro1 = (trajtotal*denominador)-(veltot * numerador1)
                            membro2 = veltot * numerador2
                            vel2 = membro2/membro1
                            print('Velocidade no 2 Trajeto=',vel2)
                    elif traj1 != None and traj2 != None:
                        if traj1 == traj2:
                            if vel1 != None and vel2 != None:
                                a = int(vel1)
                                b = int(vel2)
                                resto = None
                                while resto is not 0:
                                    resto = a % b
                                    a = b
                                    b = resto
                                mmc = (vel1 * vel2) / a
                                numerador1 = (mmc / vel1) * traj1
                                numerador2 = (mmc / vel2) * traj1
                                numeradortot = numerador1 + numerador2
                                trajtotal = traj2 + traj1
                                resultado = (trajtotal * mmc)/numeradortot
                                resultado = round(resultado, 2)
                                
                                print(trajtotal)
                                print(resultado)

                        else:
                            print('Trajetos não são iguais')
                else:
                    if vel1 != None and vel2 != None:
                        traj1 = trajtotal/2
                        traj2 = trajtotal/2
                        a = int(vel1)
                        b = int(vel2)
                        resto = None
                        while resto is not 0:
                            resto = a % b
                            a = b
                            b = resto
                        mmc = (vel1 * vel2) / a
                        numerador1 = (mmc / vel1) * traj1
                        numerador2 = (mmc / vel2) * traj2
                        numeradortot = numerador1 + numerador2
                        resultado = (trajtotal * mmc)/numeradortot
                        resultado = round(resultado, 3)

                        print(resultado)
                    elif vel1 == None and vel2 != None and veltot != None:
                        traj1 = trajtotal/2
                        traj2 = trajtotal/2
                        numerador1 = traj1
                        numerador2 = traj2*vel2
                        denominador = vel2
                        membro1 = (trajtotal*denominador)-(veltot * numerador1)
                        membro2 = veltot * numerador2
                        vel1 = membro2/membro1
                        print(vel1)
                    elif vel1 != None and vel2 == None and veltot != None:
                        traj1 = trajtotal/2
                        traj2 = trajtotal/2
                        numerador1 = traj1
                        numerador2 = traj2*vel1
                        denominador = vel1
                        membro1 = (trajtotal*denominador)-(veltot * numerador1)
                        membro2 = veltot * numerador2
                        vel2 = membro2/membro1
                        print(vel2)
                    else:
                        print('Informe pelo menos 2 velocidades')               
            elif perig == 'Não':
                if trajtotal == None:
                    if traj1 != None and traj2 != None:
                        if vel1 != None and vel2 != None:
                            a = int(vel1)
                            b = int(vel2)
                            resto = None
                            while resto is not 0:
                                resto = a % b
                                a = b
                                b = resto
                            mmc = (vel1 * vel2) / a
                            trajtotal = traj1 + traj2
                            numerador1 = (mmc/vel1) * traj1
                            numerador2 = (mmc/vel2) * traj2
                            resultado = (trajtotal*mmc)/(numerador1+numerador2)
                            print(resultado)
                        elif vel1 != None and vel2 == None and veltot != None:
                            numerador1 = traj1
                            numerador2 = vel1 * traj2
                            denominador = vel1
                            trajtotal = traj1+traj2
                            membro1 = (trajtotal*denominador)-(veltot * numerador1)
                            membro2 = veltot * numerador2
                            vel2 = membro2/membro1
                            print(vel2)
                        elif vel1 == None and vel2 != None and veltot != None:
                            numerador1 = traj2
                            numerador2 = vel2 * traj1
                            denominador = vel2
                            trajtotal = traj1+traj2
                            membro1 = (trajtotal*denominador)-(veltot * numerador1)
                            membro2 = veltot * numerador2
                            vel2 = membro2/membro1
                        else:
                            print('Informe pelo menos 2 velocidades')
                    elif traj1 != None and traj2 == None:
                        if vel1 != None and vel2 != None and veltot:
                            a = int(vel1)
                            b = int(vel2)
                            resto = None
                            while resto is not 0:
                                resto = a % b
                                a = b
                                b = resto
                            mmc = (vel1 * vel2) / a
                            numerador1 = (mmc/vel1) * traj1
                            numerador2 = (mmc/vel2)
                            membro1 = mmc - (veltot * numerador2)
                            membro2 = (veltot*numerador1) - (mmc*traj1)
                            resul = membro2/membro1
                            print(resul)
                        else:
                            print('Não consigo realizar este tipo de operação')                     
        contadorcrtl = 0
        contadorcrte = 0
janela = Tk()
cmru(janela)
janela.mainloop()
