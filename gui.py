import customtkinter as ctk
from main import TO_DO

todo_list = {}
todo = TO_DO(todo_list)


app = ctk.CTk()
app.title("TODO")
app.geometry("630x580")
app.resizable(False, False)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

def clear_frame (frame):
    for child in frame.winfo_children():
        child.destroy()

def remove(Token):
    global todo_list
    if int(Token) in todo_list.keys():
        todo.remove_work(Token)
    else :
        show_dialog("Token notfound")
    clear_frame(task_frame)
    show(todo_list)

def change_status(token):
    taskname = cp_taskname_e.get()
    status = choice.get()
    taskinfo = cp_taskinfo_e.get()
    want_to_change = {"name":False, "status":False, "info":False}
    if token == "":
        show_dialog("please enter the Token")
    else :
        if taskname != "":
            want_to_change["name"] = True
        if taskinfo != "":
            want_to_change["info"] = True
        if status == "finished" or status == "in progress":
            want_to_change["status"] = True        
    return want_to_change

def change(token):
    want_to_change = change_status(token)
    taskname = cp_taskname_e.get()
    status = choice.get()
    taskinfo = cp_taskinfo_e.get()
    if token == "":
        show_dialog("enter Token")
    else :
        if token == "":
            show_dialog("please enter the Token")
        
        if want_to_change["name"] == True:
            todo.change(token, "name", taskname)
        if want_to_change["status"] == True:
            todo.change(token, "status", status)
        if want_to_change["info"] == True:
            todo.change(token, "information", taskinfo)
        
    clear_frame(task_frame)
    show(todo_list)


def make_frame(Token, task_data, task_frame, index):
    name = task_data["name"]
    status = task_data["status"]
    info = task_data["information"]
    my_frame = ctk.CTkFrame(task_frame, fg_color="grey")
    my_frame.grid(row=index, column=0, columnspan=1, sticky="ew", padx=20, pady=10)

    token_l = ctk.CTkLabel(my_frame, text=F"#{Token}")
    token_l.grid(row=0, column=0, padx=20, pady=10)

    name_l = ctk.CTkLabel(my_frame, text=name)
    name_l.grid(row=0, column=1, sticky="e", padx=10, pady=10)

    status_l = ctk.CTkLabel(my_frame, text=status)
    status_l.grid(row=0, column=2, sticky="e", padx=20, pady=10)

    info_l = ctk.CTkLabel(my_frame, text=info)
    info_l.grid(row=0, column=3, sticky="e", padx=20, pady=10)

    del_b = ctk.CTkButton(my_frame, text="Delete", command=lambda token=Token : remove(token), width=20)
    del_b.grid(row=0, column=4, sticky="w", padx=20)
    
    change_b = ctk.CTkButton(my_frame, text="change", command=lambda token=Token : change(token), width=20)
    change_b.grid(row=0, column=5, sticky="w", padx=20)

def show(task_list):
    for index, (token, task) in enumerate(sorted(task_list.items())):
        make_frame(token, task, task_frame, index)
        
def show_dialog(message):
    dialog = ctk.CTkToplevel(app)
    dialog.title("Error")
    dialog.resizable(False, False)
    E_label = ctk.CTkLabel(dialog, text="Error : ", font=ctk.CTkFont(size=30), anchor="center")
    E_label.grid(row=0, column=1, padx=20, pady=10)
    main_l = ctk.CTkLabel(dialog, text=message, font=ctk.CTkFont(size=20), anchor="center")
    main_l.grid(row=1, column=1, padx=20, pady=10)

def add():
    taskname = cp_taskname_e.get()
    #tatus_finished = cp_taskstatus_finisehd.get()
    stattus = choice.get()
    #taskstatus = "finished" if status_finished == 1 else "in progress"
    taskinfo = cp_taskinfo_e.get()
    
    if (taskname != "") and (taskinfo != ""):
        todo.add_work(taskname, stattus, taskinfo)
        clear_frame(task_frame)
        show(todo_list)
    else :
        show_dialog("plase complete entries")


#control pannel
cp_frame = ctk.CTkFrame(app, corner_radius=10)
cp_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

cp_frame.grid_columnconfigure((0, 1, 2), weight=1)

cp_taskname_l = ctk.CTkLabel(cp_frame, text="task name : ", font=ctk.CTkFont(size=20))
cp_taskname_l.grid(row=0, column=0, padx=60, sticky="ew")

cp_taskname_e = ctk.CTkEntry(cp_frame, placeholder_text="task name", height=40, font=ctk.CTkFont(size=15))
cp_taskname_e.grid(row=0, column=1, padx= 20, pady=10)

cp_statuslabel = ctk.CTkLabel(cp_frame, text="task status : ", font=ctk.CTkFont(size=20))
cp_statuslabel.grid(row=1, column=0, padx=30)

choice = ctk.StringVar()

cp_taskstatus_finisehd = ctk.CTkRadioButton(cp_frame, text="finished", hover_color="darkgreen", font=ctk.CTkFont(size=15), variable=choice, value="finished")
cp_taskstatus_finisehd.grid(row=1, column=1, sticky="w", padx=10)

cp_taskstatus_inprogress= ctk.CTkRadioButton(cp_frame, text="in progress", hover_color="darkred", font=ctk.CTkFont(size=15), variable=choice, value="in progress")
cp_taskstatus_inprogress.grid(row=1, column=2, sticky="w")

cp_taskinfo_l = ctk.CTkLabel(cp_frame, text="information : ", font=ctk.CTkFont(size=20))
cp_taskinfo_l.grid(row=2, column=0, sticky="ew", padx=20)

cp_taskinfo_e = ctk.CTkEntry(cp_frame, placeholder_text="task info :", font=ctk.CTkFont(size=15), height=40)
cp_taskinfo_e.grid(row=2, column=1, columnspan=2, sticky="ew", padx=35, pady=20)

cp_btn_add = ctk.CTkButton(cp_frame, command=add, text="add", font=ctk.CTkFont(size=20))
cp_btn_add.grid(row=3, column=0, columnspan=3, sticky="ew", padx=15, pady=20)

task_frame = ctk.CTkScrollableFrame(app, corner_radius=10)
task_frame.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=20)

show(todo_list)

app.mainloop()