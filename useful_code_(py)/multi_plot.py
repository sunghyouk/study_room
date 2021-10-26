import matplotlib.pyplot as plt
import librosa
import librosa.display

audio = 'discomfort/discomfort_1.wav'
y, sr = librosa.load(audio)

folder = ['discomfort', 'hungry', 'laugh', 'tired']
set_label = []

# multiple plot in one window
for i in range(1, 10):
    plt.subplot(3, 3, i)
    a = folder[0] + '/' + folder[0] + '_' + str(i) + '.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr = sr)
    plt.title(folder[0] + str(i))
plt.tight_layout()
plt.show()