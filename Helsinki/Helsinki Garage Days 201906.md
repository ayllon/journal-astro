# [Helsinki Garage Day June 2019](https://wiki.cosmos.esa.int/euclid/index.php/20190603_Helsinki)

AA

[PHZ PF Roadmap and progress](https://euclid.roe.ac.uk/projects/ec_sgs_challenges/wiki/PHZ_PF_Roadmap_and_progress)

## OU-PHZ

### Weak Lensing sample selection and calibration (!!!)
Sample selection, what sources to save on the 
We need to know the selection

"""
On doit mesurer le redshift moyene dans le cell. On a besoin savoir les objects dedans.

MER nous donne photometries, SHE les formes

MER+SHE => Quels objects, PHZ post-filtering. Apres, ils vont dans la SOM. SHE avec weight.
Si lobject napartiene pas au sample => weight 0 (depuis SHE)

PHZ (nous) faisons la dernier selection. Une fois que lobject est dans la SOM, il reste la.

Actualement on ne fait pas de poids. MER nous donnes touts les objects.
Si object masqué (i.e. next to star), on jette.

MER da f_j (vector)
SHE da w_j
PHZ saca C_j (celda SOM), epsilon_j si lobject fait partie ou pas.

epsilon_j = function de f_j, w_j, flags, y lo que venga de PHZ...)

SHE must finished before we start.

Si preselección *after SOM*, calibration breaks. Can **not** remove objects form the SOM.

Can we get rid of SOM cells? Probably not.

We provide mean Z per cell.

We need the definition of photometric bin.

A Bin can, and probably will be, several cells from the SOM (see picture).

How do we define bins? In each run, the trained SOM will be different, with different objects in different cells.
We need an algorithm.


1. Calibration depends on weights from SHE. If they change, we need to re-run. Can not preselect.

2. We define bins from the SOM like the image. We count on Weak Lensing people to tell us 
how to bin the cells.

Preselection: i.e. VIS > 24.5 (I guess?)

Picture is the most important!!
Pour calibrer il faut savoir les poids des objects pour calibrer.

Correction picture: epsilon as weight on the sum.

### Gaia spectroscopic data
How useful to provide star color
Need to read summary Gaia!!

High accuracy requirements SED on VIS. What's the resolution we can get, and is it good?
Gaia as reference sample? Lacks infrarouge.

### Data products for science archive

* Calibration
    - Reference Sample + Photometries
    - Bias SOM Model
    - Mean SpecZ Bias Map
  
* [Production](https://gitlab.euclid-sgs.uk/PF-PHZ/PHZ_IAL_Pipelines/blob/develop/PHZ_Production_Pipeline/PipScript_PHZ_Production/PF_PHZ_Production.py)
    - PHZ Catalog
    - Coadded PDZ Bias Map
    - Star SED's

"""
How do we store the PDZ? Sampling?
Legacy science takes place.

We want to store:
* PDZ, full or sampling? Neighbours?
* Star SED(observed SED, not rest frame) (used for PSF)
    - Grid + index per ax (i.e. SED, redenning)
    - If not possible, what do we do? Sampling? Resolution?
* Galaxy SED too
    - How NNPZ does it?
* 100 points per SED
* Both SEDs size will be a fraction of PDZ
* SOM cell (1 per object)
* PDZ stacked dans la SOM (11k * 600 bins)
