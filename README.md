# EBM and JEM

## EBM (Energy-Based Model)
Basic Assumption: Higher the energy, lower the probability.
![EBM_principle.png](EBM_principle.png)

## JEM (Joint Energy-Based Model)
![JEM_obj.PNG](JEM_obj.PNG)

Generated samples are used to estimate the partition function.

Final Example: 
![conditional_samples.png](conditional_samples.png)

## Training Strategies for Stability
### Contrastive Divergence Loss
![cd_loss.png](cd_loss.png)

### Reservoir Sampling - SGLD : 
```MCMCSampler.synthesize_samples()```: 
    perform SGLD sampling for a given number of steps, and return the final samples. Set up different replay buffers for conditional and unconditional sampling.

The sampling process is shown below: _class label=7_
![sampling_process.PNG](sampling_process.PNG)
## Out-of-Distribution (OOD) Detection
![histogram.png](histogram.png)

JEM can be used as a binary classifier: 

_0_: in-distribution (**ID**): all blue bars

_1_: out-of-distribution (**OOD**): all orange bars

after setting the threshold (**0.25**), we can use it to detect OOD.

Corresponding ROC score : **0.9153815771938624**

