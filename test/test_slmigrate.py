import pytest
# from slmigrate import slmigrate
# from slmigrate import systemlinkmigrate
# from slmigrate import systemlinkmigrate

import systemlinkmigrate

def test_main():
    pass

def test_add_numbers():
    sum = systemlinkmigrate.add_numbers(1,2)
    assert sum == 3

def test_parse_arguments():
    parser = systemlinkmigrate.parse_arguments(["--tags", "--tag", "--taghistory", "--tagingestion", "--opc", "--opcua", "--opcuaclient", "--fis", "--files", "--file"])
    assert parser.parse_known_args()

