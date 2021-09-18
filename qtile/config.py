# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "firefox" # My terminal of choice

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod],'p',
             lazy.spawn("/home/rohanj/.config/rofi/bin/launcher_colorful"),
             desc='Run Launcher'
             ),
         Key([mod],'x',
             lazy.spawn("/home/rohanj/.config/rofi/bin/menu_powermenu"),
             desc='Logout Launcher'
             ),

         Key([mod], "w",
             lazy.spawn(myBrowser),
             desc='firefox'
             ),
        Key([mod], "equal",
             lazy.spawn("qalculate-qt"),
             desc='firefox'
             ),

         Key([mod], "space",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "a",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "d",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "t",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "Tab",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         # KeyChord(["control"],"e", [
         #     Key([], "e",
         #         lazy.spawn("emacsclient -c -a 'emacs'"),
         #         desc='Launch Emacs'
         #         ),
         #     Key([], "b",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
         #         desc='Launch ibuffer inside Emacs'
         #         ),
         #     Key([], "d",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
         #         desc='Launch dired inside Emacs'
         #         ),
         #     Key([], "i",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
         #         desc='Launch erc inside Emacs'
         #         ),
         #     Key([], "m",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
         #         desc='Launch mu4e inside Emacs'
         #         ),
         #     Key([], "n",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
         #         desc='Launch elfeed inside Emacs'
         #         ),
         #     Key([], "s",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
         #         desc='Launch the eshell inside Emacs'
         #         ),
         #     Key([], "v",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
         #         desc='Launch vterm inside Emacs'
         #         )
         # ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         # KeyChord([mod], "p", [
         #     Key([], "e",
         #         lazy.spawn("./dmscripts/dm-confedit"),
         #         desc='Choose a config file to edit'
         #         ),
         #     Key([], "i",
         #         lazy.spawn("./dmscripts/dm-maim"),
         #         desc='Take screenshots via dmenu'
         #         ),
         #     Key([], "k",
         #         lazy.spawn("./dmscripts/dm-kill"),
         #         desc='Kill processes via dmenu'
         #         ),
         #     Key([], "l",
         #         lazy.spawn("./dmscripts/dm-logout"),
         #         desc='A logout menu'
         #         ),
         #     Key([], "m",
         #         lazy.spawn("./dmscripts/dm-man"),
         #         desc='Search manpages in dmenu'
         #         ),
         #     Key([], "o",
         #         lazy.spawn("./dmscripts/dm-bookman"),
         #         desc='Search your qutebrowser bookmarks and quickmarks'
         #         ),
         #     Key([], "r",
         #         lazy.spawn("./dmscripts/dm-reddit"),
         #         desc='Search reddit via dmenu'
         #         ),
         #     Key([], "s",
         #         lazy.spawn("./dmscripts/dm-websearch"),
         #         desc='Search various search engines via dmenu'
         #         ),
         #     Key([], "p",
         #         lazy.spawn("passmenu"),
         #         desc='Retrieve passwords with dmenu'
         #         )
         # ])
]

group_names = [("www", {'layout': 'monadtall'}),
               ("dev", {'layout': 'monadtall'}),
               ("dev2", {'layout': 'monadtall'}),
               ("work", {'layout': 'monadtall'}),
               ("work2", {'layout': 'monadtall', 'spawn': ['slack','mailspring']}),
               ("crypt", {'layout': 'monadtall', 'spawn': ['brave']}),
               ("vid", {'layout': 'monadtall', 'spawn': ['chromium https://www.youtube.com/']}),
               ("disc", {'layout': 'monadtall', 'spawn': ['discord']}),
               ("chat", {'layout': 'monadtall', 'spawn': ['whatsapp-nativefier','signal-desktop']}),
               ("vnc", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]
print(groups)

for i, (name, kwargs) in enumerate(group_names, 1):
    if i == 10:
        keys.append(Key([mod], str(0), lazy.group[name].toscreen()))        # Switch to another group
        keys.append(Key([mod, "shift"], str(0), lazy.window.togroup(name))) # Send current window to another group
        break
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 1,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens
COLORS = {
    "black": "#161925",
    "red": "#e06c75",
    "green": "#98c379",
    "yellow": "#e5c07b",
    "blue": "#61afef",
    "magenta": "#c678dd",
    "cyan": "#56b6c2",
    "grey": "#abb2bf",
    "white": "#ffffff",
}
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 14,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Mono",
                       fontsize = 12,
                       margin_y = 4,
                       margin_x = 0,
                       padding_y = 6,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              # widget.Systray(
              #          background = colors[0],
              #          padding = 5
              #          ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = 'AAVE:',
                       foreground = COLORS['red'],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('brave app.aave.com')},
                       padding = 5
                       ),
             widget.GenPollText(
                       func=aave_health,
                       update_interval=3,
                       background= colors[0],
                       foreground= COLORS['red'],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('brave app.aave.com')},
                       fontsize = 12
                       ),
              widget.TextBox(
                       text = '|',
                       foreground = COLORS['red'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.CPU(
                       foreground = COLORS['blue'],
                       background = colors[0],
                       padding = 5
                       ),
              # widget.ThermalSensor(
              #          foreground = colors[2],
              #          background = colors[5],
              #          threshold = 90,
              #          padding = 5
              #          ),
             widget.TextBox(
                       text = "MEM:",
                       foreground = COLORS['blue'],
                       background = colors[0],
                       padding = 3,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = COLORS['blue'],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 0
                       ),
              widget.TextBox(
                       text = '|',
                       foreground = COLORS['blue'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = 'GPU:',
                       padding = 2,
                       foreground = COLORS['green'],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e watch -n0.5 nvidia-smi')},
                       FontsizE = 14
                       ),
            widget.GenPollText(
                       func=get_gpu_usage,
                       update_interval=2,
                       background= colors[0],
                       foreground= COLORS['green'],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e watch -n0.5 nvidia-smi')},
                       fontsize = 14
                       ),
              widget.TextBox(
                       text = 'VMEM:',
                       padding = 2,
                       foreground = COLORS['green'],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e watch -n0.5 nvidia-smi')},
                       fontsize = 14
                       ),
              widget.GenPollText(
                       func=get_gpu_mem_usage,
                       update_interval=2,
                       background= colors[0],
                       foreground= COLORS['green'],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e watch -n0.5 nvidia-smi')},
                       fontsize = 14
                       ),
              widget.TextBox(
                       text = '|',
                       foreground = COLORS['green'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                      text = " VOL:",
                       foreground = COLORS['yellow'],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                       padding = 0
                       ),
              widget.Volume(
                       foreground = COLORS['yellow'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '|',
                       foreground = COLORS['yellow'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.CurrentLayout(
                       foreground = COLORS['magenta'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '|',
                       foreground = COLORS['magenta'],
                       background = colors[0],
                       padding = 5
                       ),
              widget.Clock(
                       foreground = COLORS['cyan'],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('arcolinux-logout')},
                       format = "%A, %B %d - %H:%M "
                       ),
              ]
    return widgets_list


def aave_health():
    aave = subprocess.Popen([''' curl -s "https://api.debank.com/portfolio/list?project_id=matic_aave&user_addr=0x76d71b4b89605cf4875e67e10b02dd0495206aa7" | jq '.data.portfolio_list[0].detail.health_rate'| cut -c -5 '''],stdout=subprocess.PIPE,shell=True)
    (out, err) = aave.communicate()
    return str(out.decode('utf-8').strip('\n'))


def get_gpu_usage():
    gpu = subprocess.Popen(["nvidia-smi --query-gpu=utilization.gpu --format=csv,nounits | awk '/[0-9]/ {print $1}'"],stdout=subprocess.PIPE,shell=True)
    (out, err) = gpu.communicate()
    return str(out.decode('utf-8').strip('\n')) + '%'


def get_gpu_mem_usage():
    gpu = subprocess.Popen([''' nvidia-smi --query-gpu=memory.used,memory.total --format=csv,nounits | awk '/[0-9]/ {printf "%dM/%dM",$1,$2}' '''],stdout=subprocess.PIPE,shell=True)
    (out, err) = gpu.communicate()
    return str(out.decode('utf-8').strip('\n'))


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"