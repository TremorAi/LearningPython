__author__ = "tremor"

import pytest
from tremorbot import Twitchbot

def test_required_args():
	try:
		test = Twitchbot()
		assert False == True
	except Exception as e:
		assert isinstance(e, Exception)

		