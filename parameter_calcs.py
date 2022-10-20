from cmath import sqrt
import numpy as np

#Planet parameter list format [eccentricity, x0, y0, major semi-axis, minor-semiaxis]
marsParams = [0.093, 0, 0, 1.524, 0]
mercuryParams = [0.206, 0, 0, 0.387, 0]
earthParams = [0, 0, 0, 1, 1]
jupiterParams = [0, 0, 0, 5.2, 5.2]
venusParams = [0, 0, 0, 0.723, 0.723]
craftParams = [0, 0, 0, 0, 0]

#MARS and MERCURY minor semi-axis
marsParams[4] = np.sqrt(np.power(marsParams[3], 2) - np.power(marsParams[3], 2) * np.power(marsParams[0], 2))
mercuryParams[4] = np.sqrt(np.power(mercuryParams[3], 2) - np.power(mercuryParams[3], 2) * np.power(mercuryParams[0], 2))

#MARS and MERCURY orbit focus
marsParams[1] = marsParams[0] * marsParams[3]
mercuryParams[1] = - mercuryParams[0] * mercuryParams[3] * np.cos(np.radians(77.4))
mercuryParams[2] = mercuryParams[0] * mercuryParams[3] * np.sin(np.radians(77.4))

#CRAFT eccentricity and semi-axis
craftParams[0] = 8.8 / 6.8
craftParams[3] = 0.8 / (craftParams[0] - 1)
craftParams[1] = 0.8 + craftParams[3]
c = craftParams[3] * craftParams[0]
craftParams[4] = sqrt (np.power(c,2) - np.power(craftParams[3],2))