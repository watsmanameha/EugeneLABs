import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq
from scipy.signal import find_peaks

signal = np.load('signal_2.npy')

FD = 10000  # Частота дискретизации
N = len(signal)  # Количество отсчетов равно длине сигнала

spectrum = rfft(signal)

plt.figure(figsize=(10, 6))

# Сигнал зашумленный
plt.subplot(2, 1, 1)
time = np.arange(N) / float(FD)
plt.plot(time, signal)
plt.xlabel('Время, с')
plt.ylabel('Напряжение, мВ')
plt.title('Зашумленный сигнал')

# Спектр сигнала (частотный диапазон)
plt.subplot(2, 1, 2)
frequency = rfftfreq(N, 1.0 / FD)  # Вычисление частот для спектра
plt.plot(frequency, np.abs(spectrum), 'r')  # Чистый сигнал будет нарисован красным
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.title('Спектр сигнала')
plt.grid(True)

plt.tight_layout()

# Сохранение графика в файл
plt.savefig('signal_plot.png')

# Find peaks with custom parameters
peaks, _ = find_peaks(np.abs(spectrum), height=20000)

# Convert peak indices to frequencies in Hertz
peak_frequencies = frequency[peaks]

# Print the peak frequencies and their amplitudes
print("Peak frequencies (Hz):", peak_frequencies)
print("Peak amplitudes:", np.abs(spectrum)[peaks])
