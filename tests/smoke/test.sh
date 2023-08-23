#!/usr/bin/env bash
set -xeuo pipefail

# test command-line is available 
python -m shil --help

# test invocation tool
python -m shil invoke --help
python -mshil invoke 'ls'
python -mshil invoke 'ls' --rich

# test basic formatting
python -m shil fmt --help
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