#!/bin/bash
#PBS -l nodes=4:ppn=16:gpus=2
#PBS -l walltime=48:00:00
#PBS -e "$PBS_JOBID".err
#PBS -o "$PBS_JOBID".out
echo "PBS job id is $PBS_JOBID"
echo "PBS nodefile is at $PBS_NODEFILE"
NPROCS=$(wc -l < "$PBS_NODEFILE")
echo "NPROCS is $NPROCS"
cat "$PBS_NODEFILE" > nodes
mpirun -machinefile "$PBS_NODEFILE" -np "$NPROCS" model.py 
