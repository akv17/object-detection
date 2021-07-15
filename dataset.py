import cv2
import numpy as np

from data import (
    create_rect as _create_rect_obj,
    Image,
    Sample,
    Dataset
)


def _render_rect(
    arr,
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
    arr_height, arr_width = arr.shape[:2]
    y_min = max(0, rect_y - rect_half_height)
    y_max = min(arr_height - 1, rect_y + rect_half_height)
    x_min = max(0, rect_x - rect_half_width)
    x_max = min(arr_width - 1, rect_x + rect_half_width)
    top_left = (int(x_min), int(y_min))
    bottom_right = (int(x_max), int(y_max))
    cv2.rectangle(arr, top_left, bottom_right, color, thickness=-1)
    obj = _create_rect_obj(
        y_min=y_min,
        y_max=y_max,
        x_min=x_min,
        x_max=x_max,
    )
    return arr, obj


def create_random_image_rect(
    img_height=224,
    img_width=224,
    min_figure_height=None,
    max_figure_height=None,
    min_figure_width=None,
    max_figure_width=None,
    num_figures=1,
    color=(0, 0, 0)
):
    if min_figure_height is None or max_figure_height is None:
        min_figure_height = img_height // 4
        max_figure_height = img_height // 2
    if min_figure_width is None or max_figure_width is None:
        min_figure_width = img_width // 4
        max_figure_width = img_width // 2
    y_min_border = img_height * 0.25
    y_max_border = img_height - y_min_border
    x_min_border = img_width * 0.25
    x_max_border = img_width - x_min_border

    arr = np.tile(255, [img_height, img_width])
    arr = arr.astype(np.uint8)
    img = Image(
        height=img_height,
        width=img_width,
        arr=arr
    )
    for _ in range(num_figures):
        fig_height = np.random.uniform(min_figure_height, max_figure_height)
        fig_width = np.random.uniform(min_figure_width, max_figure_width)
        fig_y = np.random.uniform(y_min_border, y_max_border)
        fig_x = np.random.uniform(x_min_border, x_max_border)
        _, figure = _render_rect(
            arr=img.arr,
            rect_height=fig_height,
            rect_width=fig_width,
            rect_y=fig_y,
            rect_x=fig_x,
            color=color
        )
        img.add_figure(obj=figure)
    return img


def create_dataset(
    num_images=1000,
    img_height=224,
    img_width=224,
    min_figure_height=None,
    max_figure_height=None,
    min_figure_width=None,
    max_figure_width=None,
    num_figures=1,
    color=(0, 0, 0),
):
    samples = []
    for i in range(num_images):
        img = create_random_image_rect(
            img_height=img_height,
            img_width=img_width,
            min_figure_height=min_figure_height,
            max_figure_height=max_figure_height,
            min_figure_width=min_figure_width,
            max_figure_width=max_figure_width,
            num_figures=num_figures,
            color=color,
        )
        sample = Sample(
            id=str(i),
            img=img.arr,
            targets=img.figures['rect']
        )
        samples.append(sample)
    dataset = Dataset(samples)
    return dataset
