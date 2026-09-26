from coaching_site_kit import generate_slots, conflicts
from coaching_site_kit.slots import Slot

def test_slots():
    s = generate_slots(0, 120, 30)
    assert len(s) == 4

def test_conflict():
    assert conflicts(Slot(0, 30), Slot(15, 45))
    assert not conflicts(Slot(0, 30), Slot(30, 60))
