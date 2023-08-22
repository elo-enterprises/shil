"""
    test-suite: integration
"""
import os  # noqa
import tempfile

import rich
from rich.console import Console

from shil import Invocation, invoke, models

import pytest  # noqa


console = Console()


def test_rich():
    req = cmd = Invocation(command='echo {"foo":"bar"}')
    resp = cmd()
    rich.print(req)
    print()
    rich.print(resp)


def test_rich_console_command():
    console.print()
    cmd = Invocation(
        command="echo testing",
        system=True,
        # log_command=True, use_log=console.print,
    )
    console.print(cmd)
    # sys.stdin.readline()


def test_rich_console_command_output():
    cmd = Invocation(command="echo testing")
    resp = cmd()
    console.print()
    console.print(resp)
    # sys.stdin.readline()


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
