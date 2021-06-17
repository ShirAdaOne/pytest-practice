import pytest

from pythoncode.other import Calculator

class TestCalc:

    def setup_class(self):
        print("function start")
        self.cal = Calculator()

    def teardown_class(self):
        print("function end")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[
        (1,2,3),(3,4,7),(4,4,8)],
        ids=['1+2','3+4','4+4'])
    def test_add(self, a, b, expect):
        assert (self.cal.add(a, b)) == expect

    @pytest.mark.parametrize('a,b,expect',[
        (2,1,1),(9,4,5)
    ], ids=['2-1','9-4'])
    def test_sub(self, a, b, expect):
        assert (self.cal.sub(a, b)) == expect

    @pytest.mark.parametrize('a,b,expect',[
        (1,2,2),(3,4,12)
    ],ids=['1x2','3x4'])
    def test_mul(self, a, b, expect):
        assert (self.cal.mul(a, b)) == expect

    @pytest.mark.parametrize('a, b, expect',[
        (2,1,2),(9,3,3)
    ],ids=['2/1','9/3'])
    def test_div(self, a, b, expect):
        assert (self.cal.div(a, b)) == expect