#!usr/bin/env python
from tkinter import *
from turtle import pos
import pyaudio
import scipy.io.wavfile as wavfile
import matplotlib.pylab as plt
import wave
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# FUNCIONES PARA LOS BOTONES
def grabar():
    global data, CHANNELS, RATE, FORMAT, arreglo, p
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 3
    samples = (RATE/1024)*RECORD_SECONDS
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=chunk)
    stream1 = p.open(format=FORMAT, channels=CHANNELS,
                     rate=RATE, output=True, frames_per_buffer=chunk)
    print("REC")
    arreglo = []
    for i in range(0, int(samples)):
        data = stream.read(chunk)
        arreglo.append(data)
    stream.stop_stream()
    stream.close()
    stream1.stop_stream()
    stream1.close()
    wf = wave.open('audio.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setframerate(RATE)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.writeframes(b''.join(arreglo))
    wf.close()
    rate, data = wavfile.read("audio.wav")
    print(rate)
    plt.figure(1)
    plt.plot(data)
    plt.show()

def dividir():
    global palabras
    palabras = []
    c = 1
    posiciones = len(data)+1
    bandera = 0
    for posicion in range(posiciones):
        rango_min = posicion
        rango_max = posicion + 1000
        ventana = data[rango_min:rango_max]/max(data)
        E = sum([n**2 for n in ventana])
        if E >= 1.2690844527164464 and bandera == posicion and bandera > 0:
            print(E)
            for pos in range(posicion, posiciones):
                rango_min = pos
                rango_max = pos + 1000
                ventana = data[rango_min:rango_max]/max(data)
                E = sum([n**2 for n in ventana])
                if E <= 1.2690844527164464:
                    value = {
                        str(c): data[posicion:rango_max]
                    }
                    palabras.append(value)
                    c += c
                    bandera = rango_max
                    break
        elif bandera == posicion:
            bandera = rango_max
            print(bandera)
    cantidad = len(palabras)
    can_num_label = Label(
        ventana, text="NUMERO DE PALABRAS :", font=("Agency FB", 14)).place(x=110, y=100)
    can_num = Label(ventana, text=str(cantidad),
                    font=("Agency FB", 14), fg = "red").place(x=270, y=100)

def sonar():
    num = son_num.get("1.0", "end-1c")
    if palabras[0][str(num)]:
        data2 = palabras[0][str(num)]
        plt.figure(2)
        plt.plot(data2)
        plt.show()

# creando la ventana
ventana = Tk()
ventana.geometry("500x500+100+200")
ventana.title("INTERFAZ GRAFICA")
son_num = Text(ventana, height = 1, width = 5).place(x=200, y=270)
btnsaludar = Button(ventana, text="SONAR", command=sonar,
                    font=("Agency FB", 14)).place(x=200, y=300)
btnsaludar = Button(ventana, text="GRABAR", command=grabar,
                    font=("Agency FB", 14)).place(x=100, y=400)
btnsdespedir = Button(ventana, text="DIVIDIR", command=dividir,
                      font=("Agency FB", 14),).place(x=300, y=400)
ventana.mainloop()
