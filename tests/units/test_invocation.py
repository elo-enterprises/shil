"""
    test-suite: units
"""
from shil import Invocation


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
