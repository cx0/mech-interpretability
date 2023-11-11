# mech-interpretability

This repo contains my experiments to better understand the recent advances in mechanistic interpretability research (with an emphasis on characterizing the stability of discovered circuits).

### Exploring length generalization in the context of indirect object identification (IOI) task

Mechanistic interpretability aims to explain how neural networks learn at the circuit level. So far only a handful of circuits with compelling evidence have been discovered in relatively small language models [1,2,3]. It remains unclear whether these circuits (a) persist once formed after training further, and (b) have similar explanatory power in larger models or models with different architecture. A recent case study on reverse engineering the circuit behind indirect object identification (IOI) task has uncovered an interesting circuit with a fairly specialized division of labor [3]. While the authors performed extensive experiments and ablation analyses to validate the specific circuit components (i.e., specialized attention heads), how the model performance varies under different perturbations is underexplored. Here we study the performance on IOI task and its variants in the original GPT-2 small and other models of equivalent size. This analysis makes some progress toward addressing the following open research questions curated by Neel Nanda: 5.34 and 5.35 [4].

