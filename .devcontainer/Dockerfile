# Use Ubuntu 24.04 as the base image.
FROM ubuntu:24.04

# Dockblock.
LABEL author="waanlabs"
LABEL email="support@waanlabs.com"
LABEL description="Ubuntu Dev Container"
LABEL website="https://waanlabs.com"
LABEL origin="https://github.com/waanlabs/pydev"
LABEL version="1.0.0"
LABEL license="MIT"

# Custom settings.
ARG USER=wired
ARG PROJECT=pydev
ARG TIMEZONE=America/New_York

# Set non-interactive to avoid prompts during build.
ENV DEBIAN_FRONTEND=noninteractive

# Set the timezone to America/New_York.
ENV TZ=${TIMEZONE}

# Install required packages.
RUN apt-get update && \
    apt-get install -y sudo \
    software-properties-common \
    build-essential \
    bash-completion \
    make \
    wget \
    git \
    curl \
    vim \
    llvm \
    locales \
    tzdata \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup UTF-8 locale and set env.
RUN sed -i '/^#.* en_US.UTF-8 UTF-8/s/^#//' /etc/locale.gen && \
    locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Set the timezone to America/New_York. 
RUN ln -fs /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

# Create a non-root user, add to sudo group, and configure sudoers.
RUN groupadd ${USER} && \
    useradd -m -s /bin/bash -g ${USER} ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}

# Switch to new sudo user.
USER ${USER}

# Install pyenv and set env.
RUN curl https://pyenv.run | bash

RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> $HOME/.profile && \
    echo 'eval "$(pyenv init --path)"' >> $HOME/.profile && \
    echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.profile

# Add TTY to .bashrc for GPG.
RUN echo 'export GPG_TTY=$(tty)' >> ~/.profile

# Set the working directory.
WORKDIR /home/${USER}/${PROJECT}

# Change the ownership of the working directory.
RUN sudo chown -R ${USER}:${USER} /home/${USER}/${PROJECT}

# Bash as default entry point.
ENTRYPOINT ["/bin/bash"]
