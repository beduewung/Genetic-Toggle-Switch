import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k_mLb=0.0082
k_mTb=0.0149
k_mLa=1
k_mTa=0.3865
theta_L=600
theta_T=500
n_L=4
n_T=4
kp_L=0.1
kp_T=0.1
gamma_mL=gamma_mT=0.04
gamma_pL=gamma_pT=0.002

mRNAl=[]
mRNAt=[]
LacI=[]
TetR=[]

def toggle_derivative(y, t, args):
    
    mRNAl, mRNAt, LacI, TetR = y
    
    k_mLb,k_mTb,k_mLa,k_mTa,n_L,n_T,theta_L,theta_T,kp_L,kp_T,gamma_mL,gamma_mT,gamma_pL,gamma_pT = args
    
    dmLdt = k_mLb + k_mLa / (1 + ((TetR / theta_T)**n_T)) - gamma_mL * mRNAl
    dmTdt = k_mTb + k_mTa / (1 + ((LacI / theta_L)**n_L)) - gamma_mT * mRNAt
    dLdt = kp_L * mRNAl - gamma_pL * LacI
    dTdt = kp_T * mRNAt - gamma_pT * TetR 
                         
    return  [dmLdt, dmTdt,dLdt,dTdt]

rates=[k_mLb,k_mTb,k_mLa,k_mTa,n_L,n_T,theta_L,theta_T,kp_L,kp_T,gamma_mL,gamma_mT,gamma_pL,gamma_pT]
y0 = [0,0,0,0]
t = np.linspace(0,2000,300)

solution1 = odeint(toggle_derivative,y0,t, args=(rates,))


rates=[k_mLb,k_mTb,k_mLa,k_mTa,n_L,n_T,theta_L,theta_T,kp_L,kp_T,gamma_mL,gamma_mT,gamma_pL,gamma_pT]
y0 = [0,0]
t = np.linspace(0,3000,300)

    
def draw_phase_space2 (args):
    k_mLb,k_mTb,k_mLa,k_mTa,n_L,n_T,theta_L,theta_T,kp_L,kp_T,gamma_mL,gamma_mT,gamma_pL,gamma_pT = args
    n=11
    
     
    LacI_vector = np.linspace(0,2000,n)
    TetR_vector = np.linspace(0,2000,n)
    pL_vector, pT_vector = np.meshgrid(LacI_vector, TetR_vector)
    
    
    mRNAl_vector = (k_mLb + (k_mLa / (1 + ((LacI_vector / theta_T)**n_T)))) / gamma_mL
    mRNAt_vector = (k_mTb + (k_mTa / (1 + ((TetR_vector / theta_L)**n_L)))) / gamma_mT

   
    aux1 = [0]*(n**2) 
    aux2 = [0]*(n**2)
    counter = 0
    
    for i in range(n):
        for j in range(n):
            mRNAl, mRNAt, LacI, TetR = toggle_derivative([mRNAl_vector[i],mRNAt_vector[j],LacI_vector[j], TetR_vector[i]], 0,args)
            aux1[counter] = LacI
            aux2[counter] = TetR
            counter += 1 
    
    n_LacI=(kp_L*mRNAl_vector)/gamma_pL
    n_TetR=(kp_T*mRNAt_vector)/gamma_pT
    
    n_LacI_vector = n_LacI
    n_TetR_vector = n_TetR

    
    plt.quiver(pL_vector, pT_vector, aux1, aux2)
    for i in range(n):
        for j in range(n):
            solution = odeint(toggle_derivative,[mRNAl_vector[i],mRNAt_vector[j],LacI_vector[j], TetR_vector[i]], t, args=(rates,))
            plt.plot(solution[:,2],solution[:,3],'gold')
    plt.plot(n_LacI_vector, TetR_vector,'g', label='LacI nullcline')
    plt.plot(LacI_vector, n_TetR_vector,'c', label='TetR nullcline')
    plt.xlabel('LacI')
    plt.ylabel('TetR')
    plt.title('Vector field & LacI and TetR nucllines curves with 11 protein trajectories')
    plt.legend()
    plt.show()
    
draw_phase_space2(rates)
