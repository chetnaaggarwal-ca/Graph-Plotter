import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import  askopenfilename
import tkinter.messagebox
po.init_notebook_mode(connected=True)
cf.go_offline()
root = Tk()


def createdata(data):  # This function is used to check the category of data entered by user
    if data == 1:
        x = np.random.rand(100,
                           5)  # Random.rand is used to create random data it will create data having 100 rows and 5 columns
        df1 = pd.DataFrame(x, columns=['A', 'B', 'C', 'D',
                                       'E'])  # Pandas dataframe will insert the data in the tabular form and columnswill be having name a,b,c,d and e
        labelFrame2 = LabelFrame(text="Your DataFrame head is given below check the columns to plot")
        labelFrame2.grid(column=1, row=15)
        label = Label(labelFrame2, text=df1)
        label.grid(column=4, row=16)
        return df1
    elif data == 2:
        def submit():
            column1 = columnentry.get()
            row1 = row1entry.get()
            row2 = row2entry.get()
            row3 = row3entry.get()
            row4 = row4entry.get()
            list2 = []

            def checkinfo(a):
                a = a.split(" ")
                if len(a) == 5:
                    list2.append(a)
                else:
                    tkinter.messagebox.showerror(title="Incorrect Data",
                                                 message=f"Please enter valid number of {a} !\nValid number is 5")

            list1 = [column1, row1, row2, row3, row4]
            for i in list1:
                checkinfo(i)
            if len(list2) == 5:
                df1 = pd.DataFrame([list2[1], list2[2], list2[3], list2[4]], columns=list2[0])
                labelFrame2 = LabelFrame(
                    text="Your DataFrame head is given below check the columns to plot using cufflinks")
                labelFrame2.grid(column=1, row=15)
                label = Label(labelFrame2, text=df1)
                label.grid(column=4, row=16)

        labelFrame = LabelFrame(text="Enter the data")
        labelFrame.grid(column=1, row=5)
        column_label = Label(labelFrame, text='Column', font=('calibre', 10, 'bold'))
        columnentry = Entry(labelFrame, font=('calibre', 10, 'normal'))
        row1_label = Label(labelFrame, text='Row1', font=('calibre', 10, 'bold'))
        row1entry = Entry(labelFrame, font=('calibre', 10, 'normal'))
        row2_label = Label(labelFrame, text='Row2', font=('calibre', 10, 'bold'))
        row2entry = Entry(labelFrame, font=('calibre', 10, 'normal'))
        row3_label = Label(labelFrame, text='Row3', font=('calibre', 10, 'bold'))
        row3entry = Entry(labelFrame, font=('calibre', 10, 'normal'))
        row4_label = Label(labelFrame, text='Row4', font=('calibre', 10, 'bold'))
        row4entry = Entry(labelFrame, font=('calibre', 10, 'normal'))
        sub_btn = Button(labelFrame, text='Submit', command=submit)
        column_label.grid(row=0, column=1)
        columnentry.grid(row=0, column=2)
        row1_label.grid(row=1, column=1)
        row1entry.grid(row=1, column=2)
        row2_label.grid(row=2, column=1)
        row2entry.grid(row=2, column=2)
        row3_label.grid(row=3, column=1)
        row3entry.grid(row=3, column=2)
        row4_label.grid(row=4, column=1)
        row4entry.grid(row=4, column=2)
        sub_btn.grid(row=5, column=2)
    elif data == 3:
        labelFrame = ttk.LabelFrame(text="Upload a File")
        labelFrame.grid(column=1, row=10)

        def filedialog():
            filename = askopenfilename(initialdir="/", title="Select a file",
                                       filetype=(("csv", "*.csv"), ("json", "*.json"), ("txt", "*.txt")))
            x = pd.read_csv(filename)  # read a csv file
            df1 = pd.DataFrame(x)
            labelFrame2 = LabelFrame(
                text="Your DataFrame head is given below check the columns to plot using cufflinks")
            labelFrame2.grid(column=1, row=15)
            label = Label(labelFrame2, text=df1)
            label.grid(column=4, row=16)
            return df1

        def button1():
            button1 = ttk.Button(labelFrame, text="Browse A File", command=filedialog)
            button1.grid(column=1, row=12)

        button1()


def plotter(plot, a):  # THIS PLOTTER IS FOR Plotting all columns
    if plot == 2:
        finalplot = a.iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
    elif plot == 1:
        finalplot = a.iplot(kind='scatter')
    elif plot == 3:
        finalplot = a.iplot(kind='bar')
    elif plot == 4:
        finalplot = a.iplot(kind='hist')
    elif plot == 5:
        finalplot = a.iplot(kind='box')
    elif plot == 6:
        finalplot = a.iplot(kind='surface')
    labelframe = LabelFrame(text="Graph is as follow")
    labelframe.grid(row=10, column=5)
    label = Label(labelframe, text=finalplot)
    label.grid(row=11, column=5)


def plotter2(plot, a):
    def submit():
        col = int(numentry.get())
        colchoice(plot, col, a)

    labelframe = LabelFrame(text="Enter the number of columns you want to plot")
    labelframe.grid(row=10, column=4)
    num_label = Label(labelframe, text='Enter your choice', font=('calibre', 10, 'bold'))
    numentry = Entry(labelframe, font=('calibre', 10, 'normal'))
    num_label.grid(row=11, column=4)
    numentry.grid(row=11, column=5)
    sub_btn = Button(labelframe, text='Submit', command=submit)
    sub_btn.grid(row=12, column=5)

    def colchoice(plot, col, a):
        if col == 1:
            def submit():
                colm = numentry.get()
                a = colm.split()
                if len(a) == 1:
                    plotter22(colm, a)
                else:
                    tkinter.messagebox.showerror(title="Incorrect Data", message="Enter Valid Data")

            labelframe = LabelFrame(text="Enter the name of column you want to plot by selecting from dataframe head")
            labelframe.grid(row=15, column=4)
            num_label = Label(labelframe, text='Enter your choice', font=('calibre', 10, 'bold'))
            numentry = Entry(labelframe, font=('calibre', 10, 'normal'))
            num_label.grid(row=16, column=4)
            numentry.grid(row=17, column=5)
            sub_btn = Button(labelframe, text='Submit', command=submit)
            sub_btn.grid(row=18, column=5)

            def plotter22(colm, a):
                if plot == 2:
                    finalplot = a[colm].iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
                elif plot == 1:
                    finalplot = a[colm].iplot(kind='scatter')
                elif plot == 3:
                    finalplot = a[colm].iplot(kind='bar')
                elif plot == 4:
                    finalplot = a[colm].iplot(kind='hist')
                elif plot == 5:
                    finalplot = a[colm].iplot(kind='box')
                elif plot == 6 or 7:
                    tkinter.messagebox.showerror(title="Incorrect Data",
                                                 message="Bubble Plot or Surface Plot require more then one column argumnets")

        elif col == 2:
            def submit():
                colm = numentry.get()
                x = colm.split()
                coln = num2entry.get()
                y = coln.split()
                if len(x) == 1 and len(y) == 1:
                    plotter22(colm, coln, a)
                else:
                    tkinter.messagebox.showerror(title="Incorrect Data", message="Enter Valid Data")

            labelframe = LabelFrame(text="Enter the name of columns you want to plot by selecting from dataframe head")
            labelframe.grid(row=15, column=4)
            num_label = Label(labelframe, text='Enter your column 1', font=('calibre', 10, 'bold'))
            numentry = Entry(labelframe, font=('calibre', 10, 'normal'))
            num_label.grid(row=16, column=4)
            numentry.grid(row=17, column=5)
            num2_label = Label(labelframe, text='Enter your column 2', font=('calibre', 10, 'bold'))
            num2entry = Entry(labelframe, font=('calibre', 10, 'normal'))
            num2_label.grid(row=18, column=4)
            num2entry.grid(row=19, column=5)
            sub_btn = Button(labelframe, text='Submit', command=submit)
            sub_btn.grid(row=20, column=5)

            def plotter22(x, y, a):
                if plot == 2:
                    finalplot = df1[x, y].iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
                elif plot == 1:
                    finalplot = df1[x, y].iplot(kind='scatter')
                elif plot == 3:
                    finalplot = df1[x, y].iplot(kind='bar')
                elif plot == 4:
                    finalplot = df1[x, y].iplot(kind='hist')
                elif plot == 5:
                    finalplot = df1[x, y].iplot(kind='box')
                elif plot == 6:
                    finalplot = df1[x, y].iplot(kind='surface')
                elif plot == 7:
                    size = input("Please enter the size of column for Bubble plot")
                    finalplot = df1[x, y].iplot(kind='scatter', x=x, y=y, size=size)
        elif col == 3:
            def submit():
                colm = numentry.get()
                x = colm.split()
                coln = num2entry.get()
                y = coln.split()
                colmz = num3entry.get()
                z = colz.split()
                if len(x) == 1 and len(y) == 1 and len(z) == 1:
                    plotter22(colm, coln, colz, a)
                else:
                    tkinter.messagebox.showerror(title="Incorrect Data", message="Enter Valid Data")

            labelframe = LabelFrame(text="Enter the name of columns you want to plot by selecting from dataframe head")
            labelframe.grid(row=15, column=4)
            num_label = Label(labelframe, text='Enter your column 1', font=('calibre', 10, 'bold'))
            numentry = Entry(labelframe, font=('calibre', 10, 'normal'))
            num_label.grid(row=16, column=4)
            numentry.grid(row=17, column=5)
            num2_label = Label(labelframe, text='Enter your column 2', font=('calibre', 10, 'bold'))
            num2entry = Entry(labelframe, font=('calibre', 10, 'normal'))
            num2_label.grid(row=18, column=4)
            num2entry.grid(row=19, column=5)
            num3_label = Label(labelframe, text='Enter your column 3', font=('calibre', 10, 'bold'))
            num3entry = Entry(labelframe, font=('calibre', 10, 'normal'))
            num3_label.grid(row=20, column=4)
            num3entry.grid(row=21, column=5)
            sub_btn = Button(labelframe, text='Submit', command=submit)
            sub_btn.grid(row=22, column=5)

            def plotter22(x, y, z, a):
                if plot == 2:
                    finalplot = a[x, y, z].iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
                elif plot == 1:
                    finalplot = a[x, y, z].iplot(kind='scatter')
                elif plot == 3:
                    finalplot = a[x, y, z].iplot(kind='bar')
                elif plot == 4:
                    finalplot = a[x, y, z].iplot(kind='hist')
                elif plot == 5:
                    finalplot = a[x, y, z].iplot(kind='box')
                elif plot == 6:
                    finalplot = a[x, y, z].iplot(kind='surface')
                elif plot == 7:
                    size = input("Please enter the size of column for Bubble plot")
                    finalplot = a[x, y, z].iplot(kind='scatter', x=x, y=y, z=z, size=size)

        else:
            tkinter.messagebox.showerror(title="Incorrect Data",
                                         message="Please enter valid number columns between 1 to 3")


def main(cat, a):
    if cat == 1:
        def submit2():
            plot = int(plotentry.get())
            if plot >= 1 and plot <= 6:
                plotter(plot, a)

            else:
                tkinter.messagebox.showerror(title="Incorrect Data", message="Please enter valid number between 1 to 6")

        labelFrame4 = LabelFrame(text="Select the type of plot you want to plot enter number from 1 to 6")
        labelFrame4.grid(row=20, column=1)
        label2 = Label(labelFrame4, text="1. Line Plot")
        label2.grid(row=21, column=2)
        label2 = Label(labelFrame4, text="2. Scatter Plot")
        label2.grid(row=22, column=2)
        label2 = Label(labelFrame4, text="3. Bar Graph")
        label2.grid(row=23, column=2)
        label2 = Label(labelFrame4, text="4. HistoGram")
        label2.grid(row=24, column=2)
        label2 = Label(labelFrame4, text="5. Box Plot")
        label2.grid(row=25, column=2)
        label2 = Label(labelFrame4, text="6. Surface Plot")
        label2.grid(row=26, column=2)
        plot_label = Label(labelFrame4, text='Enter your choice', font=('calibre', 10, 'bold'))
        plotentry = Entry(labelFrame4, font=('calibre', 10, 'normal'))
        sub2_btn = Button(labelFrame4, text='Submit', command=submit2)
        plot_label.grid(row=27, column=1)
        plotentry.grid(row=27, column=2)
        sub2_btn.grid(row=29, column=2)
    elif cat == 2:
        def submit2():
            plot = int(plotentry.get())
            if (plot >= 1) and (plot <= 7):
                plotter2(plot, a)
            else:
                tkinter.messagebox.showerror(title="Incorrect Data", message="Please enter valid number between 1 to 7")

        labelFrame4 = LabelFrame(text="Select the type of plot you want to plot enter number from 1 to 7")
        labelFrame4.grid(row=20, column=1)
        label2 = Label(labelFrame4, text="1. Line Plot")
        label2.grid(row=21, column=2)
        label2 = Label(labelFrame4, text="2. Scatter Plot")
        label2.grid(row=22, column=2)
        label2 = Label(labelFrame4, text="3. Bar Graph")
        label2.grid(row=23, column=2)
        label2 = Label(labelFrame4, text="4. HistoGram")
        label2.grid(row=24, column=2)
        label2 = Label(labelFrame4, text="5. Box Plot")
        label2.grid(row=25, column=2)
        label2 = Label(labelFrame4, text="6. Surface Plot")
        label2.grid(row=26, column=2)
        label2 = Label(labelFrame4, text="7. Bubble Plot")
        label2.grid(row=27, column=2)
        plot_label = Label(labelFrame4, text='Enter your choice', font=('calibre', 10, 'bold'))
        plotentry = Entry(labelFrame4, font=('calibre', 10, 'normal'))
        sub2_btn = Button(labelFrame4, text='Submit', command=submit2)
        plot_label.grid(row=28, column=1)
        plotentry.grid(row=29, column=2)
        sub2_btn.grid(row=30, column=2)


def plottype(a):
    def allcol(event):
        num = 1
        main(num, a)

    def specficcol(event):
        num = 2
        main(num, a)

    labelframe4 = LabelFrame(text="What kind of plot you need ? The complete Data plot or Column plot")
    widget4 = Button(text="For plotting all columns click here", pady=10, padx=78)
    widget4.grid(row=11, column=1)
    widget4.bind('<Button-1>', allcol)
    widget5 = Button(text="For plotting specific columns click here", pady=10, padx=63)
    widget5.grid(row=12, column=1)
    widget5.bind('<Button-1>', specficcol)


def first(event):
    a = createdata(1)
    plottype(a)
    return a


def second(event):
    a = createdata(2)
    plottype(a)
    return a


def third(event):
    a = createdata(3)
    plottype(a)
    return a


root.title("Graph Plotter")
root.geometry("500x500")
Label(text="Welcome To Graph Plotter", font=("comicsans", 19, "bold"), relief=SUNKEN).grid(column=0, row=1)
widget = Button(text="1. To plot Random data with 100 rows and 5 columns", pady=10, padx=20)
widget.grid(row=3, column=0)
widget.bind('<Button-1>', first)
widget2 = Button(text="2. To plot Customize datafile with 5 columns and 4 rows", pady=10, padx=12)
widget2.grid(row=5, column=0)
widget2.bind('<Button-1>', second)

widget3 = Button(text="3. To plot Upload csv/json or text file", pady=10, padx=63)
widget3.grid(row=10, column=0)
widget3.bind('<Button-1>', third)
root.mainloop()