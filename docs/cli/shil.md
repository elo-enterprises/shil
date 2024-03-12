

## shil CLI



**entrypoint:** `python -mshil` [src](src/shil/__main__.py)

<hr/>


```
Usage: python -m shil [OPTIONS] COMMAND [ARGS]...

  CLI tool for `shil` library

Options:
  --help  Show this message and exit.

Commands:
  fmt     Pretty-printer for (line-oriented) bash
  invoke  Invocation tool for (line-oriented) bash

```



**entrypoint:** `python -mshil invoke  CMD` [src](src/shil/__main__.py)

<hr/>


```
Usage: python -m shil invoke [OPTIONS] CMD

  Invocation tool for (line-oriented) bash

Options:
  --json  use JSON output
  --rich  use rich output
  --help  Show this message and exit.

```



**entrypoint:** `python -mshil fmt  [FILENAME]` [src](src/shil/__main__.py)

<hr/>


```
Usage: python -m shil fmt [OPTIONS] [FILENAME]

  Pretty-printer for (line-oriented) bash

Options:
  --json  use JSON output
  --rich  use rich output
  --help  Show this message and exit.

```


