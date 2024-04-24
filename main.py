import customtkinter as ctk
from openai import OpenAI

# api key
client = OpenAI()

# tkinter setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("EvilGPT")
root.geometry("600x600")


def evil_gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an evil assistant that spreads misinformation"},
            {"role": "user", "content": prompt}
        ]
    )

    answer_text.configure(text=completion.choices[0].message.content)


def clear():
    prompt_entry.delete(0, len(prompt_entry.get()))


# main frame
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# title label
title = ctk.CTkLabel(master=frame, text="EvilGPT", font=("Roboto", 48))
title.pack(pady=12, padx=10)

# prompt section
prompt_frame = ctk.CTkFrame(master=frame, height=100)
prompt_frame.pack(pady=5, padx=10, fill="x")

prompt_entry = ctk.CTkEntry(master=prompt_frame, height=3)
prompt_entry.pack(fill="both")

# submit
submit = ctk.CTkButton(master=frame, text="Submit", command=lambda: evil_gpt(prompt_entry.get()))
submit.pack(pady=5)

clear = ctk.CTkButton(master=frame, text="Clear", command=clear)
clear.pack(pady=5)

answer_frame = ctk.CTkFrame(master=frame)
answer_frame.pack(pady=10, padx=10, fill="both", expand=True)

answer_text = ctk.CTkLabel(master=answer_frame, text="", wraplength=450)
answer_text.pack(pady=12, padx=10)

root.mainloop()
