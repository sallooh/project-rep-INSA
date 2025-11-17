FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    r-base \
    r-base-dev \
    build-essential \
    gfortran \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libbz2-dev \
    zlib1g-dev \
    liblzma-dev \
    libreadline-dev \
    libpng-dev \
    libjpeg-dev \
    libcairo2-dev \
    ca-certificates \
    wget \
    jags \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    libudunits2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN R -e "install.packages(c('DataCombine','sf','spdep','PReMiuM'), repos='https://cloud.r-project.org', dependencies=TRUE)"

WORKDIR /app

COPY rawTeam7code.r .
COPY CrowdstormingDataJuly1st.csv CrowdstormingDataset.csv

CMD [\"Rscript\", \"rawTeam7code.r\"]
