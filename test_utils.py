import pytest
import utils
import math

def test_fact():
    # À compléter...
    assert utils.fact(5)==120
    assert utils.fact(0)==1
    with pytest.raises(ValueError):
        utils.fact(-1)
    pass

def test_roots():
    # À compléter...
    assert utils.roots(2, 4, 1)== pytest.approx((-1.7,-0.29))
    assert utils.roots(2, 0, -2)== pytest.approx((-1,1))
    pass

def test_integrate():
    # À compléter...
    pass
