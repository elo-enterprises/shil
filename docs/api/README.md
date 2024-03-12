## API for 'shil' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### shil
* Overview:  [source code](/src/shil/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### shil.__main__
* Overview: (entrypoint) | [source code](/src/shil/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`shil.__main__._fmt`](/src/shil/__main__.py#L67-L88) with signature ``
  * [`shil.__main__._invoke`](/src/shil/__main__.py#L49-L64) with signature ``
  * [`shil.__main__.entry`](/src/shil/__main__.py#L19-L23) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`shil.__main__.report`](/src/shil/__main__.py#L26-L46) with signature `(output, json: bool = False, rich: bool = False) -> None`
-------------------------------------------------------------------------------
### shil.util
* Overview:  [source code](/src/shil/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`shil.util.Runner`](/src/shil/util.py#L27-L28) with signature `(**kwargs)`
  * [`shil.util.invoke`](/src/shil/util.py#L11-L24) with signature `(*args, **kwargs)`
-------------------------------------------------------------------------------
### shil.bin
* Overview:  [source code](/src/shil/bin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shil.console
* Overview:  [source code](/src/shil/console.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shil.parser
* Overview:  [source code](/src/shil/parser/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`shil.parser.fmt`](/src/shil/parser/__init__.py#L13-L36) with signature `(text, filename='?')`
-------------------------------------------------------------------------------
### shil.parser.grammar
* Overview:  [source code](/src/shil/parser/grammar.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shil.parser.semantics
* Overview:  [source code](/src/shil/parser/semantics.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`shil.parser.semantics.Semantics`](/src/shil/parser/semantics.py#L12-L130)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
    * with admonitions:  [🐉 Complex](/src/shil/parser/semantics.py#L34 "score 10 / 7") 
-------------------------------------------------------------------------------
### shil.models
* Overview:  [source code](/src/shil/models/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`shil.models.Invocation`](/src/shil/models/__init__.py#L23-L222)
    * with bases ([BaseModel](#shilmodelsbase),)
    * with admonitions:  [🐉 Complex](/src/shil/models/__init__.py#L79 "score 15 / 7") 
  * [`shil.models.InvocationResult`](/src/shil/models/__init__.py#L225-L265)
    * with bases ([Invocation](#shilmodels),)
* Classes: (2 total)
  * [`shil.models.Invocation`](/src/shil/models/__init__.py#L23-L222)
    * with bases ([BaseModel](#shilmodelsbase),)
    * with admonitions:  [🐉 Complex](/src/shil/models/__init__.py#L79 "score 15 / 7") 
  * [`shil.models.InvocationResult`](/src/shil/models/__init__.py#L225-L265)
    * with bases ([Invocation](#shilmodels),)
-------------------------------------------------------------------------------
### shil.models.base
* Overview:  [source code](/src/shil/models/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`shil.models.base.BaseModel`](/src/shil/models/base.py#L7-L15)
    * with bases ([BaseModel](#pydanticmain),)
