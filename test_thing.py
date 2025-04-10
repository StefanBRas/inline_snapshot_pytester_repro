from inline_snapshot import snapshot

def test_not_pytester():
    assert "hey" == snapshot()

def test_pytester(pytester):
    pytester.runpytest()

