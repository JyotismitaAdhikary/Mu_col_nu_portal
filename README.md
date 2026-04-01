MuCol ν Portal – Simulation Pipeline
This repository contains the simulation and analysis pipeline used to produce results for the neutrino portal dark matter study at a future muon collider. If you use the code cite the paper: https://inspirehep.net/literature/2859407
Overview
The workflow models signal and background processes for a dedicated muon collider neutrino detector (MuColν), focusing on neutrino-induced signatures of dark matter.
Signal generation: done using MadGraph
Background generation: done using PYTHIA8
Signal hadronization & showering: handled with PYTHIA8
Workflow
The pipeline is organized through Jupyter notebooks. To reproduce results, follow them in order:
Background Generation (ipynb 1)
Simulate neutrino-induced background using PYTHIA8
Signal Generation (ipynb 2)
Hadronize signal events produced with MadGraph using PYTHIA8
Create observables for analysis (ipynb 3)
Event Analysis (ipynb 4)
Analyze signal and background observables to select effective cuts 
ML analysis (ipynb 5)
Use BDT to further optimise the cuts

Getting Started
git clone https://github.com/JyotismitaAdhikary/Mu_col_nu_portal.git
cd Mu_col_nu_portal
pip install -r requirements.txt
Then open and run the notebooks in order (1 → 5).

Notes
The pipeline is modular and can be adapted to other BSM scenarios
Designed for reproducibility and fast iteration over physics parameters
