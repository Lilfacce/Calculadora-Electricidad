import tkinter as tk
from tkinter import ttk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CALCULADORA_ELECTRICIDAD_II:
    # Constructor
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("CALCULADORA - ELECTRICIDAD II")
        # Menú principal
        self.menu_label = ttk.Label(ventana, text="Elegir una opción:")
        self.menu_label.pack(pady=20, side=tk.LEFT)

        # Opciones del menú
        ventana.configure(background='#00BFBF')
        opciones = ["Calculadora de Filtros", "Reducción de Circuitos"]
        self.opcion_variable = tk.StringVar()
        self.opciones_combobox = ttk.Combobox(self.ventana, textvariable=self.opcion_variable, values=opciones)
        self.opciones_combobox.pack(pady=5, side=tk.LEFT)

        self.boton_seleccionar = ttk.Button(ventana, text="Elegir",command=self.seleccionar_opcion)
        self.boton_seleccionar.pack(pady=10,side=tk.LEFT)

        # Tipos de filtro 
        self.filtro_label = ttk.Label(self.ventana, text="Elija un tipo de filtro:")
        self.filtro_variable = tk.StringVar()
        tipos_filtro = ["Pasa Bajas", "Pasa Altas", "Pasa Banda", "Suprime Banda"]
        self.filtro_combobox = ttk.Combobox(self.ventana, textvariable=self.filtro_variable, values=tipos_filtro)
        self.filtro_combobox.pack(pady=5)
        self.filtro_label.pack_forget()
        self.filtro_combobox.pack_forget()

        # Reducción de circuitos 
        self.reducir_label = ttk.Label(self.ventana, text="Elija un tipo de reducción:")
        self.reducir_variable = tk.StringVar()
        tipos_reduccion = ["Serie", "Paralelo"]
        self.reducir_combobox = ttk.Combobox(self.ventana, textvariable=self.reducir_variable, values=tipos_reduccion)
        self.reducir_combobox.pack(pady=5)
        self.reducir_label.pack_forget()
        self.reducir_combobox.pack_forget()

        # Datos del filtro 
        self.resistencia_label = ttk.Label(self.ventana, text="Resistencia (Ω):")
        self.resistencia_label.pack(pady=5)
        self.resistencia_entrada = ttk.Entry(self.ventana)
        self.resistencia_entrada.pack(pady=5)

        self.inductor_label = ttk.Label(self.ventana, text="Inductancia (H):")
        self.inductor_label.pack(pady=5)
        self.inductor_entrada = ttk.Entry(self.ventana)
        self.inductor_entrada.pack(pady=5)

        self.capacitor_label = ttk.Label(self.ventana, text="Capacitancia (F):")
        self.capacitor_label.pack(pady=5)
        self.capacitor_entrada = ttk.Entry(self.ventana)
        self.capacitor_entrada.pack(pady=5)

        # Frecuencia para el resultado del filtro 
        self.frecuencia_label = ttk.Label(self.ventana, text="Frecuencia (Hz):")
        self.frecuencia_label.pack(pady=5)
        self.frecuencia_entrada = ttk.Entry(self.ventana)
        self.frecuencia_entrada.pack(pady=5)

        self.boton_respuesta = ttk.Button(ventana, text="Resultado", command=self.respuesta_filtro)
        self.boton_respuesta.pack(pady=10,side=tk.RIGHT)

        # Botón para reiniciar los datos
        self.boton_borrar = ttk.Button(ventana, text="Reniciar", command=self.borrar_entradas)
        self.boton_borrar.pack(pady=10,side=tk.RIGHT)

        # Resultado de la operación
        self.resultados_label = ttk.Label(self.ventana, text="")
        self.resultados_label.pack(pady=10)

        # Datos del circuito para reducción en serie o paralelo 
        self.resistencia1_label = ttk.Label(self.ventana, text="Resistencia 1 (Ω):")
        self.resistencia1_label.pack(pady=5)
        self.resistencia1_entrada = ttk.Entry(self.ventana)
        self.resistencia1_entrada.pack(pady=5)

        self.resistencia2_label = ttk.Label(self.ventana, text="Resistencia 2 (Ω):")
        self.resistencia2_label.pack(pady=5)
        self.resistencia2_entrada = ttk.Entry(self.ventana)
        self.resistencia2_entrada.pack(pady=5)

        self.inductor1_label = ttk.Label(self.ventana, text="Inductor 1 (H):")
        self.inductor1_label.pack(pady=5)
        self.inductor1_entrada = ttk.Entry(self.ventana)
        self.inductor1_entrada.pack(pady=5)

        self.inductor2_label = ttk.Label(self.ventana, text="Inductor 2 (H):")
        self.inductor2_label.pack(pady=5)
        self.inductor2_entrada = ttk.Entry(self.ventana)
        self.inductor2_entrada.pack(pady=5)

        self.capacitor1_label = ttk.Label(self.ventana, text="Capacitor 1 (F):")
        self.capacitor1_label.pack(pady=5)
        self.capacitor1_entrada = ttk.Entry(self.ventana)
        self.capacitor1_entrada.pack(pady=5)

        self.capacitor2_label = ttk.Label(self.ventana, text="Capacitor 2 (F):")
        self.capacitor2_label.pack(pady=5)
        self.capacitor2_entrada = ttk.Entry(self.ventana)
        self.capacitor2_entrada.pack(pady=5)

        # Ocultar elementos iniciales
        self.ocultar_parametros_filtro()
        self.ocultar_parametros_reduccion()

    def ocultar_parametros_filtro(self):
        self.filtro_label.pack_forget()
        self.filtro_combobox.pack_forget()
        self.resistencia_label.pack_forget()
        self.resistencia_entrada.pack_forget()
        self.inductor_label.pack_forget()
        self.inductor_entrada.pack_forget()
        self.capacitor_label.pack_forget()
        self.capacitor_entrada.pack_forget()
        self.frecuencia_label.pack_forget()
        self.frecuencia_entrada.pack_forget()

    def ocultar_parametros_reduccion(self):
        self.reducir_label.pack_forget()
        self.reducir_combobox.pack_forget()
        self.resistencia1_label.pack_forget()
        self.resistencia1_entrada.pack_forget()
        self.resistencia2_label.pack_forget()
        self.resistencia2_entrada.pack_forget()
        self.inductor1_label.pack_forget()
        self.inductor1_entrada.pack_forget()
        self.inductor2_label.pack_forget()
        self.inductor2_entrada.pack_forget()
        self.capacitor1_label.pack_forget()
        self.capacitor1_entrada.pack_forget()
        self.capacitor2_label.pack_forget()
        self.capacitor2_entrada.pack_forget()

    def seleccionar_opcion(self):
        self.opcion_seleccionada = self.opcion_variable.get()
        if self.opcion_seleccionada == "Calculadora de Filtros":

            # Mostrar la interfaz de la calculadora de filtros
            self.ocultar_parametros_reduccion()
            self.mostrar_parametros_filtro()
        elif self.opcion_seleccionada == "Reducción de Circuitos":

            # Mostrar la interfaz de la reducción de circuitos
            self.ocultar_parametros_filtro()
            self.mostrar_parametros_reduccion()

    def mostrar_parametros_filtro(self):
        self.filtro_label.pack(pady=5)
        self.filtro_combobox.pack(pady=5)
        self.resistencia_label.pack(pady=5)
        self.resistencia_entrada.pack(pady=5)
        self.inductor_label.pack(pady=5)
        self.inductor_entrada.pack(pady=5)
        self.capacitor_label.pack(pady=5)
        self.capacitor_entrada.pack(pady=5)
        self.frecuencia_label.pack(pady=5)
        self.frecuencia_entrada.pack(pady=5)

    def mostrar_parametros_reduccion(self):
        self.reducir_label.pack(pady=5)
        self.reducir_combobox.pack(pady=5)
        self.resistencia1_label.pack(pady=5)
        self.resistencia1_entrada.pack(pady=5)
        self.resistencia2_label.pack(pady=5)
        self.resistencia2_entrada.pack(pady=5)
        self.inductor1_label.pack(pady=5)
        self.inductor1_entrada.pack(pady=5)
        self.inductor2_label.pack(pady=5)
        self.inductor2_entrada.pack(pady=5)
        self.capacitor1_label.pack(pady=5)
        self.capacitor1_entrada.pack(pady=5)
        self.capacitor2_label.pack(pady=5)
        self.capacitor2_entrada.pack(pady=5)
        self.frecuencia_label.pack(pady=5)
        self.frecuencia_entrada.pack(pady=5)

    def mostrar_calculadora_filtros(self):

        # Ocultar los elementos de la reducción de circuitos
        self.reducir_label.pack_forget()
        self.reducir_combobox.pack_forget()
        self.resistencia1_label.pack_forget()
        self.resistencia1_entrada.pack_forget()
        self.resistencia2_label.pack_forget()
        self.resistencia2_entrada.pack_forget()
        self.inductor1_label.pack_forget()
        self.inductor1_entrada.pack_forget()
        self.inductor2_label.pack_forget()
        self.inductor2_entrada.pack_forget()
        self.capacitor1_label.pack_forget()
        self.capacitor1_entrada.pack_forget()
        self.capacitor2_label.pack_forget()
        self.capacitor2_entrada.pack_forget()

        # Mostrar los elementos de la calculadora de filtros
        self.filtro_label.pack(pady=5)
        self.filtro_combobox.pack(pady=5)
        self.resistencia_label.pack(pady=5)
        self.resistencia_entrada.pack(pady=5)
        self.inductor_label.pack(pady=5)
        self.inductor_entrada.pack(pady=5)
        self.capacitor_label.pack(pady=5)
        self.capacitor_entrada.pack(pady=5)
        self.frecuencia_label.pack(pady=5)
        self.frecuencia_entrada.pack(pady=5)

    def mostrar_reduccion(self):
        # Ocultar los elementos de la calculadora de filtros
        self.filtro_label.pack_forget()
        self.filtro_combobox.pack_forget()
        self.resistencia_label.pack_forget()
        self.resistencia_entrada.pack_forget()
        self.inductor_label.pack_forget()
        self.inductor_entrada.pack_forget()
        self.capacitor_label.pack_forget()
        self.capacitor_entrada.pack_forget()
        self.frecuencia_label.pack(pady=5)
        self.frecuencia_entrada.pack(pady=5)

        # Mostrar los elementos de la reducción de circuitos
        self.reducir_label.pack(pady=5)
        self.reducir_combobox.pack(pady=5)
        self.resistencia1_label.pack(pady=5)
        self.resistencia1_entrada.pack(pady=5)
        self.resistencia2_label.pack(pady=5)
        self.resistencia2_entrada.pack(pady=5)
        self.inductor1_label.pack(pady=5)
        self.inductor1_entrada.pack(pady=5)
        self.inductor2_label.pack(pady=5)
        self.inductor2_entrada.pack(pady=5)
        self.capacitor1_label.pack(pady=5)
        self.capacitor1_entrada.pack(pady=5)
        self.capacitor2_label.pack(pady=5)
        self.capacitor2_entrada.pack(pady=5)

    def respuesta_filtro(self):
        if self.opcion_variable.get() == "Calculadora de Filtros":
            self.calcular_respuesta_filtro()
        elif self.opcion_variable.get() == "Reducción de Circuitos":
            self.calcular_respuesta_reduccion()

    def calcular_respuesta_filtro(self):
        # Obtener el tipo de filtro seleccionado
        global transferir_funcion
        filtro_seleccionado = self.filtro_variable.get()

        # Obtener los valores de los parámetros desde las entradas del usuario
        try:
            resistencia_valor = self.convertir_valor(self.resistencia_entrada.get())
            inductor_valor = self.convertir_valor(self.inductor_entrada.get())
            capacitor_valor = self.convertir_valor(self.capacitor_entrada.get())
            frecuencia_valor = self.convertir_valor(self.frecuencia_entrada.get())
        except ValueError:
            self.resultados_label.config(text="Ingrese valores numéricos para resistencia, inductancia, capacitancia y frecuencia.")
            return

        # Crear un rango de las frecuencias para la respuesta del filtro
        frecuencias = np.logspace(1, 6, 400)
        omega = 2 * np.pi * frecuencias

        # Calcular la respuesta de los filtros para la frecuencia especificada
        if filtro_seleccionado == "Pasa Bajas":
            if capacitor_valor != 0:
                transferir_funcion = 1 / (1 + 1j * omega * capacitor_valor * resistencia_valor)
            elif inductor_valor != 0:
                transferir_funcion = 1 / (1 + 1j * omega / (inductor_valor * resistencia_valor))
            else:
                # En caso de que ambos capacitor e inductor sean 0, la transferencia no está definida
                self.resultados_label.config(
                    text="Error: Ambos capacitor e inductor no pueden ser 0 en un filtro de Pasa Bajos.")
                return
        elif filtro_seleccionado == "Pasa Altas":
            if capacitor_valor != 0:
                transferir_funcion = 1 / (1 + 1 / (1j * omega * capacitor_valor * resistencia_valor))
            elif inductor_valor != 0:
                transferir_funcion = 1 / (1 + (1j * omega * resistencia_valor) / inductor_valor)
            else:
                # En caso de que ambos capacitor e inductor sean 0, la transferencia no está definida
                self.resultados_label.config(
                    text="Error: Ambos capacitor e inductor no pueden ser 0 en un filtro de Pasa Altos.")
                return
        elif filtro_seleccionado == "Pasa Banda":
            transferir_funcion = 1 / (1 + 1j * omega * (capacitor_valor * resistencia_valor) / (1 + 1j * omega * inductor_valor))
        elif filtro_seleccionado == "Rechaza Banda":
            transferir_funcion = 1 / (1 + 1j * omega * inductor_valor / (1 + 1j * omega * capacitor_valor * resistencia_valor))

        # Calcular la respuesta para la frecuencia especificada
        transferir_funcion_de_frecuencia = np.interp(frecuencia_valor, frecuencias, transferir_funcion)

        # Mostrar la respuesta del filtro en un gráfico
        self.mostrar_grafico(frecuencias, transferir_funcion, transferir_funcion_de_frecuencia)

    def calcular_respuesta_reduccion(self):
        try:
            resistencia1_valor = self.convertir_valor(self.resistencia1_entrada.get())
            resistencia2_valor = self.convertir_valor(self.resistencia2_entrada.get())
            inductor1_valor = self.convertir_valor(self.inductor1_entrada.get())
            inductor2_valor = self.convertir_valor(self.inductor2_entrada.get())
            capacitor1_valor = self.convertir_valor(self.capacitor1_entrada.get())
            capacitor2_valor = self.convertir_valor(self.capacitor2_entrada.get())
            frecuencia = self.convertir_valor(self.frecuencia_entrada.get())
        except ValueError:
            self.resultados_label.config(
                text="Ingrese valores numéricos para resistencias, inductores, capacitores y la frecuencia")
            return

        # Determinar el tipo de reducción (en serie o en paralelo)
        tipo_reduccion = self.reducir_variable.get()

        # Calcular la resistencia, inductancia y capacitancia total
        if tipo_reduccion == "Serie":
            resistencia_total = resistencia1_valor + resistencia2_valor
            inductancia_total = inductor1_valor + inductor2_valor
            capacitancia_total = capacitor1_valor + capacitor2_valor
        elif tipo_reduccion == "Paralelo":
            resistencia_total = 1 / (1 / resistencia1_valor + 1 / resistencia2_valor)
            inductancia_total = 1 / (1 / inductor1_valor + 1 / inductor2_valor)
            capacitancia_total = capacitor1_valor + capacitor2_valor
        else:
            self.resultados_label.config(text="Tipo de reducción no reconocido.")
            return

        # Calcular la frecuencia angular
        omega = 2 * np.pi * frecuencia

        # Calcular la impedancia total en serie
        impedancia_total_serie = resistencia_total + 1j * (omega * inductancia_total - 1 / (omega * capacitancia_total))

        # Calcular la impedancia total en paralelo
        impedancia_total_paralelo = 1 / (
                    1 / resistencia_total + 1j * omega * inductancia_total - 1 / (1j * omega * capacitancia_total))

        # Formatear el texto de los resultados
        texto_resultado = f"Impedancia Total en Serie: {impedancia_total_serie}\n"
        texto_resultado += f"Diagrama Fasorial en Serie: {np.abs(impedancia_total_serie):.4f} Ω ∠ {np.angle(impedancia_total_serie, deg=True):.4f} grados\n\n"
        texto_resultado += f"Impedancia Total en Paralelo: {impedancia_total_paralelo}\n"
        texto_resultado += f"Diagrama Fasorial en Paralelo: {np.abs(impedancia_total_paralelo):.4f} Ω ∠ {np.angle(impedancia_total_paralelo, deg=True):.4f} grados\n\n"

        texto_resultado += f"Valores Totales:\n"
        texto_resultado += f"Resistencia Total: {resistencia_total}\n"
        texto_resultado += f"Inductancia Total: {inductancia_total}\n"
        texto_resultado += f"Capacitancia Total: {capacitancia_total}"

        # Actualizar la etiqueta de resultados
        self.resultados_label.config(text=texto_resultado)

    def mostrar_grafico(self, frecuencias, transferir_funcion, transferir_funcion_de_frecuencia):
        # Limpiar la ventana de gráficos anterior si existe
        if hasattr(self, 'marco_grafico'):
            self.marco_grafico.destroy()

        # Crear un nuevo marco para el gráfico
        self.marco_grafico = ttk.Frame(self.ventana)
        self.marco_grafico.pack(pady=10)

        # Crear un gráfico con dos subtramas apiladas horizontalmente, 1 fila 2 columnas
        fig, (ax_magnitud, ax_fase) = plt.subplots(1, 2, figsize=(12, 6))

        # Gráfico de Magnitud
        ax_magnitud.semilogx(frecuencias, np.abs(transferir_funcion))
        ax_magnitud.set_title('Respuesta en Magnitud')
        ax_magnitud.set_xlabel('Frecuencia (Hz)')
        ax_magnitud.set_ylabel('Magnitud')

        # Gráfico de Fase
        ax_fase.semilogx(frecuencias, np.angle(transferir_funcion, deg=True))
        ax_fase.set_title('Respuesta en Fase')
        ax_fase.set_xlabel('Frecuencia (Hz)')
        ax_fase.set_ylabel('Fase (grados)')

        # Añadir etiqueta con la respuesta para la frecuencia especificada
        ax_magnitud.annotate(f'Respuesta a {self.frecuencia_entrada.get()} Hz:\n'
                             f'Magnitud: {np.abs(transferir_funcion_de_frecuencia):.4f}\n'
                             f'Fase: {np.angle(transferir_funcion_de_frecuencia, deg=True):.4f} grados',
                             xy=(0.02, 0.75), xycoords='axes fraction', fontsize=8,
                             bbox=dict(boxstyle="round", alpha=0.1))

        # Incorporar el gráfico en la interfaz gráfica
        canvas = FigureCanvasTkAgg(fig, master=self.marco_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def borrar_entradas(self):
        # Borrar los datos en los campos de entrada
        self.opcion_variable.set("")
        self.filtro_variable.set("")
        self.reducir_variable.set("")
        self.resistencia_entrada.delete(0, tk.END)
        self.resistencia1_entrada.delete(0, tk.END)
        self.resistencia2_entrada.delete(0, tk.END)
        self.inductor_entrada.delete(0, tk.END)
        self.inductor1_entrada.delete(0, tk.END)
        self.inductor2_entrada.delete(0, tk.END)
        self.capacitor_entrada.delete(0, tk.END)
        self.capacitor1_entrada.delete(0, tk.END)
        self.capacitor2_entrada.delete(0, tk.END)
        self.frecuencia_entrada.delete(0, tk.END)
        self.resultados_label.config(text="")
        # Limpiar la ventana de gráficos, si existe
        if hasattr(self, 'marco_grafico'):
            self.marco_grafico.destroy()

    def convertir_valor(self, valor_convertido):
        # Función para convertir valores con prefijos a números
        prefijos = {'k': 1e3, 'M': 1e6, 'm': 1e-3, 'n': 1e-9, 'u': 1e-6, 'p': 1e-12}
        for prefijos, multiplier in prefijos.items():
            if valor_convertido.endswith(prefijos):
                return float(valor_convertido[:-1]) * multiplier
        return float(valor_convertido)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CALCULADORA_ELECTRICIDAD_II(ventana)
    ventana.mainloop()



