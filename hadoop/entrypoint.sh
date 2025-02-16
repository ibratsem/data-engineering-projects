#!/bin/bash
set -e

case "$1" in
    namenode)
        echo "Starting Hadoop Namenode..."
        exec ${HADOOP_HOME}/bin/hdfs namenode
        ;;
    datanode)
        echo "Starting Hadoop Datanode..."
        exec ${HADOOP_HOME}/bin/hdfs datanode
        ;;
    resourcemanager)
        echo "Starting YARN ResourceManager..."
        exec ${HADOOP_HOME}/bin/yarn resourcemanager
        ;;
    nodemanager)
        echo "Starting YARN NodeManager..."
        exec ${HADOOP_HOME}/bin/yarn nodemanager
        ;;
    *)
        exec "$@"
        ;;
esac
