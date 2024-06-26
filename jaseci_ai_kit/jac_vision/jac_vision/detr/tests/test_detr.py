from jaseci.utils.test_core import CoreTest, jac_testcase
from jaseci.jsorc.live_actions import load_module_actions, unload_module


class DETRModule(CoreTest):
    fixture_src = __file__

    @classmethod
    def setUpClass(cls):
        super(DETRModule, cls).setUpClass()
        ret = load_module_actions("jac_vision.detr")
        assert ret == True

    @jac_testcase("detr.jac", "test_detect")
    def test_detect(self, ret):
        self.assertGreaterEqual(len(ret["report"][0]), 1)

    @jac_testcase("detr.jac", "test_detect_batch")
    def test_detect_batch(self, ret):
        self.assertGreaterEqual(len(ret["report"][0][0]), 1)
        self.assertGreaterEqual(len(ret["report"][0][1]), 1)

    @classmethod
    def tearDownClass(cls):
        super(DETRModule, cls).tearDownClass()
        ret = unload_module("jac_vision.detr.detr")
        assert ret == True
