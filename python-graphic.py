import numpy as np
import matplotlib.pyplot as plt


A = 1.0      
omega = 2.0    
phi = np.pi/4  


t = np.linspace(0, 2 * np.pi, 1000)

f_t = A * np.sin(omega * t + phi)


f_prime_t = A * omega * np.cos(omega * t + phi)


plt.figure(figsize=(10, 6))
plt.plot(t, f_t, label='f(t) = A sin(omega t + phi)')
plt.plot(t, f_prime_t, label="f'(t) = A omega cos(omega t + phi)", linestyle='--')
plt.xlabel('Tempo (t)')
plt.ylabel('Amplitude')
plt.title('Função senoidal e sua derivada')
plt.legend()
plt.grid(True)
plt.show()
