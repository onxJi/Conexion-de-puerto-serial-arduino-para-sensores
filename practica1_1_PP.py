from practica1_PP import construyeVentana, createControls
from conexion_serial import configuracion_serial


interfaz = construyeVentana()
puerto_serial = configuracion_serial()
controles = createControls(interfaz.ventana, puerto_serial)
interfaz.ventana.mainloop()
