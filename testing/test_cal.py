import pytest
import yaml

from pythoncode.other import Calculator


@pytest.mark.login
def test_login():
    print("登陆")

# 解析测试数据文件
def get_datas():
    with open('../data/calc.yml') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_ids)
    print(add_datas)
    return [add_datas,add_ids]


# 解析测试步骤文件
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if 'add' == step:
            print("exec add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("exec add1")
            result = calc.add1(a, b)
        assert expect == result

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

    @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids=get_datas()[1])
    def test_add(self, a, b, expect):
        assert (self.cal.add(a, b)) == expect

    @pytest.mark.parametrize('a,b,expect',[
        (0.2, 0.1, 0.3), (0.01, 0.46, 0.47)
    ])
    def test_add_float(self, a, b, expect):
        assert (round(self.cal.add(a, b),2)) == expect

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
        (2, 1, 2),(9, 3, 3)
    ],ids=['2/1','9/3'])
    def test_div(self, a, b, expect):
        # with pytest.raises(ZeroDivisionError):
        #     self.cal.div(a, 0)
        assert (self.cal.div(a, b)) == expect

    def test_add_steps(self):
        a = 1
        b = 1
        expect = 2
        steps("../steps/add_steps.yml", self.cal, a, b, expect)
        # assert 2 == self.cal.add(1,1)
        # assert 3 == self.cal.add1(1,2)
        # assert 0 == self.cal.add(-1,1)
