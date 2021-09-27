import librosa
import librosa.display
import matplotlib.pyplot as plt

folder = ['discomfort', 'hungry', 'laugh', 'tired']

for i in range(1, 10):
    plt.subplot(3, 3, i)
    a = folder[0] + '/' + folder[0] + '_' + str(i) + '.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr = sr)
    plt.title(folder[0] + str(i))
plt.tight_layout()
plt.show()