
## Step Five: Pipeline Orchestration
Now that you have all of your functionality implemented, you need to orchestrate your pipeline,
connecting all of the individual components into an end-to-end data pipeline. In the real world,
data processing jobs are typically organized into automated workflows.
There are many ways to define a workflow and it’s scope, but typically workflows are repeatable
pipeline units which can be run independently. In cloud architecture, a workflow can be run in an
elastic Hadoop cluster with input and output data that are persistent on cloud storage such as
Azure Blob Storage. Your guided pipeline can be divided into two workflows:
- Preprocessing Workflow: data ingestion and batch load
- Analytical Workflow: analytical ETL job
In this project, you’ll launch your Spark job using a command line shell script in each workflow.

In order to schedule and run my workflow i used azure databricks. Below are screenshots of 3 tasks running sequentially as one job.
- Task 1: Extract Data
- Task 2: EOD Batch
- Task 3: Analytical ETL

![Screen Shot 2022-03-10 at 12 03 40 AM](https://user-images.githubusercontent.com/60493376/157820365-f0521d12-76c8-4e26-b358-eca4f13c84a6.png)
![Screen Shot 2022-03-10 at 12 04 22 AM](https://user-images.githubusercontent.com/60493376/157820393-793d45d0-fbaf-4e68-9ec4-a05986d4c4e1.png)
