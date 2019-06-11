# [Helsinki EC Meeting 2019](http://www.physics.helsinki.fi/ec2019/pages/schedule.html)

## Day 2

* Side note: is DPDD up to date? Who is responsible?

### S01 OU/SDC: Organization meeting

#### TK2 procedure
* TK2 November 2019
* Demo 30th October
* Procedure will be send 22th July
* TK2 meeting 5-7 November, ESTEC
* Final report 26th November
* **[SDC-CH lead should appoint PHZ presenter for the TK2](https://wiki.cosmos.esa.int/euclid/images/2/25/02_00_TK2_Zacchei_01062019_v1.0.pdf)** (!!)
* Draft docs and presentation should be sent to the project office 4th October (1 month before kick-off)
* Final two weeks before kick-off (22nd October)
* *Show slides on SDC meeting*, also mention there are a bunch of meetings in a row (SC456 Sep, ADASS & Developers Workshop Oct, TK2 Nov)

### S05 OU/SDC: SC456 status meeting
* CCB asyncrhonous
    - **Check CCB pages of PFs that already passed** (!!)
        1. **PF fill first section of the wiki**
        2. Tech coord analyze input
        3. PF fix the issues
    - Classical warning: binaries _not_ prefixed by PHZ_ (I do not think we do prefix all?)
* After CCB
    - Top: Fix failures
    - Next: Secondary test campaign (?)
* Test report documents for TK2
    - **Release notes written by PFs (there are [Word templates](https://euclid.roe.ac.uk/projects/sgsfr-paqa/wiki/Liste_des_documents_PF_(DDL)))**
    - I can try... It is basically a first release, no?
    - Need to check if one for Alexandria, one for Phosphoros... or all together?
* SC telecons evolve in Operation telecons
    - Feedback on the tests
    - Issues
    - SDC & System Status
    - Data Management
    - Test plan for the following 2 weeks
* One point of contact during summer
* SC7 no kick-off, iterative
    - Collocated meetings every 3 months
    - No kick-off, but still something defined for long period of times (i.e. region of the sky)
    
## Day 3

### S14 OU/SDC: SC456 simulation: validation and feedback (session 1/2)

* There is photon noise on the VIS simulation, so where is it?

## Day 4

### S02 OU/SDC: Common tools status
* EDEN becoming similar to a home made distribution rahter than a collection of standard libs
    - Becomes tricky handling dependencies, looking for ways to improve
* Python not typically packaged in RPMs, so they have to do it themselves
* CCB
    - CCB #8: Boost update, remove py.test (pytest instead?)
    - CCB #9: Python decorator module, python lib update
* EDEN 2.1
    - $\alpha$ for the summer (LODEEN, CODEEN)
    - $\beta$ for the developers workshop
    - 2.1 prod beginning of 2020
    - To be adopted by SC7
    
#### EDEN 2.1
* Eden will depend on CONDA
* v4.6
* Intro to Conda/Anaconda/Anaconda cloid
* Procedure:
    - Install miniconda on CVMFS
    - Install custom environment (.yml)
    - Let Conda to handle dependencies
    - All Python libraries from EDEN are in Conda channels
    - All numeric/scientific/C++ libraries from EDEN are available
* gcc will be upgraded to 7.3.0 (as shipped by Anaconda)
* Do not plan to do:
    - Distibute Elements Project with Conda
    - Create an Euclid CONDA channel
    - Integrate external libraries into CONDA
* See [slides](https://euclid.roe.ac.uk/dmsf/files/5541/view) for diagram
* ely: Elements wrapper for yum
* elr: Elements wrapper for rpm
    - [Does Hubert know](https://gitlab.euclid-sgs.uk/fleroux/Elements/commits/conda-5.4)?
* How to contribute
    - Assess impact on C++ code
    - Assess impact on Common Tools
    - Contribute Conda packages
        * Example: 3rd party, as Astromatics Suite (ja!)
* OMG

#### CONDA: Impact on the IAL
* IAL has to source CONDA env, load EDEN environment, and run
    - This probably affects Nicolas' script
* INFRA/EDEN interface?
* Conda Environment maintenance?
* Timetable
    - INFRA 1.1 with EDEN 2.1
    
#### Singularity
* Delivered through CVMFS
- Worker image generated and maintained by the CT team
* CentOS core, with few system libraries (TBC/TBD), CVMFS mounting point to be delivered by the host
* Binding to local data to be mounted at runtime
* Some initiatives: SDC-CH
* Testing: Singularity from singularity for 3rd party software (OMG)
* Version 2.x or 3.x?
    - 3.x mounting points may be created at runtime
* 3rd party container: allows to natively install and deliver TPS (i.e Astormatic)
    - Image to be delivered via CVMS
    - Wrapper scripts in order to make the call transparent, same API (??)

#### For TPS
* i.e. scapm, psfex
* Not packaged by Elements, nor CentOS, but Fedora
* Wrapper script calls Singularity, which contains the tool
* Calling Singularity container with TPS within a worker Singularity image works
    - OMG2

Sidenote: Poke FT from SIM to beta test/use SExtractor++

#### [ML/DL Working Group](https://euclid.roe.ac.uk/dmsf/files/5548/view)
* WG for joining effeorts and foster collaboration
* Comment: The idea is not to put GPU into IAL
    - Training done separately, distributed as a data product (EAS) or CVMFS, and then use IAL nodes with CPU
* Star/galaxy separation proposed as a test case

#### [6th Developer's Workshop](https://euclid.roe.ac.uk/dmsf/files/5550/view)
* 15th - 18th October 2019
* ESA-ESAC (Madrid)
* Program
    - Day 1 & 2: Common Tools and news
    - Day 3: Presentations on SIM (i.e. how to run our own simulations)
    - Day 4: Developer's experience & advanced topics
* [Draft agenda](https://euclid.roe.ac.uk/projects/codeen-users/wiki/DevelopersWorkshop6)
    - Note there is a slot for Sextractor++!! (Day 4)
