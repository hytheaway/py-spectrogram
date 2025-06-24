import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

wavfile_path = input('Path to wav file: ')
start_ms = input('Start time (ms): ')
end_ms = input('End time (ms): ')
plot_title = input('Plot title: ')
dynamic_range_min = input('Intensity scale min (dB): ')
dynamic_range_max = input('Intensity scale max (dB): ')

if not plot_title:
    plot_title = str(wavfile_path.split("/")[len(wavfile_path.split("/"))-1]) # python should convert this to whatever os

sr, samples = wavfile.read(str(wavfile_path))

if len(samples.shape) > 1:
    samples = samples.transpose()[0]

if not start_ms:
    start_ms = '0'

if not end_ms:
    end_ms = str((len(samples) / sr) * 1000)

start_in_samples = (float(start_ms)/1000) * sr
end_in_samples = (float(end_ms)/1000) * sr

if start_in_samples >= end_in_samples:
    print("Error: End time cannot be equal to or less than start time.")
    quit()

start_in_samples = int(start_in_samples)
end_in_samples = int(end_in_samples)
rebound_samples = samples[start_in_samples:end_in_samples]

f, t, spectrogram = signal.spectrogram(rebound_samples, sr)

fig, ax = plt.subplots()
# i could've done this better
if dynamic_range_min and dynamic_range_max:
    p = ax.pcolormesh(t, f, 10*np.log10(spectrogram), vmin=int(dynamic_range_min), vmax=int(dynamic_range_max), shading='auto')
elif not dynamic_range_min and dynamic_range_max:
    p = ax.pcolormesh(t, f, 10*np.log10(spectrogram), vmax=int(dynamic_range_max), shading='auto')
elif dynamic_range_min and not dynamic_range_max:
    p = ax.pcolormesh(t, f, 10*np.log10(spectrogram), vmin=int(dynamic_range_min), shading='auto')
else:
    p = ax.pcolormesh(t, f, 10*np.log10(spectrogram), shading='auto')
ax.set_ylim(1, int(sr/2))
ax.set_ylabel('Frequency (Hz)')
ax.set_xlabel('Time (s)')

fig.colorbar(p, label='Intensity (dB)')

plt.title(str(plot_title))
plt.show()