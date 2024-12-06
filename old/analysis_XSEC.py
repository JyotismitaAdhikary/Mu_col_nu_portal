import os
import numpy as np
import gzip
import shutil
import pylhe

#from FASERnu_DetectorSim import FASERvDetectorSimulation
#from FASERnu_Xsecs import *

def write_run_card(energy,number,pol):

    f= open("current/Cards/run_card.dat","w")

    f.write("#********************************************************************* \n")
    f.write("#                       MadGraph5_aMC@NLO                            * \n")
    f.write("#                                                                    * \n")
    f.write("#                     run_card.dat MadEvent                          * \n")
    f.write("#                                                                    * \n")
    f.write("#  This file is used to set the parameters of the run.               * \n")
    f.write("#                                                                    * \n")
    f.write("#  Some notation/conventions:                                        * \n")
    f.write("#                                                                    * \n")
    f.write("#   Lines starting with a '# ' are info or comments                  * \n")
    f.write("#                                                                    * \n")
    f.write("#   mind the format:   value    = variable     ! comment             * \n")
    f.write("#                                                                    * \n")
    f.write("#   To display more options, you can type the command:               * \n")
    f.write("#      update full_run_card                                          * \n")
    f.write("#********************************************************************* \n")
    f.write("# \n")
    f.write("#********************************************************************* \n")
    f.write("# Tag name for the run (one word)                                    * \n")
    f.write("#********************************************************************* \n")
    f.write("tag_1     = run_tag ! name of the run \n")
    f.write("#********************************************************************* \n")
    f.write("# Number of events and rnd seed                                      * \n")
    f.write("# Warning: Do not generate more than 1M events in a single run       * \n")
    f.write("#********************************************************************* \n")
    f.write(str(number)+" = nevents ! Number of unweighted events requested \n")
    f.write("0   = iseed   ! rnd seed (0=assigned automatically=default)) \n")
    f.write("#********************************************************************* \n")
    f.write("# Collider type and energy                                           * \n")
    f.write("# lpp: 0=No PDF, 1=proton, -1=antiproton, 2=photon from proton,      * \n")
    f.write("#                                         3=photon from electron     * \n")
    f.write("#********************************************************************* \n")
    f.write("0        = lpp1    ! beam 1 type \n")
    f.write("1        = lpp2    ! beam 2 type \n")
    f.write(str(energy)+"     = ebeam1  ! beam 1 total energy in GeV \n")
    f.write("0.938    = ebeam2  ! beam 2 total energy in GeV \n")
    f.write("#********************************************************************* \n")
    f.write("# Beam polarization from -100 (left-handed) to 100 (right-handed)    * \n")
    f.write("#********************************************************************* \n")
    f.write(str(pol)+"     = polbeam1 ! beam polarization for beam 1 \n")
    f.write("0.0     = polbeam2 ! beam polarization for beam 2 \n")
    f.write("#********************************************************************* \n")
    f.write("# PDF CHOICE: this automatically fixes also alpha_s and its evol.    * \n")
    f.write("#********************************************************************* \n")
    #f.write("nn23lo1    = pdlabel     ! PDF set \n")
    #f.write("230000    = lhaid     ! if pdlabel=lhapdf, this is the lhapdf number \n")
    f.write("lhapdf    = pdlabel     ! PDF set \n")
    f.write("102600    = lhaid     ! if pdlabel=lhapdf, this is the lhapdf number \n")
    f.write("# To see heavy ion options: type update ion_pdf \n")
    f.write("#********************************************************************* \n")
    f.write("# Renormalization and factorization scales                           * \n")
    f.write("#********************************************************************* \n")
    f.write("False = fixed_ren_scale  ! if .true. use fixed ren scale \n")
    f.write("False        = fixed_fac_scale  ! if .true. use fixed fac scale \n")
    f.write("91.188  = scale            ! fixed ren scale \n")
    f.write("91.188  = dsqrt_q2fact1    ! fixed fact scale for pdf1 \n")
    f.write("91.188  = dsqrt_q2fact2    ! fixed fact scale for pdf2 \n")
    f.write("-1 = dynamical_scale_choice ! Choose one of the preselected dynamical choices \n")
    f.write("1.0  = scalefact        ! scale factor for event-by-event scales \n")
    f.write("#********************************************************************* \n")
    f.write("# Type and output format \n")
    f.write("#********************************************************************* \n")
    f.write("False     = gridpack  !True = setting up the grid pack \n")
    f.write("-1.0 = time_of_flight ! threshold (in mm) below which the invariant livetime is not written (-1 means not written) \n")
    f.write("average =  event_norm       ! average/sum. Normalization of the weight in the LHEF \n")
    f.write("# To see MLM/CKKW  merging options: type update MLM or update CKKW \n")
    f.write("#********************************************************************* \n")
    f.write("# \n")
    f.write("#********************************************************************* \n")
    f.write("# handling of the helicities: \n")
    f.write("#  0: sum over all helicities \n")
    f.write("#  1: importance sampling over helicities \n")
    f.write("#********************************************************************* \n")
    f.write("0  = nhel          ! using helicities importance sampling or not. \n")
    f.write("#********************************************************************* \n")
    f.write("# Generation bias, check the wiki page below for more information:   * \n")
    f.write("#  'cp3.irmp.ucl.ac.be/projects/madgraph/wiki/LOEventGenerationBias' * \n")
    f.write("#********************************************************************* \n")
    f.write("None = bias_module  ! Bias type of bias, [None, ptj_bias, -custom_folder-] \n")
    f.write("{} = bias_parameters ! Specifies the parameters of the module. \n")
    f.write("# \n")
    f.write("#******************************* \n")
    f.write("# Parton level cuts definition * \n")
    f.write("#******************************* \n")
    f.write("# \n")
    f.write("# \n")
    f.write("#********************************************************************* \n")
    f.write("# BW cutoff (M+/-bwcutoff*Gamma) ! Define on/off-shell for  and decay \n")
    f.write("#********************************************************************* \n")
    f.write("15.0  = bwcutoff      ! (M+/-bwcutoff*Gamma) \n")
    f.write("#********************************************************************* \n")
    f.write("# Standard Cuts       \n")
    f.write("#********************************************************************* \n")
    f.write("# Minimum and maximum pt's (for max, -1 means no cut)                * \n")
    f.write("#********************************************************************* \n")
    f.write(" 0.0  = ptj       ! minimum pt for the jets \n")
    f.write(" 0.0  = ptl       ! minimum pt for the charged leptons \n")
    f.write("-1.0  = ptjmax    ! maximum pt for the jets \n")
    f.write("-1.0  = ptlmax    ! maximum pt for the charged leptons \n")
    f.write("{}    = pt_min_pdg ! pt cut for other particles (use pdg code). Applied on particle and anti-particle \n")
    f.write("{}    = pt_max_pdg ! pt cut for other particles (syntax e.g. {6: 100, 25: 50}) \n")
    f.write("# \n")
    f.write("# For display option for energy cut in the partonic center of mass frame type 'update ecut' \n")
    f.write("# \n")
    f.write("#********************************************************************* \n")
    f.write("# Maximum and minimum absolute rapidity (for max, -1 means no cut)   * \n")
    f.write("#********************************************************************* \n")
    f.write("-1.   = etaj    ! max rap for the jets \n")
    f.write("-1.   = etal    ! max rap for the charged leptons \n")
    f.write("0.0   = etalmin ! main rap for the charged leptons \n")
    f.write("{}    = eta_min_pdg ! rap cut for other particles (use pdg code). Applied on particle and anti-particle \n")
    f.write("{}    = eta_max_pdg ! rap cut for other particles (syntax e.g. {6: 2.5, 23: 5}) \n")
    f.write("#********************************************************************* \n")
    f.write("# Minimum and maximum DeltaR distance                                * \n")
    f.write("#********************************************************************* \n")
    f.write("0.0   = drjl    ! min distance between jet and lepton \n")
    f.write("-1.0  = drjlmax ! max distance between jet and lepton \n")
    f.write("#********************************************************************* \n")
    f.write("# Minimum and maximum invariant mass for pairs                       * \n")
    f.write("#********************************************************************* \n")
    f.write("{} = mxx_min_pdg ! min invariant mass of a pair of particles X/X~ (e.g. {6:250}) \n")
    f.write("{'default': False} = mxx_only_part_antipart ! if True the invariant mass is applied only \n")
    f.write("! to pairs of particle/antiparticle and not to pairs of the same pdg codes. \n")
    f.write("#********************************************************************* \n")
    f.write("# Inclusive cuts                                                     * \n")
    f.write("#********************************************************************* \n")
    f.write("#********************************************************************* \n")
    f.write("# maximal pdg code for quark to be considered as a light jet         * \n")
    f.write("# (otherwise b cuts are applied)                                     * \n")
    f.write("#********************************************************************* \n")
    f.write("4 = maxjetflavor    ! Maximum jet pdg code \n")
    f.write("#********************************************************************* \n")
    f.write("# \n")
    f.write("#********************************************************************* \n")
    f.write("# Store info for systematics studies                                 * \n")
    f.write("# WARNING: Do not use for interference type of computation           * \n")
    f.write("#********************************************************************* \n")
    f.write("False  = use_syst      ! Enable systematics studies \n")
    f.write("systematics = systematics_program ! none, systematics [python], SysCalc  \n")
    f.write("['--mur=0.5,1,2', '--muf=0.5,1,2', '--pdf=errorset'] = systematics_arguments \n")
    f.write("# Syscalc is deprecated but to see the associate options type'update syscalc' \n")

    f.close()

def write_param_card_mumu(mass):
    f= open("current/Cards/param_card.dat","w")
    
    f.write("###################################################################### \n")
    f.write("## PARAM_CARD AUTOMATICALY GENERATED BY MG5 FOLLOWING UFO MODEL   #### \n")
    f.write("###################################################################### \n")
    f.write("##                                                                  ## \n")
    f.write("##  Width set on Auto will be computed following the information    ## \n")
    f.write("##        present in the decay.py files of the model.               ## \n")
    f.write("##        See  arXiv:1402.1178 for more details.                    ## \n")
    f.write("##                                                                  ## \n")
    f.write("###################################################################### \n")

    f.write("################################### \n")
    f.write("## INFORMATION FOR CKMBLOCK \n")
    f.write("################################### \n")
    f.write("Block ckmblock \n")
    f.write("1 2.277360e-01 # cabi \n")

    f.write("################################### \n")
    f.write("## INFORMATION FOR MASS \n")
    f.write("################################### \n")
    f.write("Block mass \n")
    f.write("5 4.700000e+00 # MB \n")
    f.write("6 1.720000e+02 # MT \n")
    f.write("15 1.777000e+00 # MTA \n")
    f.write("23 9.118760e+01 # MZ \n")
    f.write("25 1.200000e+02 # MH \n")
    f.write("39 "+str(mass)+" # MJs \n")
    f.write("## Dependent parameters, given by model restrictions. \n")
    f.write("## Those values should be edited following the \n")
    f.write("## analytical expression. MG5 ignores those values \n")
    f.write("## but they are important for interfacing the output of MG5 \n")
    f.write("## to external program such as Pythia. \n")
    f.write("1 0.000000e+00 # d : 0.0 \n")
    f.write("2 0.000000e+00 # u : 0.0 \n")
    f.write("3 0.000000e+00 # s : 0.0 \n")
    f.write("4 0.000000e+00 # c : 0.0 \n")
    f.write("11 0.000000e+00 # e- : 0.0 \n")
    f.write("12 0.000000e+00 # ve : 0.0 \n")
    f.write("13 0.000000e+00 # mu- : 0.0 \n")
    f.write("14 0.000000e+00 # vm : 0.0 \n")
    f.write("16 0.000000e+00 # vt : 0.0 \n")
    f.write("21 0.000000e+00 # g : 0.0 \n")
    f.write("22 0.000000e+00 # a : 0.0 \n")
    f.write("24 7.982436e+01 # w+ \n")
    
    f.write("################################### \n")
    f.write("## INFORMATION FOR NEWPHYSICS \n")
    f.write("################################### \n")
    f.write("Block newphysics \n")
    f.write("1 1.000000e+00 # gnu \n")

    f.write("################################### \n")
    f.write("## INFORMATION FOR SMINPUTS \n")
    f.write("################################### \n")
    f.write("Block sminputs \n")
    f.write("1 1.279000e+02 # aEWM1 \n")
    f.write("2 1.166370e-05 # Gf \n")
    f.write("3 1.184000e-01 # aS \n")

    f.write("################################### \n")
    f.write("## INFORMATION FOR YUKAWA \n")
    f.write("################################### \n")
    f.write("Block yukawa \n")
    f.write("5 4.700000e+00 # ymb \n")
    f.write("6 1.720000e+02 # ymt \n")
    f.write("15 1.777000e+00 # ymtau \n")

    f.write("################################### \n")
    f.write("## INFORMATION FOR DECAY \n")
    f.write("################################### \n")
    f.write("DECAY   6 1.508336e+00 # WT \n")
    f.write("DECAY  23 2.495200e+00 # WZ \n")
    f.write("DECAY  24 2.085000e+00 # WW \n")
    f.write(" DECAY  25 5.753088e-03 # WH \n")
    f.write("DECAY  39 1.000000e-01 # WJs \n")
    f.write("## Dependent parameters, given by model restrictions. \n")
    f.write("## Those values should be edited following the \n")
    f.write("## analytical expression. MG5 ignores those values \n")
    f.write("## but they are important for interfacing the output of MG5 \n")
    f.write("## to external program such as Pythia. \n")
    f.write("DECAY  1 0.000000e+00 # d : 0.0 \n")
    f.write("DECAY  2 0.000000e+00 # u : 0.0 \n")
    f.write("DECAY  3 0.000000e+00 # s : 0.0 \n")
    f.write("DECAY  4 0.000000e+00 # c : 0.0 \n")
    f.write("DECAY  5 0.000000e+00 # b : 0.0 \n")
    f.write("DECAY  11 0.000000e+00 # e- : 0.0 \n")
    f.write("DECAY  12 0.000000e+00 # ve : 0.0 \n")
    f.write("DECAY  13 0.000000e+00 # mu- : 0.0 \n")
    f.write("DECAY  14 0.000000e+00 # vm : 0.0 \n")
    f.write("DECAY  15 0.000000e+00 # ta- : 0.0 \n")
    f.write("DECAY  16 0.000000e+00 # vt : 0.0 \n")
    f.write("DECAY  21 0.000000e+00 # g : 0.0 \n")
    f.write("DECAY  22 0.000000e+00 # a : 0.0 \n")
    f.write("#=========================================================== \n")
    f.write("# QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE) \n")
    f.write("#=========================================================== \n")

    f.write("Block QNUMBERS 39  # js \n")
    f.write("1 0  # 3 times electric charge \n")
    f.write("2 1  # number of spin states (2S+1) \n")
    f.write("3 1  # colour rep (1: singlet, 3: triplet, 8: octet) \n")
    f.write("4 0  # Particle/Antiparticle distinction (0=own anti) \n")
    
    f.close()

def get_xs_from_lhe(filename):
    xs=0
    with open(filename) as f:
        for line in f:
            if line == "#": continue
            words = [elt.strip() for elt in line.split( )]
            if len(words) != 6: continue
            if words[1]=="Integrated" and words[2]=="weight"and words[3]=="(pb)": xs=float(words[5])
            #if words[1]=="Cross" and words[2]=="section" and words[3]=="(pb)": xs=float(words[5])
            
    return xs
#def get_xs_from_lhe(filename):
 # with open(filename, 'r') as file:
  #  xu = 0
   # for line in file:
    #    words = [elt.strip() for elt in line.split()]
 #       if len(words) != 6:
  #          continue
  #     if words[1] == "Integrated" and words[2] == "weight" and words[3] == "(pb)":
    #        xu = float(words[5])
     #       if xu != 0:
      #          xs = xu
  #return xs 

########################################################################
###  MAIN LOOP
########################################################################

# Load spectrum and define processes
spectrum = np.loadtxt("MC_-14_3TeV_with_cut")
processes = ["vmp_muj"]
energies = [spec[0] for spec in spectrum]
masses = [0.12589254117941673, 0.5011872336272724, 1]  # Add more masses as needed
number = 1000000

for mass in masses:
    run_index = 1
    for process in processes:
        outputfile = f"results/xs_{process}.txt"
        os.makedirs(os.path.dirname(outputfile), exist_ok=True)

        for energy in energies:
            
            if os.path.isdir("current"):
                #os.system("rm -r current")
               os.system(f"cp -r template_{process} current")

            # create run card and param card
            if process in ["vmp_muj"]:
                pol = "-100"
            write_run_card(energy, number, pol)
            write_param_card_mumu(mass)

            run_dir = f"./current/Events/run_{run_index:02d}"
            os.makedirs(run_dir, exist_ok=True)

            # run MG + read results
            try:
                os.system(f"./current/bin/generate_events -f")
                #lhefilename = f"{run_dir}/unweighted_events_m{mass}_e{energy}.lhe"
                
                xs = get_xs_from_lhe(lhefilename)
            except:
                xs = 0

            
            with open(outputfile, "a") as f:
                f.write(f"{mass} {energy} {xs}\n")

            run_index += 1

    print(f"Completed simulations for mass {mass} GeV.")
