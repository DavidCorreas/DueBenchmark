FROM nvcr.io/nvidia/pytorch:20.12-py3

COPY .devcontainer/*.sh /tmp/library-scripts/
RUN bash /tmp/library-scripts/common-debian.sh \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts