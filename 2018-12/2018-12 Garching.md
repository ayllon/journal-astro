# 2018 December, 11-13 SC456 and System Team Meeting

* [SC456](https://euclid.roe.ac.uk/projects/ec_sgs_challenges/wiki/2018-12-11_SC456_Meeting_plenary_Garching)
* [System Team](https://euclid.roe.ac.uk/projects/sgsst/wiki/20181212Meeting)

## Tuesday 11

### Challenge coordination

* 04/03/2019 MWE output should be available
* No feedback (validation) from SIR, SPE, PHZ, SHE
* PF code must be frozen and available first of March
* Even though not in the timeline, some validation is expected nevertheless to find bugs and issues

### VIS
* Calibration
    * [CCD Theory](https://www.astro.ufl.edu/~lee/ast325/handouts/ccd.pdf) (Master flat/dark/bias images)
* Spurious sources on the edges on the coadded images
* Ghost masking requirements to be discussed
    * [Ghost images](http://www.stsci.edu/hst/wfpc2/Wfpc2_hand_current/ch5_psf11.html)
    * [Impact of ghosts](https://euclid.roe.ac.uk/attachments/download/15632/EUCL-STRW-TN-8002_v0.1_Impact_of_Ghosts.pdf)

### NIR
* Inconsistencies between simulated sources on NIR and VIS images

### EXT-LSST
* Would need to mix LSST environment to read and Euclid environment to write intermediate files

### MER
* [Pre-release](/euclid-fr/PF-MER/sim/SC456/pre-release-07-12-2018)
* [Some detected objects with no aparent object on the stamp](https://euclid.roe.ac.uk/issues/9127)
* [Location mismatch between VIS and NIR](https://euclid.roe.ac.uk/issues/9083)
* [Galaxies simulated but not in the true universe](https://euclid.roe.ac.uk/issues/9203)
* [Ghost images](https://euclid.roe.ac.uk/issues/9169)
* Waiting feedback from SIR, **PHZ** and SHE

### SHE
* SEDs not from PHZ, but directly from OU-SIM
    * After SC456 they will use PHZ SEDs
* VIS headers on release 3.1 not compatible with Astropy
* SHE (4) running in parallel with **PHZ** (5) for SC456
    * Need to cordinate for LE3 & SC78
* Weak Lensing Sample Selection
    * Main selection by **PHZ** (redshift binning flags)
    * Need to agree on how to pass the selection from PHZ to SHE and LE3

### PHZ
* Need True Universe to build the reference sample and dataset for the training
    * "There will be no 'true universe' for the actual run?"
    * "No, but a reference sample is needed one way or another to run for SC456, for the actual run from spec-z"

## Wednesday 12

### SIM Audit
* Scarcity of manpower
* Too many single-point-of-failure on SIM
* Need to define instrument/artefact model owners
    * SIM is not the best interface between instrument and data processing
* OU's must test their code locally
* SIM need to stabilize code (doc, maintainability)
    * Allow SDC to run simulations

### Master schedule
* Launch 06/2022
* SDC need to update their planning based on the master schedule (?)

### SC Relooking
* *Scientific Challenge*: Pipeline processing functions have been **integrated** together and with the SGS infrastructure
* *Infrastructure Challenge*: Scalability and operability of the SGS comprising all SDCs.
* Challenges will evolve in rehearsal  tests
* Should be incremental, small steps

### Organization
* Stephane point of contact for **OU-PHZ**
* Nikos point of contact for **DEV-PHZ**
* Nicolas point of contact for **SDC-CH**
* See [presentation](https://euclid.roe.ac.uk/attachments/download/15617/SC_organization.pdf) for the telecon/meeting calendar
* PF should be individually validated and integrated
* **Need to fill the [SC456 checklist](https://euclid.roe.ac.uk/projects/ec_sgs_challenges/wiki/SC456_CCB_CheckList)**

### IAL
Pipeline Runner Deployment for Pipeline Developers:

```sh
# Setting up the environment
export PIPELINERUNNER_VERSION="/cvmfs/euclid-dev.in2p3.fr/CentOS7/INFRA/1.0/opt/euclid/ST_PipelineRunner_1.5.7"
export PATH="/cvmfs/euclid-dev.in2p3.fr/CentOS7/INFRA/1.0/usr/bin/:${PATH}"
export PYTHONPATH="${PIPELINERUNNER_VERSION}/lib/python3.6/site-packages:${PYTHONPATH}"
export LODEEN_CONFIG=/cvmfs/euclid-dev.in2p3.fr/CentOS7/INFRA/CONFIG/GENERIC/1.1.17/ppo/lodeen-ial.properties

cd $PIPELINERUNNER_VERSION/bin

# Start the server
./wfm_server.py --config=$LODEEN_CONFIG,/path/to/your/config/file

# Submit a pipeline
./pipeline_runner.py --serverurl=http://localhost:50002 --data=xxx –pipeline=xxx
```

### EDEN
* [Developers' Workshop #6](https://euclid.roe.ac.uk/projects/codeen-users/wiki/DevelopersWorkshop6) at ESAC 14-18 October
* Developers' Workshop #7 (2020) in Edinburgh (SDC-UK)
* [Mailing lists](https://euclid.roe.ac.uk/projects/codeen-users/wiki/MailingLists)
* [How to handle data for unit tests](https://euclid.roe.ac.uk/projects/testdata/wiki/Software_user_guide)
* [Dummy Pipeline](https://euclid.roe.ac.uk/projects/sgssteassau/wiki/DummyPipeline)

## Thursday 13 (System Team)

### Legacy Code Status
* [3rd Party Software](https://euclid.roe.ac.uk/projects/ct_third_party/wiki/Third_Party_Software)
