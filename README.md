# MuCol ν Portal – Simulation Pipeline

This repository contains the simulation and analysis pipeline used to produce results for the neutrino portal dark matter study at a future muon collider.

📄 If you use this code, please cite the paper:  
https://inspirehep.net/literature/2859407

---

## Overview

The workflow models signal and background processes for a dedicated muon collider neutrino detector (MuColν), focusing on neutrino-induced signatures of dark matter.

- **Signal generation:** MadGraph  
- **Background generation:** PYTHIA8  
- **Signal hadronization & showering:** PYTHIA8  

---

## Workflow

The pipeline is organized through Jupyter notebooks. To reproduce results, follow them in order:

1. **Background Generation (ipynb 1)**  
   Simulate neutrino-induced background using PYTHIA8  
   ➤ To include **displaced μ⁺ background events from meson decays**, rerun this step with the updated configuration  

2. **Signal Generation (ipynb 2)**  
   Hadronize signal events produced with MadGraph using PYTHIA8  

3. **Create Observables ( ipynb 3)**  
   Generate physics observables for analysis  
   ➤ This file has been **updated (new)**  

4. **Event Analysis (ipynb 4)**  
   Analyze signal and background observables to determine effective cuts  
   ➤ This notebook has been **updated (new)**  

5. **ML Analysis (ipynb 5)**  
   Use Boosted Decision Trees (BDT) to further optimize the cuts  

---

## Getting Started

```bash
git clone https://github.com/JyotismitaAdhikary/Mu_col_nu_portal.git
cd Mu_col_nu_portal
pip install -r requirements.txt
