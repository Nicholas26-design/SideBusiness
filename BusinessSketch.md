skills:
data engineering
data analytics
machine learning/predictive analytics. 

What do you need? What does the consumer need?

Foundation:

No matter what, we need a database/ data storage. 

In terms of etl tooling, i would pick apache flink because you can stream data and batch process it. 

data visualization could then be real-time. Not sure the vendor for that. 

Data sources:

provided by customer or design application to harvest. customer provides seems easier at the moment. 

Machine Learning/Predictive analytics:

premium package offering. 

end product: 3 tiers of services. 

Bronze: batch analytics
Silver: real-time analytics
Gold: predictive analytics


Data Sources (Kafka, Kinesis, API, DB)
        │
        ▼
   Apache Flink
 (streaming ETL)
        │
        ▼
    Delta Lake
 (Bronze → Silver → Gold)
        │
        ▼
   Downstream consumers
 (e.g. Databricks SQL, Power BI)
