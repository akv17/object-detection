import cv2
import numpy as np


def create_rect(
    img_height,
    img_width,
    rect_y,
    rect_x,
    rect_height,
    rect_width,
    color=(0, 0, 0)
):
    assert rect_height % 2 != 0
    assert rect_width % 2 != 0
    rect_half_height = rect_height // 2
    rect_half_width = rect_width // 2
    img = np.tile(255, [img_height, img_width])
    img = img.astype(np.uint8)
    top_left = (
        max(0, rect_x - rect_half_width),
        max(0, rect_y - rect_half_height)
    )
    bottom_right = (
        min(img_width - 1, rect_x + rect_half_width),
        min(img_height - 1, rect_y + rect_half_height)
    )
    cv2.rectangle(img, top_left, bottom_right, color, thickness=-1)
    return img
