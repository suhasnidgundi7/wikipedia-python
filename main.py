from tkinter import*
import wikipedia
from tkinter import messagebox

class SearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wikipedia | By Suhas Nidgundi")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightgrey")

        # ============= Variable =========
        self.var_search = StringVar()

        title = Label(self.root, text="Wiki-xSearch Application", font="calibri 35 bold", bg="#023548", fg="white").place(x=0, y=0, relwidth=1)

        lbl_word = Label(self.root, text="Enter Word : ", font="calibri 30 bold", bg="lightgrey", fg="#262626").place(x=35, y=90)

        txt_word = Entry(self.root, textvariable=self.var_search, font="consolos 20", bg="white").place(x=300, y=100, width=310)

        btn_search = Button(self.root, text="Search", command=self.searchword, font="arial 20 bold", cursor="hand2", bd=0, bg="#0875B7", fg="white").place(x=650, y=98, height=40, width=150)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font="arial 20 bold", cursor="hand2", bd=0, bg="gray", fg="white").place(x=820, y=98, height=40, width=150)
        btn_enable = Button(self.root, text="Enable", command=self.enable, font="arial 20 bold", cursor="hand2", bd=0, bg="#008EA4", fg="white").place(x=990, y=98, height=40, width=150)
        btn_disable = Button(self.root, text="Disable", font="arial 20 bold", cursor="hand2", bd=0, command=self.disable, bg="#DF002A", fg="white").place(x=1160, y=98, height=40, width=150)


        frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="#DF002A")
        frame1.place(x=20, y=190, width=1330, height=500)

        scroll_y = Scrollbar(frame1, orient=VERTICAL)

        self.lbl_mode = Label(self.root, font="calibri 20 bold", bg="lightgrey", fg="yellow")
        self.lbl_mode.place(x=20, y=150)

        scroll_y.pack(side=RIGHT, fill=Y)

        self.txt_area = Text(frame1, bd=3, relief=RIDGE, font="consolos, 15", wrap = WORD, yscrollcommand=scroll_y.set)
        self.txt_area.pack(fill=BOTH, expand=1)

        scroll_y.config(command=self.txt_area.yview)



        self.check_connection()



    def check_connection(self):
        try:
            fetch_data = wikipedia.summary(self.var_search.get())
            print(fetch_data)

        except Exception as ex:
            messagebox.showerror("!!! ERROR 404 !!!", f"!!! ERROR DUE TO : {str(ex)}")



    def enable(self):
        self.txt_area.config(state=NORMAL)
        self.lbl_mode.config(text="MODE: ENABLED", bg="lightgrey", fg="green")

    def disable(self):
        self.txt_area.config(state=DISABLED)
        self.lbl_mode.config(text="MODE: DISABLED", bg="lightgrey", fg="red")

    def searchword(self):
        if self.var_search.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** SEARCH AREA SHOULD NOT BE EMPTY *** !!!")
        else:
            fetch_data = wikipedia.summary(self.var_search.get())
            self.txt_area.insert('1.0', fetch_data)
            self.var_search.set('')


    def clear(self):
        if self.var_search.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** ALL FIELDS ARE REQUIRED *** !!!")
            
        else:
            self.var_search.set('')
            self.txt_area.delete('1.0', END)
    
root = Tk()
obj = SearchApp(root)
root.mainloop()