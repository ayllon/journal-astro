* FD, PD, NA, SP, AA

* We need two data sets:
    1. For training the classification
    2. For the reference sample (Phosphoros => Ref. Sample => SOM).
* Steps
    1. Add incertainties to the catalog (no photon noise)
    2. Spec-Z sample
    3. Which objects for ref sample
    4. Which objects for the classification training
    5. Parameters for Phosphoros Grid
    6. Run pipeline
* EBV values look too big (it is our galaxy extintion)
    * Is intrinsic extintion? SP thinks not (how does it come these things are not written down?)
    * Column AV is generally extintion in the V band, which should be ~3x EBV
    * Likely EBV is the intrinsic, because otherwise it would not match
* $25{deg}^2$ as ref sample? (SPV-GAL-v8.1)
    * All of them?
    * First, need to cut for the right depth: 24.5 VIS
        * What about other bands? No, for weak lensing only VIS relevant
    * If after first cut too many (i.e $\ge 500K$), random cut for NNPZ
    * 2k objects used for Redshift Zero Point correction
    * Check PhotoZ vs SpecZ (plots, concentration)
    * Plot distribution in each SOM cell (check
* Should we run the classification, or can we skip?
    * We can ignore for building the ref. sample, but not for the run
    * Can just use the flag from MER (why is this not enough?)
    * Stars and galaxies are simulated on different sky locations, so can't train directly
      or basically using E(B-V) to tell them apart
* [AB magnitude](https://en.wikipedia.org/wiki/AB_magnitude)

$
m_0^{band} \Longrightarrow^{zero point} f_0^{band} \rightarrow \begin{cases}
    \sigma_0^{band,wide} = f_0^{band} / 10 \\
    \sigma_0^{band,ref} = f_0^{band} / 50
\end{cases}
$
