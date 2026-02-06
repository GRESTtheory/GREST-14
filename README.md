[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18500411.svg)](https://doi.org/10.5281/zenodo.18500411)

# GREST v1.2: Gravitational Response of Energy, Space, and Time
### Metric-Response Dynamics & Universal Validation Suite

**Principal Investigator:** John Gresty  
**Official Archive:** [Zenodo Record](https://doi.org/10.5281/zenodo.18500411)  
**License:** Creative Commons Attribution 4.0 / MIT

---

Overview

GREST provides a unified explanation for gravitational anomalies across physical scales without the requirement for Dark Matter. By introducing a universal vacuum acceleration scale (a0 approx 1.2 x 10^-10 m/s2), the framework defines gravity as a "stiffening" metric response in low-acceleration environments.

This repository contains the Official Validation Suite, which tests the GREST formula against 29 distinct astrophysical systems (from Black Holes to Galaxy Clusters), achieving a mean accuracy of 97.4%.

📂 Repository Contents

GREST_Theory_and_Validation.pdf - The full scientific paper detailing the derivation and proofs.

GREST_Universal_Calculator.py - Interactive tool to calculate g_obs from any Newtonian input.

validation_suite.py - Automated script that runs the "Deep Scan" verification against the CSV data.

systems_data.csv - The raw dataset containing observed values for M87*, Andromeda, Bullet Cluster, etc.

GREST_Validation_Results.txt - The official scorecard output.

🚀 Quick Start

To replicate the validation results:

# Run the automated validation
python validation_suite.py
