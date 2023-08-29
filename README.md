<table>
  <tr>
    <td colspan=2>
      <strong><u>shil</u></strong>&nbsp;&nbsp;&nbsp;&nbsp;
      <a href=https://pypi.org/project/shil><img src="https://img.shields.io/pypi/l/shil.svg"></a>
      <a href=https://pypi.org/project/shil><img src="https://badge.fury.io/py/shil.svg"></a>
      <a href="https://github.com/elo-enterprises/shil/actions/workflows/python-publish.yml"><img src="https://github.com/elo-enterprises/shil/actions/workflows/python-publish.yml/badge.svg"></a><a href="https://github.com/elo-enterprises/shil/actions/workflows/python-test.yml"><img src="https://github.com/elo-enterprises/shil/actions/workflows/python-test.yml/badge.svg"></a>
    </td>
  </tr>
  <tr>
    <td width=15%><img src=https://raw.githubusercontent.com/elo-enterprises/shil/master/img/icon.png style="width:150px"></td>
    <td>
      Shell-util library for python.  <br/>
      Includes helpers for subprocess invocation, shell-formatters / pretty-printers, and more.
      <br/>
    </td>
  </tr>
</table>

---------------------------------------------------------------------------------

  * [Overview](#overview)
  * [Features](#features)
    * [Shell-formatters / pretty-printers](#shell-formatters--pretty-printers)
    * [Subprocess Invocation](#subprocess-invocation)
  * [Installation](#installation)
  * [Usage (CLI)](#usage-cli)
  * [Usage (API)](#usage-api)
    * [OOP-style Dispatch](#oop-style-dispatch)
    * [Functional approach to dispatch](#functional-approach-to-dispatch)
    * [Loading data when command-output is JSON](#loading-data-when-command-output-is-json)
    * [Serialization with Pydantic](#serialization-with-pydantic)
    * [Caller determines logging](#caller-determines-logging)
    * [Rich-console Support](#rich-console-support)
    * [Stay DRY with Runners](#stay-dry-with-runners)


---------------------------------------------------------------------------------

## Overview

The `shil` library provides various shell-utilities for python.

-------------------------------------------------------------------------------

## Features

### Shell-formatters / pretty-printers

* A somewhat usable parser / grammar for bash
* Console support for [rich](https://rich.readthedocs.io/en/stable/index.html) & [rich protocols](https://rich.readthedocs.io/en/stable/protocol.html)

### Subprocess Invocation

There's a lot of shell-related libraries out there, especially for invocation (see for example [this list](https://www.pyinvoke.org/prior-art.html)).
The interface for `shil` is hopefully unsurprising, and something that's convenient but not fancy.  It's a utility, and not a huge framework.  

The main goal is to provide an API that is simple and stable, without a ton of dependencies.

```
>>> import shil 
>>> proc = shil.invoke('echo hello world')
>>> assert proc.succeeded
>>> assert proc.stdout.strip()=='hello world'
>>>
```

Beyond such basics, shil includes support for [rich output](#) and uses pydantic for datastructures.

See the [API docs](#usage-api) for more detailed information.  


---------------------------------------------------------------------------------

## Installation

See [pypi](https://pypi.org/project/shil/) for available releases.

```
pip install shil
```

---------------------------------------------------------------------------------

## Usage (CLI)

The shil library publishes a small CLI tool, mostly just for testing & demoing the API behaviour. See [the CLI docs](docs/cli/) for the latest (autogenerated) help.

-------------------------------------------------------------------------------

## Usage (API)

See also:

* [the unit-tests](tests/units) for some examples of library usage
* [the smoke-tests](tests/smoke/test.sh) for example usage of stand-alone scripts

### OOP-style Dispatch 

This uses `shil.Invocation` and returns `shil.InvocationResponse`.

```python
>>> import shil 
>>> req = cmd = shil.Invocation(command='printf hello-world\n')
>>> resp = cmd()
>>> print(resp.stdout)
hello-world
>>>
```

### Functional approach to dispatch

Use `shil.invoke`, get back `shil.InvocationResponse` 

```python

>>> import shil 
>>> resp = shil.invoke(command='printf hello-world\n')
>>> print(resp.stdout)
hello-world
>>>
```

### Loading data when command-output is JSON

```python
>>> import shil 
>>> cmd = shil.Invocation(command="""echo '{"foo":"bar"}'""", load_json=True)
>>> resp = cmd()
>>> print(resp.data)
{'foo': 'bar'}
>>> assert type(resp.data) == type({})
>>> assert resp.data['foo'] == 'bar'
>>>
```

### Serialization with Pydantic

```python
>>> import json, shil 
>>> req = cmd = shil.Invocation(command="""echo pipes-are-allowed|grep allowed""")
>>> resp = cmd()
>>> keys = resp.dict().keys()
>>> expected = 'stdout stderr failed failure success succeeded data'.split()
>>> assert all([k in keys for k in expected])
>>>
```

### Caller determines logging 

Works like this with basic logger:

```python
>>> import logging, shil 
>>> logger = logging.getLogger()
>>> resp = shil.invoke('ls /tmp', command_logger=logger.critical, output_logger=logger.warning)
>>>
```

Supports using [rich-logger](https://rich.readthedocs.io/en/stable/logging.html) too:

```python
>>> import shil 
>>> from rich.console import Console 
>>> console = Console(stderr=True)
>>> resp = shil.invoke('ls /tmp', command_logger=console.log)
>>>
```

### Rich-console Support

Besides using rich-logger as above, you can use the [rich-protocol](https://rich.readthedocs.io/en/stable/protocol.html) more directly.  

Printing works the way you'd expect for `Invocation` and `InvocationResponse`.

```python
import shil, rich
req = cmd = shil.Invocation(command='echo {"foo":"bar"}')
resp = cmd()
rich.print(req)
rich.print(resp)
```
By default, output looks roughly like this:

![rich console](img/rich-1.png)
<br/>
![rich console](img/rich-2.png)

### Stay DRY with Runners

Runner's are basically just [partials](https://en.wikipedia.org/wiki/Partial_application) on `shil.invoke`.  It's simple but this can help reduce copying around repetitive configuration.

```python
>>> import shil 
>>> from rich.console import Console 
>>> console=Console(stderr=True)
>>> runner = shil.Runner(output_logger=console.log, command_logger=console.log)
>>> resp = runner('ls /tmp')
>>> assert isinstance(resp,(shil.InvocationResult,))
>>>
```
