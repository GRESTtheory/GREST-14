# GREST-Engine Validation (v1.0)

This repository is the official source of truth for the **GREST Effective Field Law** (v1.0). It contains the master validation script and data used to predict gravitational dynamics across galactic and stellar scales without the use of dark matter parameters.

## Unit-Locked Constants
To ensure reproducibility, all tests use the following fixed values:
* **H0**: 73.0 km/s/Mpc
* **c**: 299,792,458 m/s
* **a0**: 1.129e-10 m/s² (Calculated as (c * H0) / 2π)

## Governing Formula
Observed acceleration ($g_{\mathrm{obs}}$) is derived from Newtonian acceleration ($g_N$):
$$g_{\mathrm{obs}} = \sqrt{g_N^2 + g_N a_0}$$

## Validation Results

### 1. Galactic Scale (RAR)
The Radial Acceleration Relation (RAR) shows the transition from Newtonian gravity to the GREST regime at low accelerations for all galactic systems, including high-mass and low-mass (dark matter deficient) galaxies.

![RAR Validation](./grest_rar_validation.png)

| System | Observed | GREST Predicted | Accuracy | Source |
| :--- | :--- | :--- | :--- | :--- |
| NGC 6503 | 133.0 km/s | 133.28 km/s | 99.79% | McGaugh (2016) |
| NGC 1052-DF2 | 7.9 km/s | 7.40 km/s | 93.66% | van Dokkum (2018) |
| NGC 7331 | 205.0 km/s | 203.81 km/s | 99.42% | McGaugh (2016) |

### 2. Stellar Scale (Wide Binaries)
GREST predicts the gravity boost observed in Gaia DR3 wide binary data beyond 10 kAU.

![Wide Binary Boost](./grest_wide_binary_boost.png)

* **Gaia Wide Binaries**: Predicts a **2.19x** gravity boost at 20 kAU, aligning with reported anomalous excess velocities (Chae, 2023).

## Files
* `grest_engine_v1.py`: The master validation script.
* `GREST_Validation_Final.csv`: Detailed validation data for all 3 galactic systems and stellar boost.
* `references.bib`: BibTeX entries for McGaugh (2016), van Dokkum (2018), and Chae (2023).
* `grest_rar_validation.png`: Visual proof of galactic acceleration.
* `grest_wide_binary_boost.png`: Visual proof of stellar gravity boost.

---

## DOI and Zenodo
The official version of the paper is hosted on Zenodo. You can cite the paper using the DOI below:
**DOI**: [10.5281/zenodo.18484663](https://doi.org/10.5281/zenodo.18484663)

For full access to the source code and data, please visit the [GitHub repository](https://github.com/GRESTtheory/GREST-Engine).

---

## License
This project is licensed under the terms of the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

