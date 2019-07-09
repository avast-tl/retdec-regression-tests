from regression_tests import *

class TestX86GccExe_ack(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.mingw32-gcc-4.7.3.O0.g.ex',
        args='--select 0x401560' # ack
    )

    def test(self):
        assert self.out_c.has_just_funcs('ack')

class TestX86GccExe_main(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.mingw32-gcc-4.7.3.O0.g.ex',
        args='--select 0x4015bb' # main
    )

    def test(self):
        assert self.out_c.has_just_funcs('main')
