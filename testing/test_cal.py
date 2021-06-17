import pytest

from pythoncode.other import Calculator

class TestCalc:

    def setup_class(self):
        print("function start")
        self.cal = Calculator()

    def teardown_class(self):
        print("function end")

    @pytest.mark.parametrize('a,b,expect',[
        (1,2,3),(3,4,5),(4,4,8)],
        ids=['int_case','bignum_case','float_case'])
    def test_add(self, a, b, expect):
        assert (self.cal.add(a,b)) == expect

    @pytest.mark.parametrize('a,b,expect',[(1,2,3),(3,4,5)])
    def test_sub(self, a, b, expect):
        assert (self.cal.sub(a,b)) == expect

    @pytest.mark.parametrize('a,b,expect',[(1,2,3),(3,4,5)])
    def test_mul(self, a, b, expect):
        assert (self.cal.mul(a,b)) == expect
