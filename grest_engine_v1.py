import numpy as np

# HARD-LOCKED CONSTANTS (GREST Engine v1.0)
H0 = 73.0  # km/s/Mpc
C = 299792458.0  # m/s
KM_TO_M = 1000.0
MPC_TO_M = 3.08567758e22
KPC_TO_M = 3.08567758e19

# Derived a0 constant
H0_S = H0 * (KM_TO_M / MPC_TO_M)
A0 = (C * H0_S) / (2 * np.pi) # Result: 1.129e-10 m/s^2

def grest_engine(v_n, r_kpc):
    """
    Core GREST Engine
    v_n: Newtonian velocity in km/s
    r_kpc: Radius in kpc
    """
    r_m = r_kpc * KPC_TO_M
    gn = ((v_n * KM_TO_M)**2) / r_m
    # Governing Formula: gobs = sqrt(gn^2 + gn*a0)
    g_obs = np.sqrt(gn**2 + gn * A0)
    v_pred = np.sqrt(g_obs * r_m) / KM_TO_M
    return v_pred

def binary_boost(sep_kau):
    """External Stellar Validation"""
    G = 6.67430e-11
    M = 2.0 * 1.989e30 # Standard 2-solar mass binary
    r = sep_kau * 1.496e14 
    gn = (G * M) / (r**2)
    boost = np.sqrt(gn**2 + gn * A0) / gn
    return boost

if __name__ == "__main__":
    print(f"--- GREST v1.0 INTERNAL VALIDATION ---")
    print(f"NGC 6503: {grest_engine(79.5, 12.52):.2f} km/s")
    print(f"NGC 7331: {grest_engine(160.0, 12.0):.2f} km/s")
    print(f"DF2: {grest_engine(0.6559, 2.0):.2f} km/s")
    print(f"\n--- GREST v1.0 EXTERNAL VALIDATION ---")
    print(f"20kAU Boost: {binary_boost(20.0):.2f}x")
