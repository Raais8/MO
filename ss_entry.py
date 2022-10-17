import numpy as np
import matplotlib.pyplot as plt
from math import pi
import parameter_calcs as pc

#Planet parameter list format [eccentricity, x0, y0, major semi-axis, minor-semiaxis]
marsParams = pc.marsParams
mercuryParams = pc.mercuryParams
earthParams = pc.earthParams
jupiterParams = pc.jupiterParams
venusParams = pc.venusParams
craftParams = pc.craftParams

#MARS and MERCURY minor semi-axis
marsParams[4] = np.sqrt(np.power(marsParams[3], 2) - np.power(marsParams[3], 2) * np.power(marsParams[0], 2))
mercuryParams[4] = np.sqrt(np.power(mercuryParams[3], 2) - np.power(mercuryParams[3], 2) * np.power(mercuryParams[0], 2))


#MARS and MERCURY orbit focus
marsParams[1] = marsParams[0] * marsParams[3]
mercuryParams[1] = - mercuryParams[0] * mercuryParams[3] * np.cos(np.radians(77.4))
mercuryParams[2] = mercuryParams[0] * mercuryParams[3] * np.sin(np.radians(77.4))

t = np.linspace(0, 2*pi, 100)
f = np.linspace(-1.5, 1.5, 100)

fig, ax = plt.subplots()

plt.plot(mercuryParams[1] + mercuryParams[3]*np.cos(t - np.radians(257.4)), mercuryParams[2] + mercuryParams[4]*np.sin(t - np.radians(257.4)), "--", color='gray') #MERCURY orbit
plt.plot(venusParams[1] + venusParams[3]*np.cos(t), venusParams[2] + venusParams[4]*np.sin(t), "--", color='red') #VENUS orbit
plt.plot(earthParams[1] + earthParams[3]*np.cos(t), earthParams[2] + earthParams[4]*np.sin(t), "--", color='blue') #EARTH orbit
plt.plot(marsParams[1] + marsParams[3]*np.cos(t), marsParams[2] + marsParams[4]*np.sin(t), "--", color='orange') #MARS orbit
plt.plot(jupiterParams[1] + jupiterParams[3]*np.cos(t), jupiterParams[2] + jupiterParams[4]*np.sin(t), "--", color='brown') #JUPITER orbit

plt.plot(craftParams[1] - craftParams[3]*np.cosh(f), craftParams[2] + craftParams[4]*np.sinh(f), "--", color='purple') #CRAFT orbit

plt.plot(0, 0, marker="o", markeredgecolor="yellow", markerfacecolor="red")

# r = np.linspace(-0.2, 0.2, 10)
j = np.linspace(-4, 4, 10)
# plt.plot(r, -4.47*r)
# plt.plot(j, -np.sqrt(3)*j)
# plt.plot(j, np.sqrt(3)*j)

ax.set_aspect(1)
fig.set_size_inches(5, 8)
fig.savefig("ss_entry.png", dpi = 100)