# Hadoop and Spark in Docker

This repository contains all necessary files to set up a containerized Hadoop and Spark environment.

## Files Overview

- **hadoop/Dockerfile**  
  Builds the custom Hadoop image by installing Java, downloading and extracting Hadoop, and setting environment variables.

- **hadoop/entrypoint.sh**  
  Starts the appropriate Hadoop service (NameNode, DataNode, ResourceManager, or NodeManager) based on the provided argument.

- **hadoop/docker-compose.yml**  
  Orchestrates the Docker containers for Hadoop and Spark, defining services, volumes, ports, and dependencies.

- **config/hadoop/core-site.xml**  
  Configures core Hadoop settings (fs.defaultFS).

- **config/hadoop/hdfs-site.xml**  
  Contains HDFS-specific settings, including replication and storage directories.

- **config/hadoop/yarn-site.xml**  
  Configures YARN by setting the ResourceManager hostname and NodeManager auxiliary services.

- **hadoop/workspace/pyspark.ipynb**  
  A Jupyter Notebook for interactive PySpark development (optional).

## How to Run

1. Build and start the containers:
   ```bash
   docker-compose -p hadoop_cluster -f hadoop/docker-compose.yml up --build -d
   ```
2. Check logs if needed:
   ```bash
   docker-compose -p hadoop_cluster logs -f
   ```
3. Access Web UIs:
   - Hadoop NameNode: http://localhost:9870
   - YARN ResourceManager: http://localhost:8088
   - Spark UI: http://localhost:8080
