# core/simulation.py
from scipy.integrate import odeint
import numpy as np

def gene_expression_model(y, t, k1, k2):
    # Simple model: y[0]=protein A, y[1]=protein B
    dA_dt = k1 - k2 * y[0]
    dB_dt = k1 * y[0] - k2 * y[1]
    return [dA_dt, dB_dt]

def simulate_expression():
    import matplotlib.pyplot as plt
    t = np.linspace(0, 50, 200)
    y0 = [0, 0]
    params = (0.1, 0.05)
    sol = odeint(gene_expression_model, y0, t, args=params)
    plt.plot(t, sol[:,0], label="Protein A")
    plt.plot(t, sol[:,1], label="Protein B")
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.legend()
    plt.title("Gene Expression Simulation")
    plt.show()
