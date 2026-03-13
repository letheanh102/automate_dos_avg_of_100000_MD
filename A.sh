#!/bin/sh
#QSUB2 queue qM
#QSUB2 core  384
#QSUB2 mpi   48
#QSUB2 smp   2
#QSUB2 wtime 47:57:00
#PBS -N 1x1_1H

. /etc/profile.d/modules.sh

module purge                                                                                                                                                                                             
module load intel
module load intel-mkl
module load intel-mpi
#module load Set/pgi-mpt                                                                                                                                                                                  
#module list                                                                                                                                                                                              
export OMP_NUM_THREADS=2

cd $PBS_O_WORKDIR
VASP=/home/theanh/vasp.5.4.4/bin/vasp_std                                                                                                     
#rm *.e* *.o* I* O* KPOINTS PCDAT REPORT WAVECAR XDATCAR vasprun.xml* C* DOSCAR* E* POSCAR                                                                                                                 
printf "start: $(date)\n" > 0_run

cp POSCAR_origin POSCAR
cp KPOINTS_scf KPOINTS
cp INCAR_scf INCAR

mpijob -mpi 48 -smp 2 $VASP

mv OUTCAR OUTCAR_scf
mv DOSCAR DOSCAR_scf
mv vasprun.xml vasprun.xml_scf

cp INCAR_dos INCAR
cp KPOINTS_dos KPOINTS
mpijob -mpi 48 -smp 2 $VASP

mv INCAR INCAR_dos
mv OUTCAR OUTCAR_dos
mv DOSCAR DOSCAR_dos
mv vasprun.xml vasprun.xml_dos

mkdir dos
cp POSCAR ./dos/
cp vasprun.xml_dos ./dos/vasprun.xml
cd ./dos/
/home/theanh/anaconda3/bin/sumo-dosplot --xmin -6 --xmax 6 --elements C
/home/theanh/anaconda3/bin/sumo-dosplot --xmin -6 --xmax 6 --elements H
/home/theanh/anaconda3/bin/sumo-dosplot --xmin -6 --xmax 6 --elements B
/home/theanh/anaconda3/bin/sumo-dosplot --xmin -6 --xmax 6 --elements O
/home/theanh/anaconda3/bin/sumo-dosplot --xmin -6 --xmax 6 --total-only
cd ../

rm WAVECAR*

printf "end:   $(date)\n" >> 0_run
mv 0_run 0_done
