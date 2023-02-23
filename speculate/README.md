I added the new experiments corresponding to the Spectre speculative attack anomaly to this folder. 

TODO: I also updated the file ../avionic_traces.docx with the new nomenclature:


 * xFTx.xx: FMS running standalone on second Cortex A53 core and FFT running standalone on third Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 
 * xxxx.FT: FMS running standalone on first Cortex A72 core and FFT running standalone on the second Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 

 * xFTI.xx: FMS, FTT and continuous spectre attack each running on a different Cortex A53.
 * xFTJ.xx: FMS, FTT and intermittent spectre attack (suspending the attack for 15s every 30s) each running on a different Cortex A53.

 * xFTx.Ix: FMS & FTT running on Cortex A53s, while continuous spectre running on Cortext A72
 * xFTx.Jx: FMS & FTT running on Cortex A53s, while intermittent spectre running on Cortext A72
