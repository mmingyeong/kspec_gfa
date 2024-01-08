
# The KSPEC GFA Camera Controller
- KSPEC-GFA is a tool for guiding, focusing, and acquisition sequence control in KSPEC observation.
- The Controller communicate with Basler Guide cameras for guiding and focusing processes.
- The Controller use the [pypylon](https://github.com/basler/pypylon) library as the middleware for the communication.

# Getting Started

## Installation

`kspec-gfa` can be installed using by cloning this repository

```console
git clone https://mmingyeong@bitbucket.org/mmmingyeong/kspec-gfa.git
```

The preferred installation for development is using [poetry](https://python-poetry.org/)

```console
cd kspec-gfa
poetry install
```

## Quick Start

```console
cd python/kspec-gfa/commander
python status.py
```

If you want to know the usage of each command, use --help option.

```console
python grab.py --help
```