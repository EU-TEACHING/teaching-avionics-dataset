I added the new experiments corresponding to the ROP/JOP branch prediction attack anomaly to this folder.

TODO: I also updated the file ../avionic_traces.docx with the new nomenclature:

* B: BPred attack continuously running on the core (a different one from where the FMS is running)
* C: BPred attack intermittently running on the core (a different one from where the FMS is running)
* D: continuous BPRED attack affecting another application running on the same core as the FMS
* E: continuous BPRED attack within the FMS applicaiton
* E: intermittent BPRED attack within the FMS applicaiton

---

 * xFTx.xx: FMS running standalone on second Cortex A53 core and FFT running standalone on third Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 
 * xFTB.xx: FMS, FTT and continuous bpred attack each running on a different Cortex A53.
 * xFTC.xx: FMS, FTT and intermittent bpred attack (suspending the attack for 15s every 30s) each running on a different Cortex A53.
 * xFTx.Bx: FMS & FTT running on Cortex A53s, while continuous bpred running on Cortext A72
 * xFTx.Cx: FMS & FTT running on Cortex A53s, while intermittent bpred running on Cortext A72

 * xxxx.FT: FMS running standalone on first Cortex A72 core and FFT running standalone on the second Cortex A53 core (should correspond to the results already present in LFBT_LFBL) 
 * xxxB.FT: FMS & FTT running on Cortex A72s, while continuous bpred running on Cortext A53
 * xxxC.FT: FMS & FTT running on Cortex A72s, while intermittent bpred running on Cortext A53

 * xDTx.xx: FMS and bpred attacked process corunning on the same Cortex A53 core
 * xxxx.DT: FMS and bpred attacked process corunning on the same Cortex A72 core

 * xETx.xx: FMS internally affected by continuous bpred attack on a Cortex A53 core
 * xxxx.ET: FMS internally affected by continuous bpred attack on a Cortex A72 core
 * xGTx.xx: FMS internally affected by intermittent bpred attackon a Cortex A53 core
 * xxxx.GT: FMS internally affected by intermittent bpred attackon a Cortex A72 core

