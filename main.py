from sys import platform as sys_pf
from SS import *
from tkinter import *
from nltk import FreqDist
from tkinter import messagebox

if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

def search_it():
    """return search result and word cloud
    
    print wordcloud and search results based on the paper titiles
    """
    author_id = get_author_id(str(name.get()))
    for aid in author_id:
        author_paper,paper_detail = get_author_paper(aid)
        paper_detail = str(paper_detail).replace('[','')
        paper_detail = paper_detail.replace(']','')
        paper_detail = paper_detail.replace(',','\r\n')
        # root.option_add("*Dialog.msg.wrapLength", "10i")
        messagebox.showinfo(name.get(), paper_detail) # print the search results by popping out messagebox
        #blank.insert(0, paper_detail)
        token_list = preprocess(author_paper)
        token_freq = FreqDist(token_list)
        wc = WordCloud(background_color="white").generate_from_frequencies(token_freq)
        plt.imshow(wc, interpolation='bilinear') # show wordcloud
        plt.axis("off")
        plt.show()

#end def

# main function to create application form for the engine
root = Tk() # create a now application form
root.title('Semantic Scholar Search Engine') # set app name
root.geometry('640x640+0+0') # set the app window size
heading = Label(root, text='Semantic Scholar Search Engine', font=('arial',30,'bold'), fg='steelblue').pack() # set app head title
label = Label(root, text='Enter the author name:',font=('arial',20,'bold'), fg='black').place(x=10,y=120) # set text label size and title
name = StringVar()
entry_box = Entry(root, textvariable=name, width=18, bg='orange').place(x=260,y=120) # set entry box settings
search = Button(root, text='search', width=10, height=3, bg='blue',command=search_it).place(x=290, y=170) # set search button settings

root.mainloop()
