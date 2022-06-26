# NFRs
Non Functional Requirements are architecturally significant requrements because they impact the system architecture. They are properties of a system that sit outside of specific business features or functionality. NFRs are sometimes called _constraints_.  Other times they are called _Quality Attributes_. These constraints do change the shape of an architecture or design.  

NFRs are requirements that do not related to business functionality.  The relate to attributes like reliability, efficiencey, portability. 
> [when the non-functional requirements are done well, you may eliminate 50 to 80 percent of product defects.](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/how-non-functional-requirements-impact-product-development)

Capturing NFRs early is part of a _shift left_ where we surface the non business value needs earlier in the process. Non functional requirements impact the system as a whole and are cross cutting across business features.

------------------

# NFR Definitions
This document describes one way of organizing NFRs for consumption by delivery teams. This format is designed to present NFRs _at a glance_. Those requiring more details in their NFRs should choose a different format.

## References
* [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )
* [Scaled Agile Framework](https://www.scaledagileframework.com/nonfunctional-requirements/) 

## Various NFR Category Taxonomies
NFR taxonomies often group related NFRs into _Categories_ or _Qualities_. _Categories_ may have _Sub-categories_ to help with organization. There are many different published NFR taxonomies.  The folloing table links to a few.

| Site                                                                                                                        | Category Type | Individual Category                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )                                                      | Execution     | safety, security and usability                                                                                              |
| [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )                                                      | Evolution     | testability, maintainability, extensibility and scalability                                                                 |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/)                | Operational   | Access/Security, Accessability, Availability, Confidentiality, Efficiency, Integrity, Survivability, Reliability, Usability |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/)                | Revisional    | Maintainability, Modifiability, Flexibility, Scalability, Verifiability                                                     |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/)                | Transitional  | Portability, Reusability, Interopability, Installability                                                                    |
| [Scaled Agile Framework](https://www.scaledagileframework.com/nonfunctional-requirements/)                                  | _Not Grouped_ | Security, reliability, performance, maintainability, scalability, and usability                                             |
| [A Guide to NFR types and examples](https://www.boxuk.com/insight/guide-to-non-functional-requirements-types-and-examples/) | _Not Grouped_ | accessibility, accountability, accuracy, adaptability, administrability, affordability, agility, auditability...            |

I couldn't find many Sub-Category examples so sub-cateogries in the sample below are ad-hoc, locally home grown.
## Generic NFR Attributes Template
Some teams create a set of NFRs in a table. Each row in the table is an individaul NFR.  Each column is an attribute of the NFR.

This table has 5 columns.  There is the category/sub-category. The definition and implementation.  The validation method.

| Category                              | Sub-Category                      | Requirement Definition     | Possible Implementation (opt)                         | Validation Method                       |
| ------------------------------------- | --------------------------------- | -------------------------- | ----------------------------------------------------- | --------------------------------------- |
| Top Level Categories from a Taxonomy. | One or two word requirements name | Description of requirement | A suggested implementation or organizational standard | How the NFR implementation is validated |

### Example NFR with _Generic Attributes Template_
The folling is a common NFR on most projects.  It contains the simple 5 column structure.

| Category        | Sub-Category | Requirement Definition                              | Possible Implementation (opt)                  | Validation Method       |
| --------------- | ------------ | --------------------------------------------------- | ---------------------------------------------- | ----------------------- |
| Maintainability | Unit Testing | All code modules must have full unit tests coverage | X Unit for testing and Sonar results converage | Review coverage results |

## Scaled Agile Framework Aligned (SAFe) Template
SAFe adds metrics to an NFR attributes listed above.  SAFe metrics drive or support Key Performance Indicators (PKIs). We use those metrics to determine project success beyond _the app is up_

SAFe additional attributes are something like:
*  Name of the KPI.
*  The _current_ KPI value 
*  The _target_ KPI vale
*  The _failure_ KPI value below which _its pretty bad_

See the SAFe web site for the meanings of these fields. https://www.scaledagileframework.com/nonfunctional-requirements/
* Labels in *(parenthesis)* are Scaled Agile Framework aligned.

| Category                               | _(Sub-Category)_                  | Requirement Definition     | Possible Implementation                               | Validation Method                       |     | _(Meter)_          | Metric Units _(Scale)_ | Metric _(Target)_       | Metric Failure _(Constraint)_ | Metric _(Current)_   |
| -------------------------------------- | --------------------------------- | -------------------------- | ----------------------------------------------------- | --------------------------------------- | --- | ------------------ | ---------------------- | ----------------------- | ----------------------------- | -------------------- |
| Top Level Categories from a  Taxonomy. | One or two word requirements name | Describing the requirement | A suggested implementation or organizational standard | How the NFR implementation is validated |     | Metric calculation | metric value type      | Target value for metric | Failure value for metric      | Current metric value |

  
------------------

# Current NFR list
NFRs have been captured in tab delimited format [NFRs.tsv](NFRs.tsv)  in the _Generic Template_ format.</br>
They are stored in _Tab Separated_ format _.tsv_ which is previewable on github. Open NFRs.tsv with a CSV/TSV viewer. 

You can find a sample list of NFRs in the _Generic Template_ format in a TSV file in this repository. 
> [NFRs.tsv](NFRs.tsv)

## Edit TSV with Excel
This just works
## Edit TSV files with Visual Code
I use the VSCode Extension _Excel Viewer_ by _GrapeCity_.
1. Select `NFRs.tsv`
2. Right mouse
3. Select `Open With ...`
4. Enter `CSV`
5. Select `CSV Editor`

## View formatted TSV files in Visual Code
I use the VSCode Extension _Excel Viewer_ by _GrapeCity_.
1. Select `NFRs.tsv`
2. Right mouse
3. Select `Open Preview`


