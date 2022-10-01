from curses.ascii import NUL
from script_options import option, options_handler

def test_register_option_success():
    opt_handler = options_handler()
    test_option = option()

    test_option.short_option = "o"
    assert opt_handler.register_option(test_option)

def test_register_option_fail_no_options_string():
    opt_handler = options_handler()
    test_option = option()

    test_option.short_option = ""
    assert not opt_handler.register_option(test_option)

def test_register_option_fail_duplicated_short():
    opt_handler = options_handler()
    test_option = option()
    test_option2 = option()


    test_option.short_option = "a"
    test_option2.short_option = "b"
    
    assert opt_handler.register_option(test_option)
    assert not opt_handler.register_option(test_option2)

def test_register_option_fail_duplicated_long():
    opt_handler = options_handler()
    test_option = option()
    test_option2 = option()


    test_option.long_option = "aaa"
    test_option2.long_option = "bbb"
    
    assert opt_handler.register_option(test_option)
    assert not opt_handler.register_option(test_option2)

def test_register_option_fail_numeric_short():
    opt_handler = options_handler()
    test_option = option()

    test_option.short_option = 1
    assert not opt_handler.register_option(test_option)

def test_register_option_fail_numeric_long():
    opt_handler = options_handler()
    test_option = option()

    test_option.long_option = 1
    assert not opt_handler.register_option(test_option)