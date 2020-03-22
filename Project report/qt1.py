dmLdt = k_mLb + k_mLa * 1/(1+((pT/theta_T)**n_T)) - gamma_mL * mL 
    
dpLdt = k_pL * mL - gamma_pL * pL
    
dmTdt = k_mTb + k_mTa * 1/(1+((pL/theta_L)**n_L)) - gamma_mT * mT
    
dpTdt = k_pT * mT - gamma_pT * pT