"""
 Copyright (C) 2020 0cc4m.

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
from typing import Tuple, Union, Optional

from .. import WINDOW_TITLE

from subprocess import check_output, CalledProcessError
import json


def load_window_tree():
    return json.loads(check_output(["swaymsg", "-t", "get_tree"]))


def find_window(name: str, window: dict) -> Optional[dict]:
    """Recursively locate a window with name `name` in the tree, starting at `window`."""
    if window["name"] == name:
        return window
    for child in window["nodes"]:
        val = find_window(name, child)
        if val:
            return val

    for child in window["floating_nodes"]:
        val = find_window(name, child)
        if val:
            return val


def get_hwnd() -> Union[dict, int]:
    """Returns a non-zero window handle to Freelancer if a window exists, otherwise, returns zero."""
    try:
        window = find_window(WINDOW_TITLE, load_window_tree())
        if window:
            return window
    except CalledProcessError:
        pass
    return 0


def is_foreground() -> bool:
    """Reports whether Freelancer is in the foreground and accepting input."""
    try:
        return get_hwnd()["focused"]
    except KeyError:
        return False


def make_foreground():
    """Bring Freelancer's window into the foreground and make it active."""
    raise NotImplementedError


def get_screen_coordinates() -> Tuple[int, int, int, int]:
    """Return the screen coordinates for the contents ("client"; excludes window decorations) of a Freelancer window."""
    hwnd = get_hwnd()
    geo = hwnd['rect']
    left_x = geo['x']
    top_y = geo['y']
    right_x = left_x + geo['width']
    bottom_y = top_y + geo['height']
    return left_x, top_y, right_x, bottom_y


def make_borderless():
    """Remove the borders and titlebar from the game running in windowed mode."""
    raise NotImplementedError
