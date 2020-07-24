import pytest
# from slmigrate import slmigrate
# from slmigrate import systemlinkmigrate
from slmigrate import systemlinkmigrate

def test_main():
    pass

def test_add_numbers():
    sum = systemlinkmigrate.add_numbers(1,2)
    assert sum == 3

def test_parse_arguments():
    parser = systemlinkmigrate.parse_arguments(["--tags", "--tag", "--taghistory", "--tagingestion", "--opc", "--opcua", "--opcuaclient"])
    assert parser.parse_known_args()

