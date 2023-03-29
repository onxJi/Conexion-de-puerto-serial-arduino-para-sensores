
import serial.tools.list_ports

class configuracion_serial():
	def __init__(self):
		pass

	def obtiene_serial(self):
		puertos = serial.tools.list_ports.comports()
		self.lista_puertos = [com[0] for com in puertos]
		self.lista_puertos.insert(0, "-")

	def abrir_puertos(self, createControls):
		try:
			self.ser = serial.Serial()
			self.ser.port = createControls.cmb_puerto.get()
			self.ser.baudrate = createControls.cmb_baud.get()
			self.ser.timeout = 0.1

			if createControls.cmb_parity.get() == 'EVEN':
				self.ser.parity = serial.PARITY_EVEN
			elif createControls.cmb_parity.get() == 'ODD':
				self.ser.parity = serial.PARITY_ODD
			elif createControls.cmb_parity.get() == 'MARK':
				self.ser.parity = serial.PARITY_MARK
			elif createControls.cmb_parity.get() == 'SPACE':
				self.ser.parity = serial.PARITY_SPACE

			if createControls.cmb_data.get() == '5':
				self.ser.data = serial.FIVEBITS
			elif createControls.cmb_data.get() == '6':
				self.ser.data = serial.SIXBITS
			elif createControls.cmb_data.get() == '7':
				self.ser.data = serial.SEVENBITS
			elif createControls.cmb_data.get() == '8':
				self.ser.data = serial.EIGHTBITS
			self.ser.open()
			self.ser.status = True
			return True, "Conexion Exitosa"
		except Exception as inst:
			return False, inst

	def cerrar_puerto(self,createControls):
		try:
			if(self.ser.is_open==True):
				self.ser.close()
				self.ser.status = False
				return True, "Conexion Terminada"
		except Exception as inst:
			return False, inst

	def recibir_datos(self,createControls):
		datos = self.ser.readline()
		return datos

	def enviar_datos(self,createControls,mensaje):
		self.ser.write(mensaje.encode())
		return "Se ha enviado datos: " + mensaje
  


