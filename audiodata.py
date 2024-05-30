import matplotlib.pyplot as plt
import wave
import numpy as np
with wave.open('C:\Users\VenkataHarshavardhan\Desktop\CL LAB\Chorus.wav','rb')as wav_file:
    audio_data = wav_file.readframes(wav_file.genframes)
audio_array= np.from buffer (audio_data, dtype=np.int 16)
plt.plot(audio_array)
plt.xlabel('time(samples)')
plt.ylabel('amplitude')
plt.title('wav file audio data')
plt.show()