import pytest
import unittest

from jaseci.utils.test_core import CoreTest, jac_testcase
from jaseci.actions.live_actions import load_module_actions, unload_module


class TextParaphraserModule(CoreTest):
    fixture_src = __file__

    @classmethod
    @unittest.skip("Skipping tests")
    def setUpClass(cls):
        super(TextParaphraserModule, cls).setUpClass()
        ret = load_module_actions("jac_nlp.paraphraser")
        assert ret == True

    @pytest.mark.order(1)
    @unittest.skip("Skipping tests")
    @jac_testcase("paraphraser.jac", "test_paraphrase")
    def test_predict(self, ret):
        self.assertEqual(ret["success"], True)

    @classmethod
    @unittest.skip("Skipping tests")
    def tearDownClass(cls):
        super(TextParaphraserModule, cls).tearDownClass()
        ret = unload_module("jac_nlp.paraphraser.paraphraser")
        assert ret == True
