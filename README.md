# AWS Retail ETL Pipeline

A serverless ETL pipeline built on AWS to automate the ingestion, validation, transformation, and loading of retail sales data into Amazon Redshift.

## Features

* Automated CSV file validation
* Data transformation using AWS Glue
* Data warehouse loading into Amazon Redshift
* Automatic archival of processed files
* Execution logging and error handling

## AWS Services

* Amazon S3
* AWS Lambda
* AWS Glue
* Amazon Redshift
* Amazon CloudWatch
* AWS IAM

## Repository Structure

```text
.
├── README.md
├── report.docx
├── file_validation_lambda.py
├── ETL_orchestrator_lambda.py
├── archive_lambda.py
├── architecture.png
└── screenshots/
```

## Workflow

1. Upload a CSV file to `raw/sales/`.
2. `file_validation_lambda.py` validates the uploaded file.
3. `ETL_orchestrator_lambda.py` starts the ETL process by:

   * Running AWS Glue jobs
   * Executing Redshift SQL scripts
   * Triggering the archive Lambda
4. `archive_lambda.py` archives processed data and cleans temporary folders.

## Notes

* SQL scripts used for Redshift loading are not included in this repository.
* In production environments, orchestration can be implemented using **AWS Step Functions** or **Apache Airflow (Amazon MWAA)** instead of a Lambda-based orchestrator.

##
