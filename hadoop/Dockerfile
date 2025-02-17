FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages: OpenJDK, wget, tar, and rsync
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget tar rsync && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Java and Hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ENV PATH=${PATH}:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin

# Download and install Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz -C /opt && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Copy Hadoop configuration files into the image (if provided)
COPY config/hadoop/ ${HADOOP_HOME}/etc/hadoop/

# Copy the entrypoint script and set execution permissions
COPY hadoop/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the default command to start the namenode (can be overridden by docker-compose)
ENTRYPOINT ["/entrypoint.sh"]
CMD ["namenode"]
