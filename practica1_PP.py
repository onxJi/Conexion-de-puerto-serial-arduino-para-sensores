from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
import time
import threading
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


from PIL import Image, ImageTk
class construyeVentana():
	def __init__(self):
		self.ventana = Tk()
		#Titulo de la ventana
		self.ventana.title("Comunicacion Serial")
		#Agregamos el tamaño de la ventana
		self.ventana.geometry("900x700")

		#Posicionamos la ventana en la parte central de la pantalla de la PC
		ancho_ventana = self.ventana.winfo_screenwidth()
		largo_ventana = self.ventana.winfo_screenheight()

		posicion_ancho = int((ancho_ventana/2)-(770/2))
		posicion_largo = int((largo_ventana/2)-(600/2))

		self.ventana.geometry("+{}+{}".format(posicion_ancho,posicion_largo))


class createControls():
	def __init__(self, ventana, serial):
		self.ventana=ventana
		self.serial=serial
		self.frame_configuration = LabelFrame(ventana, text="Datos de conexion")
		self.frame_configuration.grid(column=0,row=0,padx=10,pady=5)
  
		self.agregarControls()
  
		self.frame_IO = LabelFrame(ventana, text="Controles Entrada/Salida")
		self.frame_IO.grid(column=0,row=1,padx=10,pady=5)
		self.agregaInterfazIO()
		self.DefaultOptions2()
		self.YData = []
		self.XData = []
		self.YData2 = []
		self.XData2 = []
		self.YData3 = []
		self.msg = [2]
		self.msg2 = [1]
		self.grafica1()

	def agregarControls(self):
		Label(self.frame_configuration,text="Port:").grid(column=0, row=0, sticky='E')
		self.cmb_puerto = ttk.Combobox(self.frame_configuration, state = "readonly")
		#self.cmb_puerto["values"] = ["-","COM1","COM2","COM3", "COM4"]
		self.serial.obtiene_serial()
		self.cmb_puerto["values"]= self.serial.lista_puertos
		self.cmb_puerto.grid(column=1,row=0,padx=5,pady=5)

		#ComboBox del Baud Rate
		Label(self.frame_configuration,text="Baud rate:").grid(column=2,row=0,sticky='E')
		self.cmb_baud = ttk.Combobox(self.frame_configuration, state = "readonly")
		self.cmb_baud["values"] = ["-","300","600","1200","2400","4800","9600","14400","19200","28800"]
		self.cmb_baud.grid(column=3,row=0,padx=5,pady=5)

		Label(self.frame_configuration, text="Data Bits:").grid(column=4,row=0,sticky='E')
		self.cmb_data = ttk.Combobox(self.frame_configuration, state = "readonly")
		self.cmb_data["values"] = ["-","5","6","7","8"]
		self.cmb_data.grid(column=5,row=0,padx=5,pady=5)

		Label(self.frame_configuration, text="Parity:").grid(column=0,row=1,sticky='E')
		self.cmb_parity = ttk.Combobox(self.frame_configuration, state = "readonly")
		self.cmb_parity["values"] = ["-","EVEN","ODD","MARK","SPACE"]
		self.cmb_parity.grid(column=1,row=1,padx=5,pady=5)

		Label(self.frame_configuration, text="Stop Bits:").grid(column=2,row=1,sticky='E')
		self.cmb_stopBit = ttk.Combobox(self.frame_configuration, state = "readonly")
		self.cmb_stopBit["values"] = ["-","1","2"]
		self.cmb_stopBit.grid(column=3,row=1,padx=5,pady=5)

		self.btn_connect = Button(self.frame_configuration, text="Conectar", command=self.conectar)
		self.btn_connect.grid(column=4, row=1,ipadx=25, padx=5, pady=5)

		self.btn_disconnect = Button(self.frame_configuration, text="Desconectar", command=self.desaconectar_conexion)
		self.btn_disconnect.grid(column=5, row=1,ipadx=25, padx=5, pady=5)
		self.DefaultOptions()
		self.habilitar_controles()
		
	def agregaInterfazIO(self):
     
		self.image1 = Image.open('\\Programacion y control de perifericos\\btn_off_1.png')
		self.image2 = Image.open('\\Programacion y control de perifericos\\btn_on_1.png')
		resized1 = self.image1.resize((80,40),Image.ANTIALIAS)
		resized2 = self.image2.resize((80,40),Image.ANTIALIAS)
		self.image1 = ImageTk.PhotoImage(resized1)
		self.image2 = ImageTk.PhotoImage(resized2)
		self.btn_led1 = Button(self.frame_IO,
                         		image=self.image1,command=self.command_led1,
                           		borderwidth=0)
		self.btn_led1.grid(column=0,row=0,padx=5, pady=5)
		self.btn_led2 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led2,borderwidth=0)
		self.btn_led2.grid(column=1,row=0,padx=5, pady=5)
		self.btn_led3 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led3,borderwidth=0)
		self.btn_led3.grid(column=2,row=0,padx=5, pady=5)
		self.btn_led4 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led4,borderwidth=0)
		self.btn_led4.grid(column=3,row=0,padx=5, pady=5)
		self.btn_led5 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led5,borderwidth=0)
		self.btn_led5.grid(column=4,row=0,padx=5, pady=5)
		self.btn_led6 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led6,borderwidth=0)
		self.btn_led6.grid(column=5,row=0,padx=5, pady=5)
		self.btn_led7 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led7,borderwidth=0)
		self.btn_led7.grid(column=6,row=0,padx=5, pady=5)
		self.btn_led8 = Button(self.frame_IO,image=self.image1,
                         		command=self.command_led8,borderwidth=0)
		self.btn_led8.grid(column=7,row=0,padx=5, pady=5)
		Label(self.frame_IO,text="LED 1").grid(column=0, row=2)
		Label(self.frame_IO,text="LED 2").grid(column=1, row=2)
		Label(self.frame_IO,text="LED 3").grid(column=2, row=2)
		Label(self.frame_IO,text="LED 4").grid(column=3, row=2)
		Label(self.frame_IO,text="LED 5").grid(column=4, row=2)
		Label(self.frame_IO,text="LED 6").grid(column=5, row=2)
		Label(self.frame_IO,text="LED 7").grid(column=6, row=2)
		Label(self.frame_IO,text="LED 8").grid(column=7, row=2)
		
		
  
		self.led1=BooleanVar()
		self.led1.set(True)
		self.led2=BooleanVar()
		self.led2.set(True)
		self.led3=BooleanVar()
		self.led3.set(True)
		self.led4=BooleanVar()
		self.led4.set(True)
		self.led5=BooleanVar()
		self.led5.set(True)
		self.led6=BooleanVar()
		self.led6.set(True)
		self.led7=BooleanVar()
		self.led7.set(True)
		self.led8=BooleanVar()
		self.led8.set(True)
		self.stream1=IntVar()
		self.stream2=IntVar()
		self.stream3=IntVar()
		# self.chk_led1= Checkbutton(self.frame_IO, text="Led 1",
        #                      		variable=self.led1, onvalue="1",offvalue="0",
        #                        		command=self.command_led1)
		# self.chk_led1.grid(column=0, row=1,padx=5, pady=5)
		self.chk_stream1 = Checkbutton(self.frame_IO, text="Iniciar stream",
                                		variable=self.stream1, onvalue="1", offvalue="0",
                                  		command=self.recibe_datos)
		self.chk_stream1.grid(column=0, row=3, padx=5, pady=5)

		self.txt_recibe_mensaje = scrolledtext.ScrolledText(self.frame_IO,
                                                      		wrap=WORD, width=10,
                                                        	height=5,font=("Consolas",12))
		self.txt_recibe_mensaje.grid(column=1, row=3,padx=5, pady=5)
  
		self.chk_stream2 = Label(self.frame_IO, text="Channel 2"
                                  		)
		self.chk_stream2.grid(column=3, row=3, padx=5, pady=5)

		self.txt_recibe_mensaje_2 = scrolledtext.ScrolledText(self.frame_IO,
                                                      		wrap=WORD, width=10,
                                                        	height=5,font=("Consolas",12))
		self.txt_recibe_mensaje_2.grid(column=4, row=3,padx=5, pady=5)
  
		self.chk_stream3 = Label(self.frame_IO, text="Channel 3")
		self.chk_stream3.grid(column=6, row=3, padx=5, pady=5)

		self.txt_recibe_mensaje_3 = scrolledtext.ScrolledText(self.frame_IO,
                                                      		wrap=WORD, width=10,
                                                        	height=5,font=("Consolas",12))
		self.txt_recibe_mensaje_3.grid(column=7, row=3,padx=5, pady=5)

		########################################################
		# Agregando las graficas
		
		self.frame_graph = LabelFrame(self.ventana, text='Graficas')
		self.frame_graph.grid(column=0,row=2,padx=10, pady=5)
		self.fig = Figure(figsize=(6,4),dpi=80)
		self.plot = self.fig.add_subplot(111)
		self.fig.set_tight_layout(True)
		#self.fig.add_subplot(111)
		
		self.canvas = FigureCanvasTkAgg(self.fig, self.frame_graph)
		self.canvas.get_tk_widget().grid(column=0,row=0,padx=5, pady=5)
		########################################################

 
	def grafica1(self):
		try:
			self.plot.cla()
			self.plot.plot(self.XData, self.YData,self.XData,self.YData2,self.XData,self.YData3,linewidth=2)
			self.plot.legend(['Porcentaje %', 'Voltaje 1','Voltaje 2'],loc=2)
			self.canvas.draw()
		except Exception as e:
			print("Error",e)
		self.ventana.after(40,self.grafica1)
  

	##########################################################
	# FUNCIONES PARA ENCENDER LOS LEDS
	def command_led1(self):
		if self.led1.get() == True:
			self.serial.enviar_datos(self,"A")
			self.btn_led1.configure(image=self.image2)
			self.btn_led1.image=self.image2
			self.led1.set(False);
		else:
			self.serial.enviar_datos(self,"a")
			self.btn_led1.configure(image=self.image1)
			self.btn_led1.image=self.image1
			self.led1.set(True);
		#msg.showinfo("Informacion",self.serial.enviar_datos(self,"a"))


	def command_led2(self):
		if self.led2.get() == True:
			self.serial.enviar_datos(self,"B")
			self.btn_led2.configure(image=self.image2)
			self.btn_led2.image=self.image2
			self.led2.set(False);
		else:
			self.serial.enviar_datos(self,"b")
			self.btn_led2.configure(image=self.image1)
			self.btn_led2.image=self.image1
			self.led2.set(True);
   

	def command_led3(self):
		if self.led3.get() == True:
			self.serial.enviar_datos(self,"C")
			self.btn_led3.configure(image=self.image2)
			self.btn_led3.image=self.image2
			self.led3.set(False);
		else:
			self.serial.enviar_datos(self,"c")
			self.btn_led3.configure(image=self.image1)
			self.btn_led3.image=self.image1
			self.led3.set(True);
   

	def command_led4(self):
		if self.led4.get() == True:
			self.serial.enviar_datos(self,"D")
			self.btn_led4.configure(image=self.image2)
			self.btn_led4.image=self.image2
			self.led4.set(False);
		else:
			self.serial.enviar_datos(self,"d")
			self.btn_led4.configure(image=self.image1)
			self.btn_led4.image=self.image1
			self.led4.set(True);


	def command_led5(self):
		if self.led5.get() == True:
			self.serial.enviar_datos(self,"E")
			self.btn_led5.configure(image=self.image2)
			self.btn_led5.image=self.image2
			self.led5.set(False);
		else:
			self.serial.enviar_datos(self,"e")
			self.btn_led5.configure(image=self.image1)
			self.btn_led5.image=self.image1
			self.led5.set(True);
   
   
	def command_led6(self):
		if self.led6.get() == True:
			self.serial.enviar_datos(self,"F")
			self.btn_led6.configure(image=self.image2)
			self.btn_led6.image=self.image2
			self.led6.set(False);
		else:
			self.serial.enviar_datos(self,"f")
			self.btn_led6.configure(image=self.image1)
			self.btn_led6.image=self.image1
			self.led6.set(True);
   
	def command_led7(self):
		if self.led7.get() == True:
			self.serial.enviar_datos(self,"G")
			self.btn_led7.configure(image=self.image2)
			self.btn_led7.image=self.image2
			self.led7.set(False);
		else:
			self.serial.enviar_datos(self,"g")
			self.btn_led7.configure(image=self.image1)
			self.btn_led7.image=self.image1
			self.led7.set(True);
   
   
	def command_led8(self):
		if self.led8.get() == True:
			self.serial.enviar_datos(self,"H")
			self.btn_led8.configure(image=self.image2)
			self.btn_led8.image=self.image2
			self.led8.set(False);
		else:
			self.serial.enviar_datos(self,"h")
			self.btn_led8.configure(image=self.image1)
			self.btn_led8.image=self.image1
			self.led8.set(True);
	#########################################################################

	def serialDataStream(self):
		#time.sleep(0.2)
		while self.stream1.get()== True:
			try:
				datos = self.serial.recibir_datos(self)
				
				temp = datos.decode('utf-8')
				if len(temp)>0:
					if "|" in temp:
						self.msg = temp.split("|")
						print("---------------")
						print(self.msg)
						del self.msg[0]
						# del self.msg[2]
						# del self.msg[3]


				print(self.msg[0])
				print(self.msg[1])
				print(self.msg[2])
				self.msg2=self.msg[1]
				self.YData.append(float(self.msg[0]))
				self.YData2.append(float(self.msg[1]))
				self.YData3.append(float(self.msg[2]))
				self.txt_recibe_mensaje.insert(INSERT,self.msg[0]+"\n")
				self.txt_recibe_mensaje_2.insert(INSERT,self.msg[1]+"\n")
				self.txt_recibe_mensaje_3.insert(INSERT,self.msg[2]+"\n")
				self.XData.append(int(time.perf_counter()))
				
				
			except Exception as e:
				#print("Error",e)
				print(self.msg)
				
  
	def recibe_datos(self):
		if self.stream1.get() == True:
			self.serial.enviar_datos(self,"S")
			self.serial.t1 = threading.Thread(target=self.serialDataStream)
			self.serial.t1.setDaemon(True)
			self.serial.t1.start()
		else:
			self.serial.enviar_datos(self,"s")
			self.serial.threading = False
     
     
	def DefaultOptions(self):
		self.cmb_baud.set("-")
		self.cmb_data.set("-")
		self.cmb_parity.set("-")
		self.cmb_stopBit.set("-")
		self.cmb_puerto.set("-")

 
	def DefaultOptions2(self):
		self.btn_led1.configure(state='disabled')
		self.btn_led2.configure(state='disabled')
		self.btn_led3.configure(state='disabled')
		self.btn_led4.configure(state='disabled')
		self.btn_led5.configure(state='disabled')
		self.btn_led6.configure(state='disabled')
		self.btn_led7.configure(state='disabled')
		self.btn_led8.configure(state='disabled')
		self.chk_stream1.configure(state='disabled')
  
  
	def Habilitar_FrameIO(self):
		self.btn_led1.configure(state='normal')
		self.btn_led2.configure(state='normal')
		self.btn_led3.configure(state='normal')
		self.btn_led4.configure(state='normal')
		self.btn_led5.configure(state='normal')
		self.btn_led6.configure(state='normal')
		self.btn_led7.configure(state='normal')
		self.btn_led8.configure(state='normal')
		self.chk_stream1.configure(state='normal')

	
	def validate(self):
		if self.cmb_puerto.get()=='-':
			msg.showerror("Error", "Selecciona un puerto")
			return False
		if self.cmb_baud.get()=='-':
			msg.showerror("Error", "Selecciona el baud rate")
			return False

		return True

	def conectar(self):
		if self.validate()==False:
			return
		msg.showinfo("Informacion",
			"Trama de conexion "+self.cmb_puerto.get()+" "+self.cmb_baud.get())
		estado,respuesta = self.serial.abrir_puertos(self)
		if(estado==False):
			msg.showerror("Informacion",respuesta.args)
			
		else:
			msg.showinfo("Informacion",respuesta)
			self.deshabilitar_controles()
			self.Habilitar_FrameIO()
		
  		
		

	def desaconectar_conexion(self):
		self.serial.cerrar_puerto(self)
		self.habilitar_controles()


	def habilitar_controles(self):
		self.cmb_puerto.configure(state='normal')
		self.cmb_baud.configure(state='normal')
		self.cmb_data.configure(state='normal')
		self.cmb_parity.configure(state='normal')
		self.cmb_stopBit.configure(state='normal')
		self.btn_connect.configure(state='normal')
		self.btn_disconnect.configure(state='disabled')



	def deshabilitar_controles(self):
		self.cmb_puerto.configure(state='disabled')
		self.cmb_baud.configure(state='disabled')
		self.cmb_data.configure(state='disabled')
		self.cmb_parity.configure(state='disabled')
		self.cmb_stopBit.configure(state='disabled')
		self.btn_connect.configure(state='disabled')
		
		self.btn_disconnect.configure(state='normal')
if __name__=="__main__":
	construyeVentana()
	createControls()