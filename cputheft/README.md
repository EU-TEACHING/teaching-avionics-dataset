I added the new experiments corresponding to the CPUtheft anomaly to this folder. 

I also updated the file ../avionic_traces.docx with the new nomenclature:


 * xFTx.xx: FMS running standalone on second Cortex A53 core and FFT running standalone on third Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 

 * xUTx.xx: FMS and CPUtheft anomaly running on second Cortex A53 core and FFT running standalone on the third Cortex A53 core. 

 * xxxx.FT: FMS running standalone on first Cortex A72 core and FFT running standalone on the second Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 

 * xxxx.UT: FMS and CPUtheft anomaly running on first Cortex A72 core and FFT running standalone on the second Cortex A72 core. 

 * xFTC.xx: FMS, FTT and Cputheft anomaly each running on a different Cortex A53.


On the Cortex A53 core, the FMS uses 80%-95% of the CPU load, and therefore the slowdown seems to be significant while running together with the CPUtheft anomaly (with a load lowered to 50%) 

On the high-performance Cortex A72 core, the FMS uses 25% of CPU load, and the load seems to remain the same while running with the anomaly. So I don’t expect significant results for this one. 

Running the CPUtheft anomaly on its dedicated core (xFTC.xx)
should have no impact on the FMS behavior.
