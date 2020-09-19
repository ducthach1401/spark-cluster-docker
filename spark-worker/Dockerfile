FROM bde2020/spark-base

COPY start-worker.sh /
ENV SPARK_WORKER_WEBUI_PORT 8081
ENV SPARK_WORKER_LOG /spark/logs

CMD ["/bin/bash", "/start-worker.sh"]