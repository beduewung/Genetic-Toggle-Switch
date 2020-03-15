from matplotlib import pyplot as plt
from flask import Flask, render_template, request
from flask_cors import CORS
import json

class Simulation():

    def __init__(self, h, arguments):
        self.k_mLb = 0.0082
        self.k_mTb = 0.0082
        self.k_mLa = 1
        self.k_mTa = 1
        self.theta_L = 600
        self.theta_T = 600
        self.n_L = 4.0
        self.n_T = 4.0
        self.gamma_mL = 0.04
        self.gamma_mT = 0.04
        self.k_pT = 0.1
        self.k_pL = 0.1
        self.gamma_pL = 0.002
        self.gamma_pT = 0.002
        self.IPTG = False
        self.IPTS = False

        self.mL, self.mT, self.pL, self.pT = arguments
        self.original_args = arguments
        self.h = h

        self._gamma_pL = self.gamma_pL
        self._gamma_pT = self.gamma_pT
        self._gamma_pL = self.gamma_pL
        self._gamma_pT = self.gamma_pT

    def toggle_derivative(self):
        print("derivative", self.IPTG, self.IPTS)
        if self.IPTG == "true":
            print('in')
            # self.gamma_pL = 0.8
            self.pL = .1
        # else:
        #     self.gamma_pL = self._gamma_pL

        if self.IPTS == "true":
            print('in2')
            # self.gamma_pT = 0.8
            self.pT = .1
        # else:
        #     self.gamma_pT = self._gamma_pT
        

        
        dmLdt = self.k_mLb + self.k_mLa * 1/(1+((self.pT/self.theta_T)**self.n_T)) - self.gamma_mL * self.mL 
        
        dpLdt = self.k_pL * self.mL - self.gamma_pL * self.pL
        
        dmTdt = self.k_mTb + self.k_mTa * 1/(1+((self.pL/self.theta_L)**self.n_L)) - self.gamma_mT * self.mT
        
        dpTdt = self.k_pT * self.mT - self.gamma_pT * self.pT
        
        return [dmLdt, dmTdt, dpLdt, dpTdt]
    
    def nextStep(self):
        res = self.toggle_derivative()
        y = [self.mL, self.mT, self.pL, self.pT]
        self.mL, self.mT, self.pL, self.pT = [y[i] + h * res[i] for i in range(len(res))]
    
    def reset(self):
        self.mL, self.mT, self.pL, self.pT = self.original_args
        
    def euler(self, x0, y, x ): 
        traj_mL = []
        traj_mT = []
        traj_pL = []
        traj_pT = []

        x = 3000
        while x0 < x: 
            step = self.nextStep()
            traj_mL.append(self.mL)
            traj_mT.append(self.mT)
            traj_pL.append(self.pL)
            traj_pT.append(self.pT)
            x0 = x0 + self.h 

        return traj_mL, traj_mT, traj_pL, traj_pT
      
# Initial Values 
x0 = 0
arguments = [0, 0, 0, 0]
h = 10
x = 3000

sim = Simulation(h, arguments)





app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    sim.reset()
    return render_template('index.html')

@app.route('/get_data')
def send_data():
    sim.IPTG = request.args.get('iptg')
    sim.IPTS = request.args.get('ipts')
    sim.nextStep()
    return json.dumps({"mL" : sim.mL, "mT" : sim.mT, "pL" : sim.pL, "pT" : sim.pT})

if __name__ == '__main__':
    app.run(debug=True)

  
# results = sim.euler(x0, arguments, x)

# plt.plot(results[0])
# plt.plot(results[1])
# plt.plot(results[2])
# plt.plot(results[3])
# plt.show() 

