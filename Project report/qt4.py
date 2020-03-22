import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

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
    
    mL, mT, pL, pT = y
    
    dmLdt = k_mLb + k_mLa * 1/(1+((pT/theta_T)**n_T)) - gamma_mL * mL 
    
    dpLdt = k_pL * mL - gamma_pL * pL
    
    dmTdt = k_mTb + k_mTa * 1/(1+((pL/theta_L)**n_L)) - gamma_mT * mT
    
    dpTdt = k_pT * mT - gamma_pT * pT
    
    return [dmLdt, dmTdt, dpLdt, dpTdt]

time = np.linspace(0,3000,3001)
y0 = [0, 0, 0, 0]

solutions = odeint( toggle_derivative, y0, time, args=(params,))
   
mL = solutions[:,0]
mT = solutions[:,1]
pL = solutions[:,2]
pT = solutions[:,3]

def draw_phase_space (args):
    k_mLb, k_mTb, k_mLa, k_mTa, theta_L, theta_T, n_L, n_T, gamma_mL, gamma_mT, k_pT, k_pL, gamma_pL, gamma_pT = args

    #Part 1: draw LacI/TetR vector field
    pL_vector = np.linspace(0,2000,30)
    pT_vector = np.linspace(0,2000,30) 
    LacI_vector, TetR_vector = np.meshgrid(pL_vector, pT_vector)

    #Expressions for steady-state concentrations of mRNAs: mL and mT
    mL_vector = (k_mLb + k_mLa * 1/(1+(pT_vector/theta_T)**n_T))*(1/gamma_mL)
    mT_vector = (k_mTb + k_mTa * 1/(1+(pL_vector/theta_L)**n_L))*(1/gamma_mT)

    #Compute the value of the derivative of pL and pT for each pair of values in pL_vector and pT_vector
    aux1 = [0]*1225
    aux2 = [0]*1225
    counter = 0
    
    for i in range(30):
        for j in range(30):
            mL, mT, pL, pT = toggle_derivative([mL_vector[i], mT_vector[j], pL_vector[j], pT_vector[i]],0,args)
            aux1[counter] = pL
            aux2[counter] = pT
            counter+=1

    # plot the vector field in the protein state space
    plt.quiver(LacI_vector, TetR_vector, aux1, aux2)

    ## Part 2: draw the LacI and TetR nullclines in the protein state space, using a steady state approximation for the mRNAs
    LacI_vector= np.linspace(0,2000,30)
    TetR_vector= np.linspace(0,2000,30)

    # expression of LacI and TetR nullclines
    nLacI_vector = (k_pL * mL_vector)/gamma_pL
    nTetR_vector = (k_pT * mT_vector)/gamma_pT

    # plot nullclines
    plt.plot(nLacI_vector,TetR_vector,'g')
    plt.plot(LacI_vector,nTetR_vector,'c')
    plt.title('Vector field and evolution of the mRNA as a function of  time')
    plt.xlabel('Time')
    plt.ylabel('Evolution of the mRNA')
    plt.show()

draw_phase_space([k_mLb, k_mTb, k_mLa, k_mTa, theta_L, theta_T, n_L, n_T, gamma_mL, gamma_mT, k_pT, k_pL, gamma_pL, gamma_pT])
