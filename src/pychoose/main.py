import secrets

import customtkinter as ctk

ctk.set_appearance_mode('black')
ctk.set_default_color_theme('blue')


class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, master, choice_num, **kwargs):
        super().__init__(master, **kwargs)
        self.pack_propagate(False)

        self.label_choice = ctk.CTkLabel(self, text=f"Choice {choice_num}", height=50)
        self.text_choice = ctk.CTkTextbox(self, height=300)

        self.label_choice.pack(expand=True, fill="both")
        self.text_choice.pack(expand=True, fill="both")


        self.text_choice.bind("<Control-a>", self.select_all)
        self.text_choice.bind("<Control-A>", self.select_all)

    def select_all(self, event):
        event.widget.tag_add('sel', '1.0', 'end')
        return 'break'


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x800')
        self.title("pychoose")
        self.configure(fg_color="#FF9F50")

        self.label_app_name = ctk.CTkLabel(self, text="pychoose", text_color="white", font=("Arial", 20, "bold"))

        self.frame_choices = ctk.CTkFrame(self)
        self.frame_choice1 = ChoiceFrame(master=self.frame_choices, fg_color="#5076FF", choice_num=1, width=375, height=350)
        self.frame_choice2 = ChoiceFrame(master=self.frame_choices, fg_color="#5979FF", choice_num=2, width=375, height=350)

        self.frame_buttons = ctk.CTkFrame(self)
        self.button_choose = ctk.CTkButton(self.frame_buttons, text="Choose", command=self.choose)
        self.button_reset = ctk.CTkButton(self.frame_buttons, text="Reset", command=self.reset)

        self.label_app_name.pack(side="top", pady=5)
        self.frame_buttons.pack(side="bottom", pady=5)

        self.button_choose.pack(side="left", padx=10, pady=5)
        self.button_reset.pack(side="right", padx=10, pady=5)

        self.frame_choices.pack(expand=True, padx=20, pady=20)
        self.frame_choice1.pack(side="left", expand=True, padx=5, pady=5)
        self.frame_choice2.pack(side="right", expand=True, padx=5, pady=5)

        self.bind("<Key>", self.reset_colors)

    def choose(self):
        choices = [self.frame_choice1, self.frame_choice2]
        secrets.SystemRandom().shuffle(choices)
    
        choice = choices[0]
        non_choice = choices[1]

        choice.configure(fg_color="green")
        non_choice.configure(fg_color="red")

    def reset_colors(self, event="<Key>"):
        self.frame_choice1.configure(fg_color="#5076FF")
        self.frame_choice2.configure(fg_color="#5979FF")

    def reset(self):
        self.reset_colors(self)
        self.frame_choice1.text_choice.delete("1.0", "end")
        self.frame_choice2.text_choice.delete("1.0", "end")
        
def main():
    app = App()
    app.mainloop()
    

if __name__ == "__main__":
    main()
