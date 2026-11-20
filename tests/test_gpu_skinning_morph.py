import pytest
from render import gpu_skinning_morph as mod

CASES = [
    ("weights", 'm.weight_normalize((2, 2)) == approx((0.5, 0.5))'),
    ("morph", 'm.morph_apply(1, 2, 0.5) == approx(2.0)'),
    ("quat", 'm.quat_normalize(2, 4) == approx(2.0)'),
    ("tangent", 'm.tangent_scale((2, 0, 0), 2) == (4, 0, 0)'),
    ("barrier", 'm.barrier_required("compute", "draw") is True'),
    ("key", 'm.camera_pose_key("L", 7) == "L:7"'),
    ("blend", 'm.clip_blend(2, 4, 0.5) == approx(3.0)'),
    ("lod", 'm.lod_morph_weight(1, 4) == approx(0.75)'),
    ("root", 'm.strip_root_motion((10, 0), (2, 0)) == (8, 0)'),
    ("bone", 'm.localize_bone((5, 3), (1, 1)) == (4, 2)'),
    ("top4", 'm.top4_sum((1, 2, 3, 4, 5)) == 14'),
    ("order", 'm.morph_layer_order([3, 1, 2]) == [1, 2, 3]'),
    ("hand", 'm.normal_handedness(-1) is True'),
    ("precision", 'm.precision_round(1.2345, 100) == approx(1.23)'),
    ("hash", 'm.pose_hash(["a", "b"]) == "a|b"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
