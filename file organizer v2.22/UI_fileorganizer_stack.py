from tkinter import *
from tkinter import ttk
import tkinter.font as TkFont
import json
import os

root = Tk()
root.title('File Organiser V0.1')
root.geometry("1600x730")


#directories with relative paths
dir_source_files = r'sourcefiles'
dir_destination = r'destination'
dir_logfiles = r'logfiles'

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


# Create A Canvas
main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Configure The Canvas
# Add A Scrollbar To the main canvas
main_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
main_scrollbar.pack(side=RIGHT, fill=Y)
main_canvas.configure(yscrollcommand=main_scrollbar.set, scrollregion=main_canvas.bbox("all"))
main_canvas.bind_all('<MouseWheel>', lambda event: main_canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion = main_canvas.bbox("all")))



# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(main_canvas)

# Add that New frame To a Window In The Canvas
main_canvas.create_window((0,0), window=second_frame, anchor="nw")


#font for labels
helv12_bold = TkFont.Font(family="Helvetica",size=12,weight="bold")
font_textbox = TkFont.Font(family="Helvetica",size=9,weight="bold")


# configure the grid
instructions = Label(second_frame,
                     text=" 1. Place your files in the source folder\n 2. Check/Uncheck your sorting options\n 3. Press 'Run File Organizer'",
                     font=(helv12_bold),
                     bd=1, 
                     justify="left")
instructions.grid(column=1, row=5, sticky=W, pady=10, padx=10, ipadx=1, ipady= 10)





#creating a listbox with sourcefiles
label_sourcefiles = Label(second_frame, text=f"Sourcefiles:", font=helv12_bold)
label_sourcefiles.grid(column=1, columnspan=9, row=30, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
listbox_sourcefiles = Listbox(second_frame, width=60, height=30, borderwidth=3)
listbox_sourcefiles.grid(column=1, columnspan=9, row=40, rowspan=100, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=10, columnspan=9, row=40, rowspan=100, sticky=NS)
scrollbar.config(command = listbox_sourcefiles.yview)
listbox_sourcefiles.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=1, columnspan=9, row=140, sticky=EW, padx=(10,0))
scrollbar.config(command = listbox_sourcefiles.xview)
listbox_sourcefiles.config(xscrollcommand=scrollbar.set)


# creating labels and Textboxes with keywords
#textbox 1
label_keywords_text_box_01 = Entry(second_frame, width=40)
label_keywords_text_box_01.grid(column=30, columnspan=9, row=30, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_01.config(background = "white", font = font_textbox)
display_keywords_text_box_01 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_01.grid(column=30, columnspan=9, row=40, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_01.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, columnspan=1, row=40, sticky=NS)
scrollbar.config(command = display_keywords_text_box_01.yview)
display_keywords_text_box_01.config(yscrollcommand=scrollbar.set)

#textbox 2
label_keywords_text_box_02 = Entry(second_frame, width=40)
label_keywords_text_box_02.grid(column=30, columnspan=9, row=60, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_02.config(background = "white", font = font_textbox)
display_keywords_text_box_02 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_02.grid(column=30, columnspan=9, row=70, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_02.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=70, sticky=NS)
scrollbar.config(command = display_keywords_text_box_02.yview)
display_keywords_text_box_02.config(yscrollcommand=scrollbar.set)

#textbox 3
label_keywords_text_box_03 = Entry(second_frame, width=40)
label_keywords_text_box_03.grid(column=30, columnspan=9, row=90, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_03.config(background = "white", font = font_textbox)
display_keywords_text_box_03 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_03.grid(column=30, columnspan=9, row=100, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_03.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=100, sticky=NS)
scrollbar.config(command = display_keywords_text_box_03.yview)
display_keywords_text_box_03.config(yscrollcommand=scrollbar.set)


#textbox 4
label_keywords_text_box_04 = Entry(second_frame, width=40)
label_keywords_text_box_04.grid(column=30, columnspan=9, row=120, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_04.config(background = "white", font = font_textbox)
display_keywords_text_box_04 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_04.grid(column=30, columnspan=9, row=130, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_04.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=130, sticky=NS)
scrollbar.config(command = display_keywords_text_box_04.yview)
display_keywords_text_box_04.config(yscrollcommand=scrollbar.set)

#textbox 5
label_keywords_text_box_05 = Entry(second_frame, width=40)
label_keywords_text_box_05.grid(column=30, columnspan=9, row=150, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_05.config(background = "white", font = font_textbox)
display_keywords_text_box_05 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_05.grid(column=30, columnspan=9, row=160, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_05.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=160, sticky=NS)
scrollbar.config(command = display_keywords_text_box_05.yview)
display_keywords_text_box_05.config(yscrollcommand=scrollbar.set)

#textbox 6
label_keywords_text_box_06 = Entry(second_frame, width=40)
label_keywords_text_box_06.grid(column=30, row=180, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_06.config(background = "white", font = font_textbox)
display_keywords_text_box_06 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_06.grid(column=30, row=190, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_06.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=190, sticky=NS)
scrollbar.config(command = display_keywords_text_box_06.yview)
display_keywords_text_box_06.config(yscrollcommand=scrollbar.set)


#textbox 7
label_keywords_text_box_07 = Entry(second_frame, width=40)
label_keywords_text_box_07.grid(column=30, columnspan=9, row=210, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_07.config(background = "white", font = font_textbox)
display_keywords_text_box_07 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_07.grid(column=30, columnspan=9, row=220, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_07.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=220, sticky=NS)
scrollbar.config(command = display_keywords_text_box_07.yview)
display_keywords_text_box_07.config(yscrollcommand=scrollbar.set)

#textbox 8
label_keywords_text_box_08 = Entry(second_frame, width=40)
label_keywords_text_box_08.grid(column=30, columnspan=9, row=240, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_08.config(background = "white", font = font_textbox)
display_keywords_text_box_08 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_08.grid(column=30, columnspan=9, row=250, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_08.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=250, sticky=NS)
scrollbar.config(command = display_keywords_text_box_08.yview)
display_keywords_text_box_08.config(yscrollcommand=scrollbar.set)

#textbox 9
label_keywords_text_box_09 = Entry(second_frame, width=40)
label_keywords_text_box_09.grid(column=30, columnspan=9, row=270, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_09.config(background = "white", font = font_textbox)
display_keywords_text_box_09 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_09.grid(column=30, columnspan=9, row=280, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_09.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=280, sticky=NS)
scrollbar.config(command = display_keywords_text_box_09.yview)
display_keywords_text_box_09.config(yscrollcommand=scrollbar.set)

#textbox 10
label_keywords_text_box_10 = Entry(second_frame, width=40)
label_keywords_text_box_10.grid(column=30, columnspan=9, row=300, sticky=W, pady=(10,0), padx=25, ipadx=1, ipady= 0)
label_keywords_text_box_10.config(background = "white", font = font_textbox)
display_keywords_text_box_10 = Text(second_frame, width=50, height=5, borderwidth=3)
display_keywords_text_box_10.grid(column=30, columnspan=9, row=310, sticky=W, pady=0, padx=(25,0), ipadx=1, ipady= 1)
display_keywords_text_box_10.config(background = "white", font = font_textbox)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=40, row=310, sticky=NS)
scrollbar.config(command = display_keywords_text_box_10.yview)
display_keywords_text_box_10.config(yscrollcommand=scrollbar.set)



# creating dst listboxes
# listbox 1
dst_folder_name_01 = Label(second_frame, text=f"1")
dst_folder_name_01.grid(column=80, row=30, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_01 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_01.grid(column=80, row=40, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=40, sticky=NS)
scrollbar.config(command = display_files_list_box_01.yview)
display_files_list_box_01.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=50, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_01.xview)
display_files_list_box_01.config(xscrollcommand=scrollbar.set)

# listbox 2
dst_folder_name_02 = Label(second_frame, text=f"2")
dst_folder_name_02.grid(column=80, row=60, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_02 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_02.grid(column=80, row=70, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=70, sticky=NS)
scrollbar.config(command = display_files_list_box_02.yview)
display_files_list_box_02.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=80, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_02.xview)
display_files_list_box_02.config(xscrollcommand=scrollbar.set)

# listbox 3
dst_folder_name_03 = Label(second_frame, text=f"3")
dst_folder_name_03.grid(column=80, row=90, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_03 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_03.grid(column=80, row=100, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=100, sticky=NS)
scrollbar.config(command = display_files_list_box_03.yview)
display_files_list_box_03.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=110, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_03.xview)
display_files_list_box_03.config(xscrollcommand=scrollbar.set)


# listbox 4
dst_folder_name_04 = Label(second_frame, text=f"4")
dst_folder_name_04.grid(column=80, row=120, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_04 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_04.grid(column=80, row=130, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=130, sticky=NS)
scrollbar.config(command = display_files_list_box_04.yview)
display_files_list_box_04.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=140, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_04.xview)
display_files_list_box_04.config(xscrollcommand=scrollbar.set)


# listbox 5
dst_folder_name_05 = Label(second_frame, text=f"5")
dst_folder_name_05.grid(column=80, row=150, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_05 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_05.grid(column=80, row=160, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=160, sticky=NS)
scrollbar.config(command = display_files_list_box_05.yview)
display_files_list_box_05.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=170, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_05.xview)
display_files_list_box_05.config(xscrollcommand=scrollbar.set)


# listbox 6
dst_folder_name_06 = Label(second_frame, text=f"6")
dst_folder_name_06.grid(column=80, row=180, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_06 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_06.grid(column=80, row=190, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=190, sticky=NS)
scrollbar.config(command = display_files_list_box_06.yview)
display_files_list_box_06.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=200, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_06.xview)
display_files_list_box_06.config(xscrollcommand=scrollbar.set)

# listbox 7
dst_folder_name_07 = Label(second_frame, text=f"7")
dst_folder_name_07.grid(column=80, row=210, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_07 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_07.grid(column=80, row=220, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=220, sticky=NS)
scrollbar.config(command = display_files_list_box_07.yview)
display_files_list_box_07.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=230, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_07.xview)
display_files_list_box_07.config(xscrollcommand=scrollbar.set)


# listbox 8
dst_folder_name_08 = Label(second_frame, text=f"8")
dst_folder_name_08.grid(column=80, row=240, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_08 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_08.grid(column=80, row=250, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=250, sticky=NS)
scrollbar.config(command = display_files_list_box_08.yview)
display_files_list_box_08.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=260, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_08.xview)
display_files_list_box_08.config(xscrollcommand=scrollbar.set)


# listbox 9
dst_folder_name_09 = Label(second_frame, text=f"9")
dst_folder_name_09.grid(column=80, row=270, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_09 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_09.grid(column=80, row=280, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=280, sticky=NS)
scrollbar.config(command = display_files_list_box_09.yview)
display_files_list_box_09.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=290, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_09.xview)
display_files_list_box_09.config(xscrollcommand=scrollbar.set)


# listbox 10
dst_folder_name_10 = Label(second_frame, text=f"10")
dst_folder_name_10.grid(column=80, row=300, sticky=W, pady=(10,0), padx=10, ipadx=1, ipady= 0)
display_files_list_box_10 = Listbox(second_frame, width=60, height=5, borderwidth=3)
display_files_list_box_10.grid(column=80, row=310, sticky=W, pady=0, padx=(10,0), ipadx=1, ipady= 1)
scrollbar = Scrollbar(second_frame)
scrollbar.grid(column=90, row=310, sticky=NS)
scrollbar.config(command = display_files_list_box_10.yview)
display_files_list_box_10.config(font = (font_textbox), 
                             yscrollcommand=scrollbar.set)
scrollbar = Scrollbar(second_frame, orient = 'horizontal')
scrollbar.grid(column=80, row=320, sticky=EW, padx=(10,0))
scrollbar.config(command = display_files_list_box_10.xview)
display_files_list_box_10.config(xscrollcommand=scrollbar.set)


def save_content_textboxes():
    dict_textBox_01={label_keywords_text_box_01.get(): display_keywords_text_box_01.get('1.0','end-1c')}
    dict_textBox_02={label_keywords_text_box_02.get(): display_keywords_text_box_02.get('1.0','end-1c')}
    dict_textBox_03={label_keywords_text_box_03.get(): display_keywords_text_box_03.get('1.0','end-1c')}
    dict_textBox_04={label_keywords_text_box_04.get(): display_keywords_text_box_04.get('1.0','end-1c')}
    dict_textBox_05={label_keywords_text_box_05.get(): display_keywords_text_box_05.get('1.0','end-1c')}
    dict_textBox_06={label_keywords_text_box_06.get(): display_keywords_text_box_06.get('1.0','end-1c')}
    dict_textBox_07={label_keywords_text_box_07.get(): display_keywords_text_box_07.get('1.0','end-1c')}
    dict_textBox_08={label_keywords_text_box_08.get(): display_keywords_text_box_08.get('1.0','end-1c')}
    dict_textBox_09={label_keywords_text_box_09.get(): display_keywords_text_box_09.get('1.0','end-1c')}
    dict_textBox_10={label_keywords_text_box_10.get(): display_keywords_text_box_10.get('1.0','end-1c')}
    list_of_dict_textBoxes =[dict_textBox_01, dict_textBox_02, dict_textBox_03, dict_textBox_04, dict_textBox_05,
                             dict_textBox_06, dict_textBox_07, dict_textBox_08, dict_textBox_09, dict_textBox_10]
    json_content = json.dumps(list_of_dict_textBoxes)
    with open("saved keywords raw.json", "w") as outfile:
        outfile.write(json_content)    

    dict_textBoxes = {
        label_keywords_text_box_01.get(): display_keywords_text_box_01.get('1.0','end-1c'),
        label_keywords_text_box_02.get(): display_keywords_text_box_02.get('1.0','end-1c'),
        label_keywords_text_box_03.get(): display_keywords_text_box_03.get('1.0','end-1c'),
        label_keywords_text_box_04.get(): display_keywords_text_box_04.get('1.0','end-1c'),
        label_keywords_text_box_05.get(): display_keywords_text_box_05.get('1.0','end-1c'),
        label_keywords_text_box_06.get(): display_keywords_text_box_06.get('1.0','end-1c'),
        label_keywords_text_box_07.get(): display_keywords_text_box_07.get('1.0','end-1c'),
        label_keywords_text_box_08.get(): display_keywords_text_box_08.get('1.0','end-1c'),
        label_keywords_text_box_09.get(): display_keywords_text_box_09.get('1.0','end-1c'),
        label_keywords_text_box_10.get(): display_keywords_text_box_10.get('1.0','end-1c'),
        }    
    with open("saved keywords raw.json") as infile:
        dicts_textBoxes_CLEAN = {}    
        data = json.load(infile)
        for entry in data:
            for key_raw, value_raw in entry.items():
                if key_raw == "":
                    break
                value_raw.replace("\\t", "").replace("\\n", "").replace("\\r", "")
                value_raw = "".join(value_raw.split("\n"))
                value_raw = "".join(value_raw.split("\t"))
                value_raw = "".join(value_raw.split("\r"))
                dicts_textBoxes_CLEAN[key_raw] = value_raw
        json_content = json.dumps(dicts_textBoxes_CLEAN, indent = 4)
        with open("saved keywords clean.json", "w") as outfile:
            outfile.write(json_content)


def display_dst_listboxes():    
    json_object_open = open("saved keywords clean.json")
    saved_keywords_clean_json = json.load(json_object_open)
    list_of_dicts_dstFolderNames_and_keywords = []
    list_seen_sourcefiles = []
    list_seen_sourcefiles_and_matching_keywords = []
    for key, value in saved_keywords_clean_json.items():
        dict_dstFolder_and_keywords = {key:value}
        list_of_dicts_dstFolderNames_and_keywords.append(dict_dstFolder_and_keywords)
    print("List of dictionaries with Foldernames and Keywords generated, here is the list:")
    print(str(list_of_dicts_dstFolderNames_and_keywords))
    print("")
    print("Now iterating through the list of dictionaries from textboxes")
    
    try:
        for dstFolderName, keywords_with_hashtags in list_of_dicts_dstFolderNames_and_keywords[0].items():
            list_unseenSrcFiles_and_therefore_to_be_moved = []
            for sourcefile in os.scandir(dir_source_files):
                if sourcefile in list_seen_sourcefiles:
                    print(f"file {sourcefile.name} was already seen")
                    continue
                else:
                    keywords_without_hashtags = keywords_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                    keywords_without_hashtags.remove('') #removes empty entries from list
                    keywords_without_hashtags
                    for keyword in keywords_without_hashtags:
                        keyword=keyword.rstrip()
                        if keyword.lower() in sourcefile.name.lower():
                            print(f"keyword '{keyword}' found in sourcefile '{sourcefile.name}'")
                            list_seen_sourcefiles.append(sourcefile)
                            list_seen_sourcefiles_and_matching_keywords.append("#" + keyword + ": " + sourcefile.name)
                            list_seen_sourcefiles=list(set(list_seen_sourcefiles))
                            list_unseenSrcFiles_and_therefore_to_be_moved.append(sourcefile)
            print(f"the following files will be moved:")
            print(list_unseenSrcFiles_and_therefore_to_be_moved)
            dst_folder_name_01.config(text=dstFolderName)
            display_files_list_box_01.delete(0,END)
            for sourcefile_to_be_moved in list_unseenSrcFiles_and_therefore_to_be_moved:
                print(f"Willl move {sourcefile_to_be_moved} to destination folder")
            for sourcefile_name_and_matching_keyword in list_seen_sourcefiles_and_matching_keywords:
                display_files_list_box_01.insert(END, sourcefile_name_and_matching_keyword)
    except IndexError:
            pass
    
    try:
        for dstFolderName, keywords_with_hashtags in list_of_dicts_dstFolderNames_and_keywords[1].items():
            list_unseenSrcFiles_and_therefore_to_be_moved = []
            for sourcefile in os.scandir(dir_source_files):
                if sourcefile in list_seen_sourcefiles:
                    print(f"file {sourcefile.name} was already seen")
                    continue
                else:
                    keywords_without_hashtags = keywords_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                    keywords_without_hashtags.remove('') #removes empty entries from list
                    keywords_without_hashtags
                    for keyword in keywords_without_hashtags:
                        keyword=keyword.rstrip()
                        if keyword.lower() in sourcefile.name.lower():
                            print(f"keyword '{keyword}' found in sourcefile '{sourcefile.name}'")
                            list_seen_sourcefiles.append(sourcefile)
                            list_seen_sourcefiles=list(set(list_seen_sourcefiles))
                            list_unseenSrcFiles_and_therefore_to_be_moved.append(sourcefile)
            print(f"the following files will be moved:")
            print(list_unseenSrcFiles_and_therefore_to_be_moved)
            display_files_list_box_02.delete(0,END)
            for sourcefile_name in list_unseenSrcFiles_and_therefore_to_be_moved:
                display_files_list_box_02.insert(END, sourcefile_name.name)
    except IndexError:
            pass
        
    try:
        for dstFolderName, keywords_with_hashtags in list_of_dicts_dstFolderNames_and_keywords[2].items():
            list_unseenSrcFiles_and_therefore_to_be_moved = []
            for sourcefile in os.scandir(dir_source_files):
                if sourcefile in list_seen_sourcefiles:
                    print(f"file {sourcefile.name} was already seen")
                    continue
                else:
                    keywords_without_hashtags = keywords_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                    keywords_without_hashtags.remove('') #removes empty entries from list
                    keywords_without_hashtags
                    for keyword in keywords_without_hashtags:
                        keyword=keyword.rstrip()
                        if keyword.lower() in sourcefile.name.lower():
                            print(f"keyword '{keyword}' found in sourcefile '{sourcefile.name}'")
                            list_seen_sourcefiles.append(sourcefile)
                            list_seen_sourcefiles=list(set(list_seen_sourcefiles))
                            list_unseenSrcFiles_and_therefore_to_be_moved.append(sourcefile)
            print(f"the following files will be moved:")
            print(list_unseenSrcFiles_and_therefore_to_be_moved)
            display_files_list_box_03.delete(0,END)
            for sourcefile_name in list_unseenSrcFiles_and_therefore_to_be_moved:
                display_files_list_box_03.insert(END, sourcefile_name.name)
    except IndexError:
            pass
        
            
    try:
        for dstFolderName, keywords_with_hashtags in list_of_dicts_dstFolderNames_and_keywords[3].items():
            list_unseenSrcFiles_and_therefore_to_be_moved = []
            for sourcefile in os.scandir(dir_source_files):
                if sourcefile in list_seen_sourcefiles:
                    print(f"file {sourcefile.name} was already seen")
                    continue
                else:
                    keywords_without_hashtags = keywords_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                    keywords_without_hashtags.remove('') #removes empty entries from list
                    keywords_without_hashtags
                    for keyword in keywords_without_hashtags:
                        keyword=keyword.rstrip()
                        if keyword.lower() in sourcefile.name.lower():
                            print(f"keyword '{keyword}' found in sourcefile '{sourcefile.name}'")
                            list_seen_sourcefiles.append(sourcefile)
                            list_seen_sourcefiles=list(set(list_seen_sourcefiles))
                            list_unseenSrcFiles_and_therefore_to_be_moved.append(sourcefile)
            print(f"the following files will be moved:")
            print(list_unseenSrcFiles_and_therefore_to_be_moved)
            display_files_list_box_04.delete(0,END)
            for sourcefile_name in list_unseenSrcFiles_and_therefore_to_be_moved:
                display_files_list_box_04.insert(END, sourcefile_name.name)
    except IndexError:
            pass






# Get State functions
def get_state_extract_from_folders():
    if state_extract_boolean.get():
        print("Extract files from folders is set TRUE")
        return(True)
    if not state_extract_boolean.get():
        print("Extract files from folders is set FALSE")
        return(False)

def get_state_delete_emptyFolders():
    if state_delete_boolean.get():
        print("Delete empty folders after moving files is set TRUE")
        return(True)
    if not state_delete_boolean.get():
        print("Delete empty folders after moving files is set FALSE")
        return(False)
        
state_extract_boolean=IntVar()
Checkbutton(second_frame, text = "Extract files\n from parentfolders", variable=state_extract_boolean, onvalue=1, 
            offvalue=0, command=get_state_extract_from_folders).grid(column=30, columnspan=1, row=5, sticky=W, padx=(10,0), ipadx=10, ipady= 10)

state_delete_boolean=IntVar()
Checkbutton(second_frame, text = "Delete\nempty folders", variable=state_delete_boolean, onvalue=1, 
            offvalue=0, command=get_state_delete_emptyFolders).grid(column=35, columnspan=1, row=5, sticky=W, padx=(10,0), ipadx=10, ipady= 10)


button_check_for_keywords = Button(second_frame,
                               text = "Match Keywords",
                               bg = "lightblue",
                               font= ('Arial 12'),
                               command = lambda:[
                                   save_content_textboxes(),
                                   display_dst_listboxes(),
                                   print("button_check_for_keywords pressed")
                                   ]
                               )
button_check_for_keywords.grid(column=1, row=10, sticky=W, padx=(10,0), pady=(10,10), ipadx=10, ipady=10)


button_Run_File_Organizer = Button(second_frame,
                               text = "Run File Organizer",
                               font= ('Arial 12'),
                               command = lambda:[
                                   get_state_extract_from_folders(),
                                   get_state_delete_emptyFolders(),
                                   #create_folders_and_move_files()
                                   ]
                               )
button_Run_File_Organizer.grid(column=1, row=1, sticky=W, padx=(10,0), pady=(10,10), ipadx=10, ipady=10)


# The setup - filling the textboxes at the start
for sourcefile in os.scandir(dir_source_files):
    listbox_sourcefiles.insert(END,sourcefile.name)

try:
    json_object_open = open("saved keywords raw.json")
    json_object_data = json.load(json_object_open)
    for key_textbox_label, value_textbox_keywords in json_object_data[0].items():
        label_keywords_text_box_01.insert(END,key_textbox_label)
        display_keywords_text_box_01.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[1].items():
        label_keywords_text_box_02.insert(END,key_textbox_label)
        display_keywords_text_box_02.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[2].items():
        label_keywords_text_box_03.insert(END,key_textbox_label)
        display_keywords_text_box_03.insert(END,value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[3].items():
        label_keywords_text_box_04.insert(END,key_textbox_label)
        display_keywords_text_box_04.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[4].items():
        label_keywords_text_box_05.insert(END,key_textbox_label)
        display_keywords_text_box_05.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[5].items():
        label_keywords_text_box_06.insert(END,key_textbox_label)
        display_keywords_text_box_06.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[6].items():
        label_keywords_text_box_07.insert(END,key_textbox_label)
        display_keywords_text_box_07.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[7].items():
        label_keywords_text_box_08.insert(END,key_textbox_label)
        display_keywords_text_box_08.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[8].items():
        label_keywords_text_box_09.insert(END,key_textbox_label)
        display_keywords_text_box_09.insert(END, value_textbox_keywords)
    for key_textbox_label, value_textbox_keywords in json_object_data[9].items():
        label_keywords_text_box_10.insert(END,key_textbox_label)
        display_keywords_text_box_10.insert(END, value_textbox_keywords)
except ValueError:
    pass










root.mainloop()