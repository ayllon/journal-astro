# 🗓️ [Agenda](https://euclid.roe.ac.uk/projects/sgs_sys_admin/wiki/Infrastructure_Workshop_September_2018)

## 📄 Should do
1. Play with this dummy pipeline, getting a PPO and running on SDC-CH. May need to ask iNicolas.
2. Ask for some explanation about pilot jobs, and how do they relate to the actual running.
3. Have a look at COORS.
4. Have a look at what DSS more precisely does.

## 2018-09-12

### 🎎 [Dummy pipeline](https://euclid.roe.ac.uk/projects/sgssteassau/wiki/DummyPipeline)
JSON configuration file to generate 'dummy' jobs that mimic memory consumption and CPU
wall time of real scientific jobs.
Makes sense, because infra can't run as of today the actual jobs, but they need to see
how would they work.

### IAL
Something about installation and bootstrap script and the like.
Check the [slides](https://euclid.roe.ac.uk/attachments/download/14679/IAL_status_update_sep18.pptx) and
have a look at the documentation for the summary (double check with Nicolas?).

Retry policies are yielding an interesting discussion. For instance, on case of failure,
it may be nice to keep input files, or even some of the intermediate ones, as
it can save time when retrying those parts of the pipeline that failed (feedback from
SHEAR, if I understood).

Problematic, on the other hand, when files already exist (retries), software
may fail to run (i.e astropy will refuse to overwrite an existing file, comment
from Nikos).

Payload job statistics are nice.

Lot of discussion about modifying input files. It has been stated several times that computer says **no**. Besides, each stage should not make asumptions about there is
this file coming from, etc. Should stick to the dataflow concept.

Anyway, I don't *think* this is relevant for SDC-CH.

(This should have ended at 10:40 and it's 13:12).

### 💰 SC456 processing budget
Wrong numbers for CH, apparently yet again, even though Nicolas had updated the
wiki.

### 📆 SC456 schedule
* EXT observations delivered by SIM end of august
* NIP observations delivered
* VIS and NISP-S simulation issues

### 🛠️ Common Tools Status
* Extra libs for SC456 (I guess the specific ones are on the wiki)
* Issue with Scamp, Swarp and Asterism
* Upgrade of EuclidEnv (cvmfs and python3 path issues)

### COORS
Check what is it 🤔

### ⚙ Operations during SC456
For the centralisation of the PF logs the IAL could say where to look.
Centralisation on Kibana, as those logs are removed after the run.

DSS logs should be linked with the PPO ID.

### SC456 system overview
Field 277, nobs 7,... check exact details on the presentation.

PHZ-Cal mentioned to be run locally at UNIGE (done).

## 2018-09-13

### 🖭 EAS-DSS tape
Tape interaction would not work with the Swiss
supercomputer, which is where we (?) are considering to store the data
on tape .
Nikos said files have to be flagged somehow whether to go or not
straight to tape. Some intermediate files are to be accessed immediately,
and they should not go into tape when generated.

* What data goes into tape? i.e. what data is not to be accessed often?

Suggestions that the files going into tape can be automated, and then flagged
as offline, and bringing online - he - should involve a human 👩.

### ☁️ Data for pipeline in memory?
Really, requirement from SHE to be able to use a local temporary storage for
their pipeline, as parallel tasks access for read/write the same set of 
files. They are a lot of files, and the I/O at the parallelism level they use
bring shared storage to their knees.

(This is what triggers the question about pilot jobs and what do they do, and
why do they make use of temp storage easier).

Not all clusters will necessarily be able to provide a local filesystem
for temporary access.
Could be handled as another resource (as CPU or RAM).
Need SDC to provide their possibilities so a baseline can be established.

### 🌲 EDEN environment selection
**Singularity** container based solution mentioned. Images could be in
CVMFS 🛳️.

### 📏 Scaling the IAL DRM
Review IAL architecture.

Handling multiple queues, with different priorities. For instance,
high priority for small jobs with short wall time ⏱️.

### 🐙 CVMFS for distributing data files
Easier to scale for read-only data files that are systematically required
by PF.

Create a stratum0 on top of DSS?

### 📏 Running at scale SHE
(IAL-WFM)

### 💼 AOB
[SDC-CH](https://euclid.roe.ac.uk/projects/sgs_sys_admin/wiki/SDC-CH) page
on the SGS System Administration wiki is empty.
Asked to fill these pages ✏.


