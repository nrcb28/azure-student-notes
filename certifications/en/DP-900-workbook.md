# DP-900 · Common advanced workbook

[Guide](DP-900.md) · [Ten cases](DP-900-cases.md) · [Contents](README.md)

Five matching units across eight languages. Use synthetic data and document predictions separately from observations. These exercises do not deploy Azure and do not establish full exam coverage.

<a id="dp-900-unit-1"></a>

## 1. Describe data before selecting its store

Inventory a PDF, an enrolment row, an optional-metadata JSON document, and a download event. For each, describe its structure, identifier, producer, consumer, retention, and sensitive fields. Then write the operation that matters: retrieve a file, record an enrolment, or aggregate events. Distinguish a format choice from a workload requirement.

**Scenario:** somebody proposes one database because all four datasets belong to the same app. **Evidence:** a four-row decision matrix, one rejected alternative for each row, and a statement of what new requirement could change the choice. Do not invent service limits or assume every JSON document requires Cosmos DB.

<a id="dp-900-unit-2"></a>

## 2. Make relational integrity visible

Draw Students, Courses, and Enrolments with stable identifiers. Create six synthetic rows and explain primary keys, references, and a rule that prevents duplicate enrolment. Predict a join result. Next change a course title and compare the changes needed with a design that copied the title into every enrolment. The goal is to expose a concrete update anomaly, not recite a normalisation slogan.

**Scenario:** a student is enrolled in a nonexistent course. **Evidence:** the rule that should reject or detect it, a sample invalid record, and an expected outcome. If you execute a local SQL example, name its engine; local SQLite behaviour is not a test of Azure SQL.

<a id="dp-900-unit-3"></a>

## 3. Choose who operates the database

Compare Azure SQL Database, Managed Instance, and SQL Server on a VM for a new app and a migration. List compatibility dependencies, network and identity needs, maintenance responsibilities, and recovery expectations. Add an open-source engine option where the existing application requires it. Separate a justified recommendation from a claim that one product is always best.

**Scenario:** the migration inventory includes a component requiring guest operating-system access. **Evidence:** a compatibility question list, an operating-responsibility table, and a proof-of-concept plan with success criteria. No deployment is required; state which assumptions still need testing before accepting a target.

<a id="dp-900-unit-4"></a>

## 4. Reconcile a small data pipeline

Make six synthetic download events: include one duplicate identifier and one record missing a course. Define valid input, a unique event, and the completion condition. Draw an ETL route and an ELT route, locating validation and rejected-record storage in each. Explain when batch processing meets the required delay and when a streaming design might be justified.

**Scenario:** the dashboard total differs from the source row count. **Evidence:** source, duplicate, rejected, and accepted counts with a reproducible explanation. Give the owner and response for a failed run. A successful pipeline status does not prove that its business totals are correct.

<a id="dp-900-unit-5"></a>

## 5. Define one trustworthy analytical measure

Choose a reporting grain, such as one completed download event, and define a fact with course and date context. Specify time zone, late-event treatment, and freshness. Explain which part stores data, which transforms it, which provides the semantic model, and which displays a report. Compare a lake, warehouse, or lakehouse according to the work required rather than a product label.

**Final evidence:** submit your storage matrix, relational sketch, pipeline reconciliation, and a mock monthly report with its measure definition. Explain the relevant roles of Fabric, Synapse, and Power BI. Identify one unanswered question for the official guide; a good mock report does not demonstrate cloud operation or exam readiness.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) · [Data notes](../../en/04-storage.md)
