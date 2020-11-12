from tkinter import *
import os

class Window_SRS:  #shutdown restart switch users

    def __init__(self,root):
        self.root=root
        self.root.title("Shutdown Restart Switch-Users")
        self.root.geometry("400x200")
        self.root.iconbitmap("logo881.ico")
        self.root.resizable(0,0)


        def on_enter1(e):
            but_shutdown['background']="black"
            but_shutdown['foreground']="cyan"  
        def on_leave1(e):
            but_shutdown['background']="SystemButtonFace"
            but_shutdown['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_restart['background']="black"
            but_restart['foreground']="cyan"  
        def on_leave2(e):
            but_restart['background']="SystemButtonFace"
            but_restart['foreground']="SystemButtonText"

        def on_enter3(e):
            but_switch_user['background']="black"
            but_switch_user['foreground']="cyan"  
        def on_leave3(e):
            but_switch_user['background']="SystemButtonFace"
            but_switch_user['foreground']="SystemButtonText"


        def shutdown():
            os.system("shutdown /s /t 1")

        def restart():
            os.system("shutdown /r /t 1")

        
        def logout():
            os.system("shutdown -l")


#=============mainframe==============================
        
        mainframe=Frame(self.root,width=400,height=200,relief="ridge",bd=3,bg="gray77")
        mainframe.place(x=0,y=0)


        but_shutdown=Button(mainframe,width=19,text="Shutdown",font=('times new roman',12),cursor="hand2",command=shutdown)
        but_shutdown.place(x=100,y=20)
        but_shutdown.bind("<Enter>",on_enter1)
        but_shutdown.bind("<Leave>",on_leave1)

        but_restart=Button(mainframe,width=19,text="Restart",font=('times new roman',12),cursor="hand2",command=restart)
        but_restart.place(x=100,y=80)
        but_restart.bind("<Enter>",on_enter2)
        but_restart.bind("<Leave>",on_leave2)


        but_switch_user=Button(mainframe,width=19,text="Logout",font=('times new roman',12),cursor="hand2",command=logout)
        but_switch_user.place(x=100,y=140)
        but_switch_user.bind("<Enter>",on_enter3)
        but_switch_user.bind("<Leave>",on_leave3)




if __name__ == "__main__":
    root=Tk()
    app=Window_SRS(root)
    root.mainloop()
