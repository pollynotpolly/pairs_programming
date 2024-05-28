from lib.report_length import *

def test_report_length():
    result = report_length("Polly")
    assert result == "This string was 5 characters long."