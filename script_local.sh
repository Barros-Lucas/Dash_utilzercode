#!/bin/bash

cd /home/Dash/

cp $1 /home/images/images1.nii 
cp $2 /home/images/images2.nii

mkdir results
cd /home/Dash/results/

exec /utilzreg-code/utilzreg_BUILD/uTIlzReg_Demons /home/images/images1.nii /home/images/images2.nii -Gauss_fluid 8 -iterations 10
