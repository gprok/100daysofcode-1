from tkinter import Tk, Label, Button, Frame, BOTH, Text, RAISED, Entry
from href import Href

class MillipedeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Crawler")

        master.geometry("500x500")
        mainFrame = Frame(master=master,bg='white')
        mainFrame.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
        mainFrame.pack(fill=BOTH, expand=1) #Expand the frame to fill the root window

        self.label = Label(mainFrame, text="Type a URL")
        self.label.pack()

        # self.urlField = Text(mainFrame, height=1, width=30, borderwidth=1, relief=RAISED)
        self.urlField = Entry(mainFrame)
        self.urlField.pack()

        self.greet_button = Button(mainFrame, text="Crawl", command=self.crawl)
        self.greet_button.pack()

        self.close_button = Button(mainFrame, text="Close", command=master.quit)
        self.close_button.pack()

    def crawl(self):
        hrefs = Href(self.urlField.get())
        domains = hrefs.countHyperlinks()
        for domain in domains:
            print(domain, domains[domain])



def main():
    root = Tk()
    my_gui = MillipedeGUI(root)
    root.mainloop()


if __name__== "__main__":
    main()
