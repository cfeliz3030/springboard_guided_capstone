
## Guided Capstone Step Two: Data Ingestion

Learning Objectives:
* Learn to parse CSV and JSON files
* Create a Spark DataFrame with defined schema
* Persist the Spark DataFrame into file system using partitioning

The data that’s submitted by exchanges will be in two different formats: CSV and JSON. CSV
means Comma Separated Values, so it is a text document that contains many values separated
by commas. JSON is JavaScript Object Notation, in which text data is stored following a
standard convention. Both of these are flat text files containing trade and quotes from different
numbers of fields. The record type can be identified by column ‘rec_type’ which is a fixed
position for CSV files.

## Tools used:
* Azure Databricks
* Azure Blob Storage
* Azure azcopy

## Usage
* Sign up for an Azure account.
* Create blob storage object and Azure Databricks cluster.
* Load data files into storage account using azcopy.
* Run ```springcapital_dataingestion.ipynb```

## File Final Output + File Partitions
![Screen Shot 2021-12-29 at 7 22 00 PM](https://user-images.githubusercontent.com/60493376/147722831-7ebfbc0b-7191-44a7-91c7-2bf8bbed9a71.png)

![Screen Shot 2021-12-29 at 8 21 26 PM](https://user-images.githubusercontent.com/60493376/147722859-774bfa15-d248-4a77-94f1-8c42de3bfd4f.png)
