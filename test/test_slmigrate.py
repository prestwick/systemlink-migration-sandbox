from slmigrate import slmigrate


def test_main():
    pass

def test_argparser():
    assert setup_argparse() == "Namespace(opc=False, tag=False)"
