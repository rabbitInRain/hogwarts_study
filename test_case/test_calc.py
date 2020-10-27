import pytest

from test_case.calc import Calc


class TestDemo:
    def setup_class(self):
        self.calc = Calc()
    def setup(self):
        pass

    @pytest.mark.parametrize('a,b,c,d',[[10,5,2,50],[4,2,2,8],[6,5,2,30]])
    def test_calc(self,a,b,c,d):
        assert self.calc.div(a,b) == c
        assert self.calc.mul(a,b) == d