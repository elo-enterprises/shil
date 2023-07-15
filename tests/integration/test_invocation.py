"""
    test-suite: integration
"""
import os
import tempfile

from shil import Invocation, invoke, models
from rich.console import Console

console = Console()


def test_rich_console():
    cmd = Invocation(command="echo testing")
    resp = cmd()
    console.print(cmd)
    console.print(resp)


def test_Invocation_is_lazy():
    with tempfile.NamedTemporaryFile() as tmp:
        fname = tmp.name
    assert not os.path.exists(fname)
    cmd = Invocation(command=f"touch {fname}")
    assert not os.path.exists(fname)
    resp = cmd()
    assert os.path.exists(fname)
    os.remove(fname)


def test_invoke_is_eager():
    with tempfile.NamedTemporaryFile() as tmp:
        fname = tmp.name
    assert not os.path.exists(fname)
    resp = invoke(f"touch {fname}")
    assert os.path.exists(fname)
    assert isinstance(resp, (models.InvocationResult))
    os.remove(fname)
