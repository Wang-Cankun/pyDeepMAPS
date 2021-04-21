# runtime:2.3GB, devel: 5.27GB
FROM wangcankun100/deepmaps-python-base
LABEL maintainer="Cankun Wang <cankun.wang@osumc.edu>"

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000
COPY . .
RUN mkdir /data

ENTRYPOINT ["/tini", "--"]
CMD ["python","-m", "flask", "run"]
#CMD ["/bin/bash"]
