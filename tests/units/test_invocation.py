"""
    test-suite: units
"""
import os  # noqa

import pytest  # noqa
from fleks.util import lme
from rich.console import Console

from shil import Invocation, Runner, invoke, models  # noqa

LOGGER = lme.get_logger(__name__)


def test_runner():
    runner = Runner(
        command_logger=Console().print,
        # LOGGER.critical,
        output_logger=LOGGER.critical,
    )
    assert runner("ls /tmp").succeeded


@pytest.mark.skip(reason="broken now")
def test_system_pid():
    cmd = Invocation(command="echo testing", system=True)
    resp = cmd()
    assert resp.pid != -1


def test_log_command():
    cmd = Invocation(
        command="echo testing",
        system=True,
        log_command=True,
    )()
    resp = cmd()


def test_invocation_simple():
    cmd = Invocation(command='printf "1\n2\n3"')
    resp = cmd()
    assert "1\n2\n3" == resp.stdout.strip()
    assert resp.success
    assert not resp.failure


def test_invocation_pipe():
    cmd = Invocation(command="""echo 'printf "1\n2\n3"' | bash""")
    resp = cmd()
    assert "1\n2\n3" == resp.stdout.strip()
    assert resp.success
    assert not resp.failure


def test_invocation_input():
    cmd = Invocation(command="bash", stdin='printf "1\n2\n3"')
    resp = cmd()
    assert resp.succeeded
    assert not resp.failed
    assert "1\n2\n3" == resp.stdout.strip()
