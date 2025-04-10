import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

wavfile_path = input('Path to wav file: ')

sample_rate, samples = wavfile.read(str(wavfile_path))

frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, 10*np.log10(spectrogram), shading='gouraud')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.colorbar(label='Intensity (dB)')
plt.show()