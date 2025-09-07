from usesful_funcs import *

def page_show_info(mainroot, list_frame, main_frame):
    mainroot.change_frame(list_frame)
    f = tk.Frame(list_frame, width=500, height=100)
    f.pack_propagate(False)
    f.pack()
