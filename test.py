fn = 'test_modify.txt'
key_words = 'str - 6'


def write_ref_file():
    with open(fn, 'w') as fid:
        info = ['str - ' + str(i) + '\n' for i in range(10)]
        fid.writelines(info)


def update_file():
    with open(fn, "r+") as fid:
        cursor = 0
        line = fid.readline()
        while line:
            if line.find(key_words) != -1:
                print(key_words)
                print(line)
                # read to end
                rest_part = fid.read()
                # seek to key line
                fid.seek(cursor)
                # delete the rest part
                fid.truncate()
                # update key line
                line += ' '.join([key_words]*5) + '\n'

                fid.write(line)
                fid.write(rest_part)
                break

            cursor = fid.tell() 
            line = fid.readline()

write_ref_file()
update_file()

# def add_devices():
#     # no need to keep our files open while users provide their input
#     code = input("Enter device code: ")
#     amount = int(input("How many devices you are adding: "))
#     # you might want to validate the amount before converting to integer, tho
#     with open("uredjaji.txt", "r+") as f:
#         current_position = 0  # keep track of our current position in the file
#         line = f.readline()  # we need to do it manually for .tell() to work
#         while line:
#             # no need to parse the whole line to check for the code
#             if line[:len(code) + 1] == code + ":":  # code found
#                 remaining_content = f.read()  # read the rest of the file first
#                 f.seek(
#                     current_position)  # seek back to the current line position
#                 f.truncate(
#                 )  # delete the rest of the file, including the current line
#                 line = line.rstrip()  # clear out the whitespace at the end
#                 amount_index = line.rfind(
#                     ":") + 1  # find the amount index position
#                 current_amount = int(line[amount_index:])  # get our amount
#                 # slice out the old amount, replace with the new:
#                 line = line[:amount_index] + str(current_amount +
#                                                  amount) + "\n"
#                 f.write(line)  # write it back to the file
#                 f.write(remaining_content)  # write the remaining content
#                 return  # done!
#             current_position = f.tell()  # cache our current position
#             line = f.readline()  # get the next line
#     print("Invalid device code: {}".format(code))

# ============================================================
# ============================================================
# ============================================================
# ============================================================
# ============================================================
# ============================================================

# import matplotlib.pyplot as plt
# import numpy as np

# import matplotlib
# matplotlib.use('TkAgg')

# x = np.arange(1,10,0.1)
# y = x**2
# z = x**3+5

# plt.ion() #开启interactive mode

# plt.figure(1)
# plt.plot(x,y)   #立即绘制图像1
# # plt.pause(20)    #等待2s但是不会关闭图像1

# plt.figure(2)
# plt.plot(x,z)   #立即绘制图像2
# # plt.pause(2)    #等待2s关闭图像1，2

# plt.ioff()      #关闭interactive mode
# plt.show()      #显示图像1,2并且阻塞程序

# ============================================================
# ============================================================
# ============================================================
# ============================================================
# ============================================================
# ============================================================

# from tkinter import *
# import calendar

# root = Tk()
# # root.geometry("400x300")
# root.title("Calendar")

# # Function

# def text():
#     month_int = int(month.get())
#     year_int = int(year.get())
#     cal = calendar.month(year_int, month_int)
#     textfield.delete(0.0, END)
#     textfield.insert(INSERT, cal)

# # Creating Labels
# label1 = Label(root, text="Month:")
# label1.grid(row=0, column=0)

# label2 = Label(root, text="Year:")
# label2.grid(row=0, column=1)

# # Creating spinbox
# month = Spinbox(root, from_=1, to=12, width=8)
# month.grid(row=1, column=0, padx=5)

# year = Spinbox(root, from_=2000, to=2100, width=10)
# year.grid(row=1, column=1, padx=10)

# # Creating Button
# button = Button(root, text="Go", command=text)
# button.grid(row=1, column=2, padx=10)

# # Creating Textfield
# textfield = Text(root, width=25, height=10, fg="red")
# textfield.grid(row=2, columnspan=2)

# root.mainloop()