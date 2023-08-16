#!/usr/bin/env bash
set -xeuo pipefail

# test command-line is available 
python -m shil --help
python -m shil fmt --help
python -m shil invoke --help

# test basic formatting
printf '\
  docker run -it --rm -v `pwd`:/workspace \
  -w /workspace --entrypoint bash \
  some-image -c "some command"' \
| python -m shil fmt - 

# test rich output
printf '\
  docker run -it --rm -v `pwd`:/workspace \
  -w /workspace --entrypoint bash \
  some-image -c "some command"' \
| python -m shil fmt - --rich 