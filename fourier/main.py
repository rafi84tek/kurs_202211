"""
Transformata Fouriera

"""

import numpy as np
import matplotlib.pyplot as plt


#okreslenie rozmiaru próbki
samplingFrequency = 100

#interwał - funkcja falowa, sinusoida
# [Hz] = 1/s
samplingInterval = 1 / samplingFrequency
beginTime = 0
endTime = 10

#e3finicja dwóćh syngnałów w [Hz]
signal1Frequency = 4
signal2Frequency = 7

#zakres badanego czasu, z podziałem do samplingInterval,
#NumPy tworzy dla nas zakres
time = np.arange(beginTime, endTime, samplingInterval)

amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)
amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)

#robimy wykres
figure, axis = plt.subplots(4, 1) #subplots = tu 4 wykresy na 1
plt.subplots_adjust(hspace=1) #horizontal space, żeby ładnie wyglądało

#wykres nr 1
axis[0].set_title('funkcja falowa z sygnałem 4 hz')
axis[0].plot(time, amplitude1) #co na osiach
axis[0].set_xlabel("czas") #opis osi
axis[0].set_ylabel("amplitura") #opis osi

#wykres nr 2
axis[1].set_title('funkcja falowa z sygnałem 7 hz')
axis[1].plot(time, amplitude2) #co na osiach
axis[1].set_xlabel("czas") #opis osi
axis[1].set_ylabel("amplitura") #opis osi


#składanie funkcji
amplitude = amplitude1 + amplitude2
#wykres nr 3 - złożenie funkcji
axis[2].set_title('złożenie dwóch funkcji falowych')
axis[2].plot(time, amplitude) #co na osiach
axis[2].set_xlabel("czas") #opis osi
axis[2].set_ylabel("amplitura") #opis osi


#Transformata Fouriera
tpCount = len(amplitude) #ile elementów zawiera funkcja, czyli na ile punktów jest rozłożona
fourierTransform = np.fft.fft(amplitude) / tpCount #transformata przerobi funkcję "amplitude", czyli nasze złożenie dwóch funkcji
# normalizacja / rozkłady - przekształcenie danych, by można je było porównać na wykresie
fourierTransform = fourierTransform[range(int(tpCount / 2))]

values = np.arange(int(tpCount / 2))
timePeriod = tpCount / samplingFrequency
frequencies = values / timePeriod

#wykres nr 4 - Transpormata Fouriera
axis[3].set_title('Transformata Fouriera funkcji amplitude')
axis[3].plot(frequencies, abs(fourierTransform)) #co na osiach
axis[3].set_xlabel("Częstotliwość") #opis osi
axis[3].set_ylabel("Amplitura") #opis osi

plt.show()
