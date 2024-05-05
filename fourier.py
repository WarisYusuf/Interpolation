import numpy as np
import matplotlib.pyplot as plt

# Zeitvektor
t = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# Fourier-Reihe für k=1 bis k=5
f_t = (4 / np.pi) * (
    np.sin(t) +
    np.sin(3 * t) / 3 +
    np.sin(5 * t) / 5 +
    np.sin(7 * t) / 7 +
    np.sin(9 * t) / 9
)

# Perfektes Rechtecksignal
square_wave = np.sign(np.sin(t))

# Plot der Fourier-Annäherung und des perfekten Rechtecksignals
plt.figure(figsize=(12, 6))
plt.plot(t, f_t, label="Fourier Approximation für k=1 bis 5")
plt.plot(t, square_wave, linestyle='dashed', label="Perfektes Rechtecksignal", alpha=0.7)
plt.title("Fourier-Annäherung an ein Rechtecksignal")
plt.xlabel("t (Zeit)")
plt.ylabel("f(t)")
plt.legend()
plt.grid(True)
plt.show()

# Berechnung der maximalen Abweichung
max_deviation = np.max(np.abs(f_t - square_wave))
max_deviation
