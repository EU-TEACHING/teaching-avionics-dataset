I added the new experiments corresponding to the Spectre speculative attack anomaly to this folder. 


* I: Spectre Continuous running on the core
* J: Spectre Intermittent running on the core
* K: FMS + Spectre continuous running on the same core
* L: FMS + Spectre intermittent running on the same core

---

 * xFTx.xx: FMS running standalone on second Cortex A53 core and FFT running standalone on third Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 
 * xxxx.FT: FMS running standalone on first Cortex A72 core and FFT running standalone on the second Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 

 * xFTI.xx: FMS, FTT and continuous spectre attack each running on a different Cortex A53.
 * xFTJ.xx: FMS, FTT and intermittent spectre attack (suspending the attack for 15s every 30s) each running on a different Cortex A53.

 * xFTx.Ix: FMS & FTT running on Cortex A53s, while continuous spectre running on Cortext A72
 * xFTx.Jx: FMS & FTT running on Cortex A53s, while intermittent spectre running on Cortext A72

 * xxxI.FT: FMS & FTT running on Cortex A72s, while continuous spectre running on Cortext A53
 * xxxJ.FT: FMS & FTT running on Cortex A72s, while intermittent spectre running on Cortext A53

 * xKTx.xx: FMS and Spectre corunning on the same Cortex A53 core
 * xxxx.KT: FMS and Spectre corunning on the same Cortex A72 core
