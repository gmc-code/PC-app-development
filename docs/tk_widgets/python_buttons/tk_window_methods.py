import tkinter as tk

# Function to list all methods of a Tkinter widget
def list_methods(widget):
    return [method for method in dir(widget) if callable(getattr(widget, method))]

# Initialize Tkinter root
root = tk.Tk()

# Get methods of Tk window and Button widget
tk_methods = list_methods(root)
button_methods = list_methods(tk.Button(root))

# Compare methods to find common and unique methods
common_methods = set(tk_methods).intersection(button_methods)
unique_to_tk = set(tk_methods) - common_methods
unique_to_button = set(button_methods) - common_methods

# Close the Tkinter root
window.destroy()

# Format output as reStructuredText
output_rst = f"""
Methods in Tk (root):
=====================
{', '.join(sorted(tk_methods))}

Methods in Button:
==================
{', '.join(sorted(button_methods))}

Common Methods:
===============
{', '.join(sorted(common_methods))}

Unique to Tk (root):
====================
{', '.join(sorted(unique_to_tk))}

Unique to Button:
=================
{', '.join(sorted(unique_to_button))}
"""

# Print the result
print(output_rst)



'''
after
after_cancel
after_idle
after_info
anchor
aspect
attributes
bbox
bell
bind
bind_all
bind_class
bindtags
busy
busy_cget
busy_config
busy_configure
busy_current
busy_forget
busy_hold
busy_status
cget
client
clipboard_append
clipboard_clear
clipboard_get
colormapwindows
columnconfigure
command
config
configure
deiconify
deletecommand
destroy
event_add
event_delete
event_generate
event_info
focus
focus_displayof
focus_force
focus_get
focus_lastfor
focus_set
focusmodel
forget
frame
geometry
getboolean
getdouble
getint
getvar
grab_current
grab_release
grab_set
grab_set_global
grab_status
grid
grid_anchor
grid_bbox
grid_columnconfigure
grid_location
grid_propagate
grid_rowconfigure
grid_size
grid_slaves
group
iconbitmap
iconify
iconmask
iconname
iconphoto
iconposition
iconwindow
image_names
image_types
info_patchlevel
keys
lift
loadtk
lower
mainloop
manage
maxsize
minsize
nametowidget
option_add
option_clear
option_get
option_readfile
overrideredirect
pack_propagate
pack_slaves
place_slaves
positionfrom
propagate
protocol
quit
readprofile
register
report_callback_exception
resizable
rowconfigure
selection_clear
selection_get
selection_handle
selection_own
selection_own_get
send
setvar
size
sizefrom
slaves
state
title
tk_bisque
tk_busy
tk_busy_cget
tk_busy_config
tk_busy_configure
tk_busy_current
tk_busy_forget
tk_busy_hold
tk_busy_status
tk_focusFollowsMouse
tk_focusNext
tk_focusPrev
tk_setPalette
tk_strictMotif
tkraise
transient
unbind
unbind_all
unbind_class
update
update_idletasks
wait_variable
wait_visibility
wait_window
waitvar
winfo_atom
winfo_atomname
winfo_cells
winfo_children
winfo_class
winfo_colormapfull
winfo_containing
winfo_depth
winfo_exists
winfo_fpixels
winfo_geometry
winfo_height
winfo_id
winfo_interps
winfo_ismapped
winfo_manager
winfo_name
winfo_parent
winfo_pathname
winfo_pixels
winfo_pointerx
winfo_pointerxy
winfo_pointery
winfo_reqheight
winfo_reqwidth
winfo_rgb
winfo_rootx
winfo_rooty
winfo_screen
winfo_screencells
winfo_screendepth
winfo_screenheight
winfo_screenmmheight
winfo_screenmmwidth
winfo_screenvisual
winfo_screenwidth
winfo_server
winfo_toplevel
winfo_viewable
winfo_visual
winfo_visualid
winfo_visualsavailable
winfo_vrootheight
winfo_vrootwidth
winfo_vrootx
winfo_vrooty
winfo_width
winfo_x
winfo_y
withdraw
wm_aspect
wm_attributes
wm_client
wm_colormapwindows
wm_command
wm_deiconify
wm_focusmodel
wm_forget
wm_frame
wm_geometry
wm_grid
wm_group
wm_iconbitmap
wm_iconify
wm_iconmask
wm_iconname
wm_iconphoto
wm_iconposition
wm_iconwindow
wm_manage
wm_maxsize
wm_minsize
wm_overrideredirect
wm_positionfrom
wm_protocol
wm_resizable
wm_sizefrom
wm_state
wm_title
wm_transient
wm_withdraw
'''
