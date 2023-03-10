import pytest

from jaseci.utils.test_core import CoreTest, jac_testcase
from jaseci.actions.live_actions import load_module_actions, unload_module


class TextParaphraserModule(CoreTest):
    fixture_src = __file__

    @classmethod
    def setUpClass(cls):
        super(TextParaphraserModule, cls).setUpClass()
        ret = load_module_actions("jac_nlp.paraphraser")
        assert ret == True

    @classmethod
    def tearDownClass(cls):
        super(TextParaphraserModule, cls).tearDownClass()
        ret = unload_module("jac_nlp.paraphraser.paraphraser")
        assert ret == True
