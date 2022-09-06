# NFRs
NFRs are requirements that do not relate to business functionality. They relate to attributes like reliability, efficiency, and portability.

Non Functional Requirements are architecturally significant requirements because they impact the system architecture. They are properties of a system that sit outside of specific business features or functionality. NFRs are sometimes called constraints. Other times they are called Quality Attributes. Constraints generally change the shape of architecture or design.

> [when the non-functional requirements are done well, you may eliminate 50 to 80 percent of product defects.](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/how-non-functional-requirements-impact-product-development)

Capturing NFRs early is part of a _shift left_ where we surface the non business value needs earlier in the process. Non functional requirements impact the system as a whole and are cross cutting across business features.

------------------

## NFR or Not an NFR
NFRs are defined by architecture or designers and are implemented by the delivery teams. Policies exist to meet organizational needs.

Teams need to be diligent about knowing the difference between an NFR that drives system design and organizational policies or guidelines. NFRs drive changes in system design. Policies tend to change the way people operate or maintain the systems. You can especially see this where NFRs overlap for certain parts of CI/CD like continuous testing.  

| Function or Capability                                  | NFR | Policy or Goal |
| ------------------------------------------------------- | --- | -------------- |
| Automated deployment and smoke test after every build   | ?   | Yes            |
| Services include health check endpoint to verify status | Yes | ?              |
| Support fully automated deployments in all environments | ?   | Yes            |
| Auto restart apps on health check failure               | No  | Yes            |
| Exercise APIs on regular basis to verify health         | No  | Yes            |
| Health check dashboard UI                               | No  | Yes            |
| Distribute SLA goals and metrics on a regular basis     | No  | Yes            |
| Components require a runbook that describes triage      | No  | Yes            |

------------------

Software source metrics and other design-time metrics feel like a grey area. They are part of a group's software development policies. They don't explicitly drive software architecture but can influence it. We only get unit-testable code by writing unit tests and checking coverage. At the same time, test coverage targets, code complexity targets, and other code metrics feel like development best practices and not NFRs. 

| Function or Capability  | NFR | Policy or Goal |
| ----------------------- | --- | -------------- |
| Testable code           | Yes | Yes            |
| 100% unit test coverage | ?   | Yes            |

------------------

# NFR Definitions
This document describes one way of organizing NFRs for consumption by delivery teams. This format is designed to present NFRs _at a glance_. Those requiring more details in their NFRs should choose a different format.

------------------

## References
* [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )
* [Scaled Agile Framework](https://www.scaledagileframework.com/nonfunctional-requirements/) 

------------------

## NFR Taxonomies and Classifications
NFR taxonomies often group related NFRs into _Categories_ or _Qualities_. _Categories_ may have _Sub-categories_ to help with organization. 

There are many different published NFR taxonomies.  The following table links to a few.

| Site                                                                                                                        | Category Type | Individual Category                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )                                                      | Execution     | safety, security and usability                                                                                              |
| [Wikipedia](https://en.wikipedia.org/wiki/Non-functional_requirement )                                                      | Evolution     | testability, maintainability, extensibility and scalability                                                                 |
| | | |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/)                | Operational   | Access/Security, Accessability, Availability, Confidentiality, Efficiency, Integrity, Survivability, Reliability, Usability |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/)                | Revisional    | Maintainability, Modifiability, Flexibility, Scalability, Verifiability                                                     |
| [Modern Requirements](https://www.modernrequirements.com/blogs/pillar/what-are-non-functional-requirements/)                | Transitional  | Portability, Reusability, Interopability, Installability                                                                    |
| | | |
| [Scaled Agile Framework](https://www.scaledagileframework.com/nonfunctional-requirements/)                                  | _Not Grouped_ | Security, reliability, performance, maintainability, scalability, and usability                                             |
| | | |
| [A Guide to NFR types and examples](https://www.boxuk.com/insight/guide-to-non-functional-requirements-types-and-examples/) | _Not Grouped_ | accessibility, accountability, accuracy, adaptability, administrability, affordability, agility, auditability...            |

NFR are organized by category and sub-category.

------------------

## Simple NFR Attributes Template
Some teams create a set of NFRs in a table. Each row in the table is an individual NFR.  Each column is an attribute of the NFR.

This table has 5 columns.  
* There is the category/sub-category.
* The NFR definition and implementation.  
* A method for validationg that the NFR is implemented

We get something like the following when using a tabular definition format.

| Category                              | Sub-Category                      | Requirement Definition     | Possible Implementation (opt)                         | Validation Method                       |
| ------------------------------------- | --------------------------------- | -------------------------- | ----------------------------------------------------- | --------------------------------------- |
| Top-level Categories from a Taxonomy. | One or two word requirements name | Description of requirement | A suggested implementation or organizational standard | How the NFR implementation is validated |


------------------

### Example NFR with _Generic Attributes Template_ - 5 Column short form
The following is a common NFR on most projects. It contains a simple 5 column structure.

| Category        | Sub-Category | Requirement Definition                              | Possible Implementation (opt)                  | Validation Method       |
| --------------- | ------------ | --------------------------------------------------- | ---------------------------------------------- | ----------------------- |
| Evolution | Testing | Code modules must have full unit tests coverage | X Unit for testing and Sonar results coverage | Review coverage results |
| Evolution | Testing | Acceptance criteria must be part of functional tests | BDD tests exist for all positive and negative acceptance criteria | Review as part of pull request |

------------------

## Scaled Agile Framework Aligned (SAFe) Template - 10 column with KPI
SAFe adds metrics to the NFR attributes listed above.  SAFe metrics drive or support Key Performance Indicators (PKIs). We use those metrics to determine project success beyond _the app is up_

SAFe additional attributes are something like:
*  Name of the KPI.
*  The _current_ KPI value 
*  The _target_ KPI vale
*  The _failure_ KPI value below which _its pretty bad_

See the SAFe web site for the meanings of these fields. https://www.scaledagileframework.com/nonfunctional-requirements/
* Labels in *(parenthesis)* are Scaled Agile Framework aligned.

| Category                               | _(Sub-Category)_                  | Requirement Definition     | Possible Implementation                               | Validation Method                       |     | _(Meter)_          | Metric Units _(Scale)_ | Metric _(Target)_       | Metric Failure _(Constraint)_ | Metric _(Current)_   |
| -------------------------------------- | --------------------------------- | -------------------------- | ----------------------------------------------------- | --------------------------------------- | --- | ------------------ | ---------------------- | ----------------------- | ----------------------------- | -------------------- |
| Top Level Categories from a Taxonomy. | One or two word requirements name | Requirement Definition | A suggested implementation or organizational standard | How the NFR implementation is validated |     | Metric calculation | metric value type      | Target value for metric | Failure value for metric      | Current metric value |

------------------

# Identifying NFR Applicability
The Categories group similar or topical NFRs. They don't tell you when the NFRs apply.  Each deployable, management or operational component is impacted by some subset of the NFRs across several categories.  Web HTTP API endpoints often have similar NFRs.  Databases all have a common set of NFRs.  

Backlog items should be defined with the appropriate NFRs. We can categorize components by type and associate various NFRs to each of those component or operational type.  

``` mermaid-js
flowchart TD;

    subgraph subcategory1a[Safety]
        NFR1a1[NFR]
        NFR1a2[NFR]
    end
    subgraph subcategory1b[Security]
        NFR1b1[NFR]
        NFR1b2[NFR]
        NFR1b3[NFR]
    end
    subgraph subcategory2a[Testability]
        NFR2a1[NFR]
        NFR2a2[NFR]
        NFR2a3[NFR]
    end
    subgraph subcategory2b[Lineage]
        NFR2b1[NFR]
        NFR2b2[NFR]
    end

    subgraph category1[Execution]
        subcategory1a
        subcategory1b
    end

    subgraph category2[Evolution]
        subcategory2a
        subcategory2b
    end
    
    subgraph Categories
        category1
        category2
    end
    
    subgraph Deployables[Deliverables]
        DeployableType1[ ]
        DeployableType1b[ ]
        DeployableType2[ ]
        DeployableType2b[ ]
        DeployableType3[ ]
    end

    NFR1a1 --> DeployableType1
    NFR1a2 --> DeployableType2

    NFR1b1 --> DeployableType1
    NFR1b2 --> DeployableType2
    NFR1b3 --> DeployableType2

    NFR2a1 --> DeployableType1
    NFR2a2 --> DeployableType2
    NFR2a3 --> DeployableType3

    NFR2b1 --> DeployableType1
    NFR2b2 --> DeployableType3
```

Ex: All web API endpoints have similar NFRs about metrics, encryption, audit, etc

------------------

# Current NFR list
NFRs have been captured in tab-delimited format [NFRs.tsv](NFRs.tsv)  in the _Generic Template_ format.</br>
They are stored in _Tab Separated_ format _.tsv_ which is previewable on GitHub. Open NFRs.tsv with a CSV/TSV viewer. 

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


