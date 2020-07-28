import pytest
# from slmigrate import slmigrate
# from slmigrate import systemlinkmigrate
# from slmigrate import systemlinkmigrate

import systemlinkmigrate
import slmigrate.constants as constants
import slmigrate.capture as capture

def test_main():
    pass

def test_add_numbers():
    sum = systemlinkmigrate.add_numbers(1,2)
    assert sum == 3

def test_parse_arguments():
    parser = systemlinkmigrate.parse_arguments([constants.tag.arg, constants.opc.arg, constants.fis.arg, constants.alarmrule.arg, constants.testmonitor.arg])
    assert parser.parse_known_args()

