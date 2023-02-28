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

    assert utils.roots(2, 0, -2) == pytest.approx((-1.0, 1.0))
    assert utils.roots(2, 1, -2) == pytest.approx((-1.28077640, 0.78077640))
    assert utils.roots(2, 1, 2) == tuple()

    pass

def test_integrate():
    # À compléter...

    assert abs(utils.integrate('(1-x**2)**(1/2)',-1,1)-math.pi/2) < 0.00001
    assert utils.integrate('(1-x**2)**(1/2),-1,1') == pytest.approx(math.pi/2)
    pass
