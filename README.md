NFRs have been captured in tab delimited format [NFRs.tsv](NFRs.tsv)  </br>
They are stored in _Tab Separated_ format _.tsv_ which is previewable on github

# NFRs
Non Functional Requirements are architecturally significant requrements because they impact the system architecture.  Non functional requirements impact the system as a whole and are cross cutting across business features.

------------------

# NFR Definitions
This document describes one way of specifying NFRs for consumption by delivery teams. 
This format is designed to present NFRs _at a glance_
Those requiring more details in their NFRs should choose a different format.

## References
* [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )
* [Scaled Agile Framework](https://www.scaledagileframework.com/nonfunctional-requirements/) 

## Various NFR Category Taxonomies
NFRs are often grouped with related NFRs into _Categories_.  There are many different published NFR categories and Category Type aggeregationsrs.  The links below show some Categories that are grouped under described Category Types

| Site                                                                                                         | Category Type | Individual Category                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )                                       | Execution     | safety, security and usability                                                                                              |
| [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )                                       | Evolution     | testability, maintainability, extensibility and scalability                                                                 |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/) | Operational   | Access/Security, Accessability, Availability, Confidentiality, Efficiency, Integrity, Survivability, Reliability, Usability |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/) | Revisional    | Maintainability, Modifiability, Flexibility, Scalability, Verifiability                                                     |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/) | Transitional  | Portability, Reusability, Interopability, Installability                                                                    |
| [Scaled Agile Framework](https://www.scaledagileframework.com/nonfunctional-requirements/)                   | _Not Grouped_ | Security, reliability, performance, maintainability, scalability, and usability                                             |

I couldn't find many Sub-Category examples so there ones in the sample below are ad-hoc following no model.
## Generic NFR Attributes Template

| Category                              | Sub-Category                      | Requirement Definition     | Possible Implementation (opt)                         | Validation Method                       |
| ------------------------------------- | --------------------------------- | -------------------------- | ----------------------------------------------------- | --------------------------------------- |
| Top Level Categories from a Taxonomy. | One or two word requirements name | Describing the requirement | A suggested implementation or organizational standard | How the NFR implementation is validated |

## Scaled Agile Framework Aligned (SAFe) Template
See the SAFe web site for the meanings of these fields. https://www.scaledagileframework.com/nonfunctional-requirements/
* Labels in *(parenthesis)* are Scaled Agile Framework aligned.

| Category                               | _(Sub-Category)_                  | Requirement Definition     | Possible Implementation                               | Validation Method                       |     | _(Meter)_          | Metric Units _(Scale)_ | Metric _(Target)_       | Metric Failure _(Constraint)_ | Metric _(Current)_   |
| -------------------------------------- | --------------------------------- | -------------------------- | ----------------------------------------------------- | --------------------------------------- | --- | ------------------ | ---------------------- | ----------------------- | ----------------------------- | -------------------- |
| Top Level Categories from a  Taxonomy. | One or two word requirements name | Describing the requirement | A suggested implementation or organizational standard | How the NFR implementation is validated |     | Metric calculation | metric value type      | Target value for metric | Failure value for metric      | Current metric value |

  
------------------

# Example NFRs
You can find a sample list of NFRs in the _Generic Template_ format in a TSV file in this repository. 
Open NFRs.tsv with a CSV/TSV viewer. 

[NFRs.tsv](NFRs.tsv)

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


