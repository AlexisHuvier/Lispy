import webbrowser
from lispy.error import lispy_function


@lispy_function("webbrowser:open", ["str"], "Open url in default browser")
def webbrowser_open(args):
    webbrowser.open(args[0])

@lispy_function("webbrowser:openwindow", ["str"], "Open url in new window of default browser")
def webbrowser_openwindow(args):
    webbrowser.open_new(args[0])

@lispy_function("webbrowser:opentab", ["str"], "Open url in new tab of default browser")
def webbrowser_opentab(args):
    webbrowser.open_new_tab(args[0])