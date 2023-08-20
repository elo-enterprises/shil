

## shil CLI



**entrypoint:** `python -mshil` [src](src/shil/__main__.py)



```
Usage: python -m shil [OPTIONS] COMMAND [ARGS]...

  CLI tool for `shil` library

Options:
  --help  Show this message and exit.

Commands:
  fmt     Pretty-printer for (line-oriented) bash
  invoke  Invocation tool for (line-oriented) bash

```


<hr/>

**entrypoint:** `python -mshil invoke` [src](src/shil/__main__.py)



```
Usage: python -m shil invoke [OPTIONS]

  Invocation tool for (line-oriented) bash

Options:
  --rich  use rich output
  --help  Show this message and exit.

```


<hr/>

**entrypoint:** `python -mshil fmt  [FILENAME]` [src](src/shil/__main__.py)



```
Usage: python -m shil fmt [OPTIONS] [FILENAME]

  Pretty-printer for (line-oriented) bash

Options:
  --rich  use rich output
  --help  Show this message and exit.

```


<hr/>
