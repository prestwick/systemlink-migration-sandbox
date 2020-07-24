import pytest
from slmigrate import slmigrate


def test_main():
    pass

def test_add_numbers():
    sum = slmigrate.add_numbers(1,2)
    assert sum == 3

def test_parse_arguments():
    parser = slmigrate.parse_arguments(["--tags", "--tag", "--taghistory", "--tagingestion", "--opc", "--opcua", "--opcuaclient"])
    # assert parser.parse_known_args(["Namespace", ["--tags"]])
    assert parser.parse_known_args()

