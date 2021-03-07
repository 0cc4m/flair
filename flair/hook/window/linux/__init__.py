"""
 Copyright (C) 2021 0cc4m

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
import os


if os.environ["XDG_SESSION_TYPE"] == "x11":
    from .x11 import get_hwnd, is_foreground, make_foreground, get_screen_coordinates, make_borderless
elif os.environ["XDG_CURRENT_DESKTOP"] == "sway":
    from .sway import get_hwnd, is_foreground, make_foreground, get_screen_coordinates, make_borderless
else:
    raise NotImplementedError("Desktop Environment not supported")
