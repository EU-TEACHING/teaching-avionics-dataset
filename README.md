# teaching-avionics-datasetavionic_traces.docx

Dataset of traces generated for the avionics use-case. These traces indicate the
behavior of the software critical tasks on the hardware.

## Documentation

Check the folowing files:
 * avionic_traces.docx
 * avionic_traces.pptx
 * TEACHING-D5.3_AI models training dataset_1.0.pdf

## Traces (see avionic_traces.docx)
 * **LFBT_LFBL**: dataset for flightplans between LFBT and LFBL airports, while corunning with the DDoS-L2 anomaly (DDoS to the L2 cache from the other cores)
 * **cputheft**: dataset for flightplans between LFBT and LFBL airports, while corunning with the CPUtheft anomaly (Hi CPU computation load from another application)
 * **speculate**: dataset for flightplans between LFBT and LFBL airports, while corunning with a spectre attack
 * **bpred**: dataset for flightplans between LFBT and LFBL airports, while  corunning with a branch predictor hammering anomaly (Hi level of branch misprediction from other corunning applications and from the FMS applicaition)

## Common file:
 * hw_events_arm64.csv correspond to the list of available hardware events that could be counted on the iMx8 board (see avionic_traces.pptx).

## License

Check the LICENSE file

![BY-NC-SA](by-nc-sa.svg)
