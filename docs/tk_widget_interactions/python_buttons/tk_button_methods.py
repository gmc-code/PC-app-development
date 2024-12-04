import tkinter as tk

# Function to list all methods of a Tkinter button
def list_button_methods():
    root = tk.Tk()
    button = tk.Button(root, text="Click Me")
    methods = [method for method in dir(button) if callable(getattr(button, method))]
    root.destroy()
    return methods

# Get the list of methods
button_methods = list_button_methods()

# Print the list of methods
for method in button_methods:
    print(method)


'''
after
after_cancel
after_idle
after_info
anchor
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
clipboard_append
clipboard_clear
clipboard_get
columnconfigure
config
configure
deletecommand
destroy
event_add
event_delete
event_generate
event_info
flash
focus
focus_displayof
focus_force
focus_get
focus_lastfor
focus_set
forget
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
grid_configure
grid_forget
grid_info
grid_location
grid_propagate
grid_remove
grid_rowconfigure
grid_size
grid_slaves
image_names
image_types
info
info_patchlevel
invoke
keys
lift
location
lower
mainloop
nametowidget
option_add
option_clear
option_get
option_readfile
pack
pack_configure
pack_forget
pack_info
pack_propagate
pack_slaves
place
place_configure
place_forget
place_info
place_slaves
propagate
quit
register
rowconfigure
selection_clear
selection_get
selection_handle
selection_own
selection_own_get
send
setvar
size
slaves
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
'''


'''
Unique to Button:
=================

flash
grid_configure
grid_forget
grid_info
grid_remove
info
invoke
location
pack
pack_configure
pack_forget
pack_info
place
place_configure
place_forget
place_info

'''
