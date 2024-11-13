from acrostic.generator import AcrosticGenerator

def test_acrostic_simple():
    assert len(AcrosticGenerator.generate("foo")) == 3
