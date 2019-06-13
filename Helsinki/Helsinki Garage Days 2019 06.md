# [Helsinki Garage Day June 2019](https://wiki.cosmos.esa.int/euclid/index.php/20190603_Helsinki)

## Cosmic rays on Euclid Science
* Simulated cosmic rays are too simplistic (single pixel, constant energy)
* Simulation of fully real CR too computing intensive (width, nuclear reaction...)
* Compute something close enough: i.e with width
* Main source of radiation is sun, with solar flares any now and then
* VIS data taken during Coronal Mass Emission is useless for shape measurement
* VIS data will have holes during the flare
    - How much can we lose?gith
    - Re-schedule to fill them in?
* Gaia has gone into safe mode during CME
    - What about Euclid?late
    
## [Gaia spectroscopic data](https://wiki.cosmos.esa.int/euclid/images/b/bc/Mohr-GD_Helsinki.pdf)
* Use RP/BP bandpasses that include griz bands of DES filters
* Would Gaia pseudo photometry be of sufficient quality and signal/noise for
    - Calibration of DES?
    - Bandpass variation DECam focal plane
* Will test for
    - Evidence of persistence photometric errors
    - Evidence for bandpass variation (!?)
* VIS/NIR/EXT - MER - PHZ/SHE must adopt model that will meet requirements
    - See proposal by Jean Coupon Nice 2018: bandpass variation
    - Is solving for mean wavelenght shift as function of position across focal plan adecuate?
* PHZ/SHE software must adopt the position dependent bandpass model
* Bandpass variations: clearly measured in DECam and likely generic to all EXT
    - VIS, NIR TBC
* SGS coordination/discussion for bandpass tracking from EXT/VIS/NIR throught MER to PHZ/SHE

Comments from people:
* Spectroscopy may be good for stars, but not for galaxies, as they have more variation
* Something about models predicting well variation for stars on a set of CCD

Notes:
* NNPZ has support for filter mean transmission per source

## [Timing of sources in MER catalog](https://wiki.cosmos.esa.int/euclid/images/1/12/BA-XMD_GD_Helsinki_source_timing.pptx)
* Legacy science requires timing information (variability, proper motion of stars)
* Tiling makes attaching time information difficult (up to 16 exposures in a tile)
* Should MER pipeline target this for SC7 or SC8?
* https://euclid.roe.ac.uk/issues/10556
* Need more information for the use cases

## Products for the Science Archive System (SAS)
* Science-oriented user interface
* What fraction of the products stored on the data centers will be pushed to the SAS?
* Data Releases are made from SAS
* The Data Product Description Document should contain all products involved in data processing
    - [PHZ 11](http://euclid.esac.esa.int/dm/dpdd/latest/phzdpd/phzindex.html) (I see more than 11?)
        * I think it is outdated. Need to look for the document.
    - 250 DP in total
* Products pushed to SAS needs more in depth description than what is in the DPDD
* Not being in the SAS != not being available. But it means not being "queriable".
    - *But* not in the SAS = restricted to EC people.
* How should proceed? Considered mandatory:
    - PF output interface products
    - PF calibration products
        * Need to be consistent with the science data
* Comment: Put more, but hide behind a view. Otherwise, analysis can become difficult.
* Comment: Turn around, think what do we want released, and from there get what should go into the SAS
    - Probaly not possible
* Comment: Evolve DPDD, make it more verbose, and push that
    - Mean all data products from the data processingn go to the SAS
    - Good for future scientist, better documentation and disponibility
    - Implies pushing RAW. Good idea?
    - Work load on OU, to clarify the documentation
* Comment: Start from use cases, and grow from there: what data required to satisfy use case
    - Having the raw data does not mean SAS should provide any use case as a service (i.e. do something with pixels)
* Having DSS and SAS isolated is good to keep availability while, i.e, there is a data reprocessing due to a failure
    - Otherwise, users would see availability/performance drop
    
### Action plan
* Agree on selection for SAS promotion
* **Each OU-lead to apply these criteria on their product list and provide product set**
    - Next Garage Day, autumn 2019
* Harmonise/reudce list

* VIS, NIR, EXT and MER to discuss/harmonise their products
    - If they can, otherwise: why are they different, even though they are imaging
    
## [Integration of OU-LE3 into the Science Ground Segment data analysis](https://euclid.roe.ac.uk/projects/ec_sgs_challenges/wiki/Integration_of_LE3_into_SGS)
* SC8 is OU-LE3 integration
* Selection criteria has to be defined together with the science
    - How many selection criteria?
    - Static?
    - They mean parameters for the selection
    - Interactively?
    - Can we have a stable definition of sky patch to distribute across SDCs?
* **What is a blinding module?**
    
## [Weak Lensing selection](https://wiki.cosmos.esa.int/euclid/images/d/d6/Schrabback_gd_wl_sample.pdf)
* Step 2: This galaxy is assigned N to bin X, M to bin Y (PHZ)
* Use the full stack to emulate effects of neighbours and the like
* **PHZ responsability: how noise affects bin selection (TBD together)**
* Pipeline updates *will* be orchestrated

## [Increasing Euclid Sky Coverage.... Zodiacal](https://wiki.cosmos.esa.int/euclid/images/8/81/Ganga.pdf)
* Low latitudes later interesting because compensates CTI
* Best regions first (if it stops working!)
