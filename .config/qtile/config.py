"""My configuration for the Qtile Tiling Window Manager."""
#
# -----------
#
# ________      ______               _________
# ___  __ \________  /_______ _____________  /
# __  /_/ /  __ \_  __ \  __ `/_  __ \__ _  /
# _  _, _// /_/ /  / / / /_/ /_  / / / /_/ /
# /_/ |_| \____//_/ /_/\__,_/ /_/ /_/\____/
# -----------
#
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401


from libqtile import qtile, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.popup import Popup
import subprocess
import os

# from libqtile.utils import guess_terminal
from bar_widgets import get_bar_widgets
from bar_widgets import colors


mod = "mod4"
alt_key = "mod1"

my_terminal = "kitty"
myTerm = "kitty"
myBrowser = "firefox"
launch_tmux = "kitty -e tmux -u"
my_browser = "firefox"

# A list of available commands that can be bound to keys can be found
# at https://docs.qtile.org/en/latest/manual/config/lazy.html


def qtile_keys():
    """Qtile function keys."""
    qtile_keys = [
        Key(
            [mod, "control"],
            "r",
            lazy.reload_config(),
            desc="Reload the config",
        ),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ]

    return qtile_keys


def layout_keys():
    """All layout keys."""
    layout_keys = [
        # The essentials
        Key(
            [mod, "control"],
            "space",
            lazy.next_layout(),
            desc="Toggle through layouts",
        ),
        Key(
            [mod, "control", "shift"],
            "space",
            lazy.prev_layout(),
            desc="Toggle through layouts",
        ),
        Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
        Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
        Key(
            [mod, "shift"],
            "s",
            lazy.spawn("flameshot gui"),
            desc="Restart Qtile",
        ),
        Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        # Switch focus to specific monitor (out of three)
        Key([mod], "a", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
        Key([mod], "d", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
        Key(
            [mod],
            "period",
            lazy.next_screen(),
            desc="Move focus to next monitor",
        ),
        Key(
            [mod],
            "comma",
            lazy.prev_screen(),
            desc="Move focus to prev monitor",
        ),
        Key(
            [mod],
            "KP_End",
            lazy.group["one"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Down",
            lazy.group["two"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Page_Down",
            lazy.group["three"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Left",
            lazy.group["four"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Begin",
            lazy.group["five"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Right",
            lazy.group["six"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Home",
            lazy.group["seven"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Up",
            lazy.group["eight"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Page_Up",
            lazy.group["nine"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "KP_Insert",
            lazy.group["ten"].toscreen(1),
            desc="Open num workspace on second monitor",
        ),
        Key(
            [mod],
            "comma",
            lazy.prev_screen(),
            desc="Move focus to prev monitor",
        ),
        # Move between workspaces
        # Treetab controls
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.move_left(),
            desc="Move up a section in treetab",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.move_right(),
            desc="Move down a section in treetab",
        ),
        # Window controls
        Key(
            [mod],
            "h",
            lazy.layout.left(),
            desc="Move focus down in current stack pane",
        ),
        Key(
            [mod],
            "l",
            lazy.layout.right(),
            desc="Move focus down in current stack pane",
        ),
        Key(
            [mod],
            "j",
            lazy.layout.down(),
            desc="Move focus down in current stack pane",
        ),
        Key(
            [mod],
            "k",
            lazy.layout.up(),
            desc="Move focus up in current stack pane",
        ),
        Key(
            [mod, "shift"],
            "j",
            lazy.layout.shuffle_down(),
            lazy.layout.section_down(),
            desc="Move windows down in current stack",
        ),
        Key(
            [mod, "shift"],
            "k",
            lazy.layout.shuffle_up(),
            lazy.layout.section_up(),
            desc="Move windows up in current stack",
        ),
        Key(
            [mod],
            "s",
            lazy.layout.shrink(),
            desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
        ),
        Key(
            [mod],
            "b",
            lazy.layout.grow(),
            desc="Expand window (MonadTall), increase number in master pane (Tile)",
        ),
        Key(
            [mod],
            "m",
            lazy.layout.grow(),
            desc="toggle window between minimum and maximum sizes",
        ),
        Key(
            [mod, "shift"],
            "t",
            lazy.window.toggle_floating(),
            desc="toggle floating",
        ),
        Key(
            [mod],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="toggle fullscreen",
        ),
        ### Stack controls
        Key(
            [mod, "shift"],
            "Tab",
            lazy.layout.rotate(),
            lazy.layout.flip(),
            desc="Switch which side main pane occupies (XmonadTall)",
        ),
        Key(
            [mod],
            "Tab",
            lazy.layout.next(),
            desc="Switch window focus to other pane(s) of stack",
        ),
        Key(
            [mod, "shift"],
            "space",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
    ]

    return layout_keys


def spawn_keys():
    """All spawn keys for lazy."""
    spawn_keys = [
        Key(
            [mod],
            "Return",
            lazy.spawn(launch_tmux),
            desc="Launches My Terminal",
        ),
        Key(
            [mod],
            "t",
            lazy.spawn(my_terminal),
            desc="Launch terminal",
        ),
        Key(
            [mod],
            "F2",
            lazy.spawn("bash /home/rohanj/.config/scripts/audio_change.sh"),
            desc="Turn off screen",
        ),
        Key(
            [mod],
            "F3",
            lazy.spawn("bash /home/rohanj/.config/scripts/screen_off.sh"),
            desc="Turn off screen",
        ),
        Key([mod], "e", lazy.spawn("nautilus -w"), desc="Open File manager"),
        Key(
            [mod],
            "x",
            lazy.spawn("/home/rohanj/.config/rofi/bin/menu_powermenu"),
            desc="Logout Launcher",
        ),
        Key(
            [mod, "shift"],
            "s",
            lazy.spawn("flameshot gui"),
            desc="Screenshot utility",
        ),
        Key(
            [mod],
            "n",
            lazy.spawn("neovide"),
            desc="open neovide",
        ),
        Key(
            [mod, "control"],
            "m",
            lazy.spawn("bash /home/rohanj/.local/bin/mac"),
            desc="open neovide",
        ),
        Key([mod], "equal", lazy.spawn("galculator"), desc="calculator"),
        Key(
            [mod],
            "p",
            lazy.spawn(".config/rofi/bin/launcher_colorful"),
            desc="Prompt",
        ),
        Key(
            [mod, "shift"],
            "e",
            lazy.spawn(".config/rofi/bin/launcher_colorful_emoji"),
            desc="Prompt",
        ),
        Key(
            [mod, "control"],
            "Tab",
            lazy.spawn(".config/rofi/bin/launcher_colorful_win"),
            desc="Prompt",
        ),
        Key(
            [],
            "XF86AudioMute",
            lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
            desc="Mute audio",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
            desc="Reduce volume",
        ),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
            desc="Increase volume",
        ),
        Key(
            [],
            "XF86Calculator",
            lazy.spawn("gnome-calculator -m advanced"),
            desc="Open calculator",
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.spawn("xbacklight -dec 5"),
            desc="Decrease brightness",
        ),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.spawn("xbacklight -inc 5"),
            desc="Increase brightness",
        ),
        KeyChord(
            [mod],
            "w",
            [
                Key([mod], "w", lazy.spawn("firefox"), desc="Launch firefox"),
                Key([mod], "c", lazy.spawn("chromium"), desc="Launch chromium"),
                Key([mod], "b", lazy.spawn("brave"), desc="Launch brave"),
            ],
        ),
    ]

    return spawn_keys


group_names = [
    (
        "one",
        {"layout": "monadtall"},
    ),
    (
        "two",
        {"layout": "monadtall"},
    ),
    ("three", {"layout": "monadtall"}),
    ("four", {"layout": "monadtall"}),
    ("five", {"layout": "monadtall"}),
    ("six", {"layout": "monadtall", "spawn": ["brave"]}),
    ("seven", {"layout": "monadtall", "spawn": ["chromium"]}),
    (
        "eight",
        {"layout": "treetab", "spawn": ["discord", "spotify"]},
    ),
    (
        "nine",
        {
            "layout": "monadtall",
            "spawn": ["signal-desktop", "ferdi"],
            "matches": [Match(wm_class=["ferdi", "signal-desktop"])],
        },
    ),
    (
        "ten",
        {
            "layout": "monadtall",
            "matches": [Match(wm_class=["keepassxc"])],
        },
    ),
]

keys_screen_0 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
keys_screen_1 = [
    "KP_End",
    "KP_Down",
    "KP_Page_Down",
    "KP_Left",
    "KP_Begin",
    "KP_Right",
    "KP_Home",
    "KP_Up",
    "KP_Page_Up",
    "KP_Insert",
]


def group_keys(group_names, keys, screen_number):
    """Keys to access screen groups."""
    group_keys = []
    for i, (name, kwargs) in enumerate(group_names):
        group_keys.append(
            Key(
                [mod],
                keys[i],
                lazy.group[name].toscreen(screen_number),
                lazy.to_screen(screen_number),
                desc=f"Switch to group {name}",
            )
        )  # Switch to another group
        group_keys.append(
            Key(
                [mod, "shift"],
                keys[i],
                lazy.window.togroup(name, switch_group=False),
                desc=f"Send active to window to group {name}",
            )
        )
    group_keys.extend(
        [
            Key([], "F10", lazy.group["scratchpad"].dropdown_toggle("Terminal")),
            Key(
                [],
                "F12",
                lazy.group["scratchpad"].dropdown_toggle("bitwarden"),
            ),
            Key(
                ["control"],
                "1",
                lazy.group["scratchpad"].dropdown_toggle("file-manager"),
            ),
            Key(
                ["control"],
                "2",
                lazy.group["scratchpad"].dropdown_toggle("Terminal"),
            ),
            Key(
                [mod, "shift"],
                "d",
                lazy.screen.next_group(),
                desc="Move to right workspace",
            ),
            Key(
                [mod, "shift"],
                "a",
                lazy.screen.prev_group(),
                desc="Move to left workspace",
            ),
        ]
    )

    return group_keys


keys = [
    *qtile_keys(),
    *layout_keys(),
    *spawn_keys(),
    *group_keys(group_names, keys=keys_screen_0, screen_number=0),
    *group_keys(group_names, keys=keys_screen_1, screen_number=1),
]


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        try:
            desc = k.desc
        except:
            desc = "dummy desc"

        key_help += "{:<30} {}".format(mods, desc + "\n")

    return key_help


pop_obj = Popup(qtile=qtile)


groups = [Group(name, **kwargs) for name, kwargs in group_names]

layout_defaults = {
    "border_width": 1,
    "margin": 8,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}
layouts = [
    layout.MonadTall(**layout_defaults),
    layout.Max(),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200,
    ),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], **layout_defaults),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadWide(**layout_defaults),
    # layout.RatioTile(),
    # layout.Tile(**layout_defaults),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(font="Ubuntu Mono", fontsize=14, padding=2, background=colors[2])
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=get_bar_widgets(primary=True, laptop=False),
    ),
    Screen(
        top=get_bar_widgets(primary=False, laptop=False),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop`
        # to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="gnome-calendar"),  # Calendar app
        Match(wm_class="gnome-calculator"),  # Calculator app
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_defaults,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# To autostart stuff that would normally be in .xinitrc
@hook.subscribe.startup_once
def start_once():
    """Stuff to autostart with qtile."""
    subprocess.call([f"{os.environ['HOME']}/.config/qtile/autostart.sh"])
