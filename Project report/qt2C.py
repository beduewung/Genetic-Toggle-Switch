import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#values

k_mLb = 0.0082
k_mTb = 0.0149
k_mLa = 1.0
k_mTa = 0.3865
theta_L = 600
theta_T = 500
n_L = 4.0
n_T = 4.0
gamma_mL = 0.04
gamma_mT = 0.04
k_pT = 0.1
k_pL = 0.1
gamma_pL = 0.002
gamma_pT = 0.002

pL = 0
pT = 0

arguments = [pL,pT]
params = [k_mLb, k_mTb, k_mLa, k_mTa, theta_L, theta_T, n_L, n_T, gamma_mL, gamma_mT, k_pT, k_pL, gamma_pL, gamma_pT]


def toggle_derivative (y,t,args):
    
    k_mLb, k_mTb, k_mLa, k_mTa, theta_L, theta_T, n_L, n_T, gamma_mL, gamma_mT, k_pT, k_pL, gamma_pL, gamma_pT = args
    pL, pT = y

    mL = (k_mLb + k_mLa * 1/(1+(pT/theta_T)**n_T))*(1/gamma_mL)
    dpLdt = (k_pL * mL) - (gamma_pL * pL)

    mT = (k_mTb + k_mTa * 1/(1+(pL/theta_L)**n_L))*(1/gamma_mT)
    dpTdt = (k_pT * mT)  - (gamma_pT * pT)
    
    return [dpLdt, dpTdt]


time = np.linspace(0,3000,3001)

solutions = odeint(toggle_derivative, arguments, time, args=(params,))


plt.plot(solutions[:,0], solutions[:, 1], 'g', label='[TetR]')
plt.xlabel('LacI')
plt.ylabel('TetR')
plt.title('Concentration of TetR as a fucntion of the concentration of LacI')
plt.legend()
plt.show()

