def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")

def test_out():
    print("test out")

class TestDemo:

    # 类的前后执行
    def setup_class(self):
        print("TestDemo setup")

    def teardown_class(self):
        print("TestDemo teardown")

    # 方法前后执行
    def setup(self):
        print("function setup")

    def teardown(self):
        print("function teardown")

    def test_demo(self):
        print("testing")

    def test_demo2(self):
        print("2")
