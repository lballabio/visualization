FROM lballabio/jupyter

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y git \
 && pip install --no-cache-dir \
        git+https://github.com/lballabio/visualization.git \
 && apt-get purge -y git \
 && apt-get --purge autoremove -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

