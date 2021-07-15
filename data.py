from dataclasses import dataclass, field
from typing import Any


@dataclass
class Rect:
    y_min: float
    y_max: float
    x_min: float
    x_max: float
    height: float
    width: float
    y_center: float
    x_center: float

    def as_tuple(self):
        return self.y_min, self.y_max, self.x_min, self.x_max


def create_rect(y_min, y_max, x_min, x_max):
    height = y_max - y_min
    width = x_max - x_min
    y_center = (y_max + y_min) / 2
    x_center = (x_max + x_min) / 2
    obj = Rect(
        y_min=int(y_min),
        y_max=int(y_max),
        x_min=int(x_min),
        x_max=int(x_max),
        y_center=int(y_center),
        x_center=int(x_center),
        height=int(height),
        width=int(width),
    )
    return obj


@dataclass
class Image:
    height: float
    width: float
    arr: Any = field(repr=False)
    figures: Any = field(repr=False, default_factory=dict)

    def add_figure(self, name, obj):
        self.figures.setdefault(name, []).append(obj)
