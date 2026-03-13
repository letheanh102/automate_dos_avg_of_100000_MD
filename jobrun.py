import re
import os
import time
import math
import glob
from libraries import *
from variables import *
from atreader import *
nat,ntyp=len(geom)-2,len(species)

pre=molname
title=molname
file=pre
filein=file+'.INCAR_scf'

input = open(filein, 'w')
       
input.write('System = bdd111\n')
input.write('ISTART = %s\n' %(istart))
input.write('ICHARG = %s\n' %(icharg))
input.write('PREC   = %s\n' %(prec))
input.write('ALGO   = %s\n' %(algo))
input.write('LMIXTAU = %s \n' %(lmixtau))
input.write('LMAXTAU = %s \n' %(lmaxtau))
input.write('ISMEAR  = %s\n' %(ismear))
input.write('SIGMA   = %s\n' %(sigma))
input.write('NSW     = %s\n' %(nsw))
input.write('NEDOS  = %s\nEMAX = 20\nEMIN = -20\n' %(nedos))
input.write('IBRION  = %s\n' %(ibrion))
input.write('!ISIF    = %s\n' %(isif))
input.write('ISYM    = %s\n' %(isym))
input.write('SYMPREC = %s\n' %(symprec))
input.write('NWRITE  = %s\n' %(nwrite))
input.write('!EDIFFG  = %s\n' %(ediffg))
input.write('EDIFF   = %s\n' %(ediff))
input.write('!LORBIT  = %s\n' %(lorbit))
input.write('ISPIN   = %s\n' %(ispin))
input.write('MAGMOM  = %s\n' %(magmom))
input.write('AMIX    = %s\n' %(amix))
input.write('BMIX    = %s\n' %(bmix))
input.write('AMIX_MAG = %s\n' %(amix_mag))
input.write('BMIX_MAG = %s\n' %(bmix_mag))
input.write('!NELMIN   = %s\n' %(nelmin))
input.write('!POTIM    = %s\n' %(potim))
input.write('!MEGAGGA  = %s\n' %(metagga))
input.write('!LUSE_VDW = %s\n' %(luse_vdw))
input.write('LASPH    = %s\n' %(lasph))
input.write('IVDW     = %s\n' %(ivdw))
input.write('ADDGRID  = %s\n' %(addgrid))
input.write('!BPARAM   = %s\n' %(bparam))
input.write('!KPAR     = %s\n' %(kpar))
input.write('!NPAR     = %s\n' %(npar))
input.write('!NCORE    = %s\n' %(ncore))
input.write('LPLANE   = %s\n' %(lplane))
input.write('LREAL    = %s\n' %(lreal))
input.write('!NELM     = %s\n' %(nelm))
input.write('LWAVE    = %s\n' %(lwave))

input.close()

filein=file+'.INCAR_dos'
input = open(filein, 'w')

input.write('System = bdd111\n')
input.write('ISTART = 1\n')
input.write('ICHARG = 11\n')
input.write('PREC   = %s\n' %(prec))
input.write('ALGO   = %s\n' %(algo))
input.write('LMIXTAU = %s \n' %(lmixtau))
input.write('LMAXTAU = %s \n' %(lmaxtau))
input.write('ISMEAR  = %s\n' %(ismear))
input.write('SIGMA   = %s\n' %(sigma))
input.write('NEDOS   = 4001\nEMAX = 20\nEMIN = -20\n')
input.write('NSW     = %s\n' %(nsw))
input.write('IBRION  = %s\n' %(ibrion))
input.write('!ISIF    = %s\n' %(isif))
input.write('ISYM    = %s\n' %(isym))
input.write('SYMPREC = %s\n' %(symprec))
input.write('NWRITE  = %s\n' %(nwrite))
input.write('!EDIFFG  = %s\n' %(ediffg))
input.write('EDIFF   = %s\n' %(ediff))
input.write('LORBIT  = 11\n')
input.write('ISPIN   = %s\n' %(ispin))
input.write('!MAGMOM  = %s\n' %(magmom))
input.write('AMIX    = %s\n' %(amix))
input.write('BMIX    = %s\n' %(bmix))
input.write('AMIX_MAG = %s\n' %(amix_mag))
input.write('BMIX_MAG = %s\n' %(bmix_mag))
input.write('!NELMIN   = %s\n' %(nelmin))
input.write('!POTIM    = %s\n' %(potim))
input.write('!MEGAGGA  = %s\n' %(metagga))
input.write('!LUSE_VDW = %s\n' %(luse_vdw))
input.write('LASPH    = %s\n' %(lasph))
input.write('IVDW     = %s\n' %(ivdw))
input.write('ADDGRID  = %s\n' %(addgrid))
input.write('!BPARAM   = %s\n' %(bparam))
input.write('!KPAR     = %s\n' %(kpar))
input.write('!NPAR     = %s\n' %(npar))
input.write('!NCORE    = %s\n' %(ncore))
input.write('LPLANE   = %s\n' %(lplane))
input.write('LREAL    = %s\n' %(lreal))
input.write('!NELM     = %s\n' %(nelm))
input.write('LWAVE    = %s\n' %(lwave))

input.close()

geo=open(molname+'.xyz','r').readlines()
filein=file+'.POSCAR'
input= open(filein, 'w')
input.write('bdd\n%s\n%s\n%s\n%s\n' %(scale, a, b, c))
for at in range(0,ntyp):
 input.write(pseudos[re.sub('[0-9]','',species[at])][0]+' ')
input.write('\n')
                                                                                                                                      
for at in range(0,ntyp):
 for at0 in range(2,nat+2):
  if (geo[at0].split()[0] == species[at]):
   count +=1
 input.write('%s ' %(count))
 count = 0
input.write('\n')
input.write('Cartesian\n')
for at in range(0,ntyp):
 for at0 in range(2,nat+2):
  if (geo[at0].split()[0] == species[at]):
   input.write(geo[at0].split()[1]+' '+geo[at0].split()[2]+' '+geo[at0].split()[3]+'\n')

input.close()

print "All done\n"
