# DP-900 · 10 cases with reasoned answers

[Guide](DP-900.md) · [Workbook](DP-900-workbook.md) · [Contents](README.md)

Original practice scenarios, not real exam questions. First state the requirement, then reject an alternative and describe the evidence you would collect. No cloud deployment is claimed.

## 1. The notes app stores PDFs and searchable ownership metadata. Must both go into one SQL table?

<details>
<summary>Reasoning</summary>

No. One plausible design stores PDF objects in Blob Storage and their ownership and course relationships in a database. The important part is explaining the access and consistency boundary: an upload may succeed while its metadata update fails. Define a recoverable workflow and how orphaned files are detected. A single database representation is another possible design if its requirements justify it, but “all data must be a SQL row” is not a useful starting assumption.

</details>

## 2. A JSON file contains optional nested attributes. Is it unstructured because some fields are missing?

<details>
<summary>Reasoning</summary>

JSON can represent semi-structured data: its keys and nesting carry organisation even when records differ. Missing fields do not remove that structure. Separate the representation from its quality and storage choice. Ask whether a missing field is valid, unknown, or an ingestion error, and record how a consumer should react. A document database might fit the access pattern, but the presence of JSON alone does not settle that architectural decision.

</details>

## 3. Every enrolment row repeats a course's title and lecturer. What failure could normalisation prevent?

<details>
<summary>Reasoning</summary>

A course title change could update some enrolment rows and leave others with an old value. Keeping a Courses record identified by a stable key, then referencing it from Enrolments, reduces that update anomaly. Explain the required constraints and how joins reconstruct a useful result. This does not mean duplication is forbidden everywhere: an analytical snapshot may intentionally preserve historical descriptions. State whether the question concerns current transactional truth or a historical reporting model.

</details>

## 4. A reporting query slows down live enrolment. Would moving the chart into Power BI automatically remove the database load?

<details>
<summary>Reasoning</summary>

No. The effect depends on how the model obtains and refreshes its data. A report can still query the operational source or create expensive refresh work. Clarify freshness, query patterns, and source capacity before choosing a reporting design. A curated analytical copy may isolate some work, but introduces refresh delay and pipeline responsibilities. Measure source workload and define what “up to date” means rather than assuming a different visualisation tool changes the underlying access.

</details>

## 5. An existing SQL Server application needs operating-system components. Is Azure SQL Database always a drop-in replacement?

<details>
<summary>Reasoning</summary>

No. Inventory those components and other dependencies before selecting a target. Azure SQL Database, Managed Instance, and SQL Server on Azure VMs have different management and compatibility boundaries. A VM can provide operating-system access but leaves more maintenance with the team. Managed Instance may address some instance-level requirements without satisfying every external dependency. Build a compatibility list and a migration test plan; a familiar database engine is not evidence that the complete application will run unchanged.

</details>

## 6. A student says Azure Table Storage provides foreign keys because its name contains Table. How would you correct the design?

<details>
<summary>Reasoning</summary>

Table Storage is a nonrelational entity store, not a managed relational SQL service. Do not assume relational joins or foreign-key enforcement from its name. Identify the actual reads, updates, relationships, and consistency requirements, then compare a suitable entity model with a relational design. The useful evidence is a worked example: show how an enrolment retrieves its related course and how invalid references are prevented or detected. Product names are clues to investigate, not substitutes for capabilities.

</details>

## 7. Nightly processing meets a next-morning report deadline. Should the team replace it with streaming just to sound modern?

<details>
<summary>Reasoning</summary>

Start with the business delay requirement. If a reliable nightly batch provides the needed result on time, streaming may add operational work without changing the decision users can make. If staff must react to overload within minutes, evaluate a lower-latency path for that requirement. In either case handle duplicate records, incomplete input, and retries. Compare end-to-end freshness and failure recovery, not only how often one processing component runs.

</details>

## 8. Raw data is loaded into a warehouse and cleaned there. Is this ETL, and does the warehouse make validation unnecessary?

<details>
<summary>Reasoning</summary>

That ordering describes ELT: load first, transform using the target's processing capabilities. ETL performs the transformation before loading the intended destination. Neither removes the need for data contracts and checks. Define where invalid records go, which transformations are repeatable, and how accepted totals reconcile with the source. Keep restricted raw data access controlled even when analysts only see a cleaned model; an easy query interface does not establish that the underlying records are safe or correct.

</details>

## 9. A dashboard counts download events. Retries produce duplicate event IDs. Is COUNT(*) necessarily the number of completed downloads?

<details>
<summary>Reasoning</summary>

Only if the data definition makes each counted row one completed download. Duplicate deliveries can inflate COUNT(*). Define the business event, stable identifier, completion condition, and reporting interval, then deduplicate or aggregate according to that definition. Keep a rejected or duplicate count so the change is explainable. Test with a tiny dataset containing one repeated ID and one incomplete download. A plausible chart does not prove that its measure represents the user's intended question.

</details>

## 10. Six course records fit in a document model. Does that prove Cosmos DB is the only sensible store?

<details>
<summary>Reasoning</summary>

No. Many services can store six records; that example only demonstrates representability. Compare the expected application queries, relationships, update behaviour, consistency, operational requirements, and team skills. A relational database may be simpler when constraints and related entities dominate; a document model may suit other patterns. Document one reason for your preferred option and one condition that would change it. Fundamentals preparation should build this reasoning rather than attach a database product to every JSON-shaped example.

</details>

Sources: [official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900), [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), [Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction), [ETL/ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl), [Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview).
