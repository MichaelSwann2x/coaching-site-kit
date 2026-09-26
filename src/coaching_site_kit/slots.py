from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Slot:
    start: int
    end: int

def generate_slots(day_start: int, day_end: int, duration: int, step: int | None = None) -> list[Slot]:
    step = step or duration
    slots = []
    t = day_start
    while t + duration <= day_end:
        slots.append(Slot(t, t + duration))
        t += step
    return slots

def conflicts(a: Slot, b: Slot) -> bool:
    return not (a.end <= b.start or b.end <= a.start)
