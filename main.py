import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

wavfile_path = input('Path to wav file: ')

start_ms = input('Start time (ms): ')
end_ms = input('End time (ms): ')

sr, samples = wavfile.read(str(wavfile_path))

start_in_samples = (float(start_ms)/1000) * sr
end_in_samples = (float(end_ms)/1000) * sr

if start_in_samples >= end_in_samples:
    print("Error: End time cannot be equal to or less than start time.")
    quit()

start_in_samples = int(start_in_samples)
end_in_samples = int(end_in_samples)

rebound_samples = samples[start_in_samples:end_in_samples]

f, t, spectrogram = signal.spectrogram(rebound_samples, sr)

plt.pcolormesh(t, f, 10*np.log10(spectrogram), shading='gouraud')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.colorbar(label='Intensity (dB)')
plt.show()