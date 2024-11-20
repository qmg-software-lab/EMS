available text for metadata and documentation development (drafting)


# Patient Transport Explorer 
Python Module 

> ## Clinical Data Mapping to EMS Cluster
>
> #### Pre-conditions
>  1. Hospital EMR has patient information in the system
>  2. Physician Clears Patient for discharge
>  3. Transport provider is contacted and minimum required patient data is shared with the
>  4. transport provider (name, gender, date of birth, MRN)
>  5. The pickup time is arranged
>  6. Transport patient care record is ready to retrieve information and both the EMR and
>  patient care record have an established XD* infrastructure.
> 
> #### Main Flow
> 1. Transport teams arrives at the pick-up location and queries the patient information from
> the Hospital EMR to populate the patient care record system.
> 2. Transport team receives nurse report and transfer of care
> Patient contact is made and transport is started
> 
> #### Post-conditions
> 1. Patient information is updated in the patient care record system during transport.
> 3. Patient is transferred to the care of the drop-off facility staff.
>
> ###
> ## Terminology Resources
>   - https://terminology.hl7.org/1.0.0/CodeSystem-conceptdomains.html
> ###
>
> 
# Sample RIPT

This folder should be used to hold sample RIPT documents.

## IHE RIPT specification

- Current [Routine Interfacility Patient Transport (RIPT)](https://www.ihe.net//uploadedFiles/Documents/PCC/IHE_PCC_Suppl_RIPT.pdf) - Published 2017-09-08 Note: An updated revision (2.0) has been published for public comment as of 2021-01-12
- [draft publication of next generation RIPT](http://build.fhir.org/ig/IHE/PCC.RIPT/branches/master/index.html)
  - [Soure for the IG](https://github.com/IHE/PCC.RIPT)
