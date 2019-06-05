import tkinter as tk
from bs4 import BeautifulSoup
import requests


class HinduInshorts(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title('Hindu Inshorts..')
        #canvas = tk.Canvas(self, height = 500, width = 600 )
        #canvas.pack()
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Front_page, Sports_page, Business_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
    def news_section(self,section_in):
        
        source = requests.get('https://www.thehindu.com/todays-paper/').text
        soup = BeautifulSoup(source,'lxml')
        section = soup.find('div', class_='tpaper-container')
        news = []
        for category in section.find_all('a'):
            
            if category.text == section_in :
        
                link = category['href']
                category_source = requests.get(link).text
                category_soup = BeautifulSoup(category_source,'lxml')
    
        
                headlines = category_soup.find('div', class_='section-container')
                for lines in headlines.find_all('a'):
                    try:
                        news.append(lines.text)
        
                    except Exception as e :
                        print('****error loading data****moving to next feed..')
        return news

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Welcome to Hindu Inshorts. Please select a Category.', font=40)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text='Front Page',font=40,activebackground='#27AE60',bg='#000000',fg='#FFFFFF',
                            width = 15, command=lambda: controller.show_frame("Front_page"))
        label1 = tk.Label(self)
        label2 = tk.Label(self)
        
        button2 = tk.Button(self, text='Sports Page',font=40,activebackground='#27AE60',bg='#000000',fg='#FFFFFF',
                            width = 15, command=lambda: controller.show_frame("Sports_page"))
        
        button3 = tk.Button(self, text='Business Page',font=40,activebackground='#27AE60',bg='#000000',fg='#FFFFFF',
                            width = 15, command=lambda: controller.show_frame("Business_page"))
        
        button1.pack()
        label1.pack()
        button2.pack()
        label2.pack()
        button3.pack()



class Front_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Front Page Headlines.", font=80)
        label.pack(side="top", fill="x", pady=10)
        news = controller.news_section('Front Page')
        newsfeed=''
        for lines in range(len(news)):
            newsfeed += str(lines+1)+ '. ' +news[lines]+'\n'
            
        label = tk.Label(self, text=newsfeed, font=40, justify='left',fg='#808080')
        label.pack(side="top", fill="x")
            
        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack(side='left')
        button_next = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("Menu"))
        button_next.pack(side='right')
        button_back = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("Menu"))
        button_back.pack(side='left')


class Sports_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Sports News", font=60)
        label.pack(side="top", fill="x", pady=10)
        news = controller.news_section('sport')
        newsfeed=''
        for lines in range(len(news)):
            newsfeed += str(lines+1)+ '. ' +news[lines]+'\n'
            
        label = tk.Label(self, text=newsfeed, font=40, justify='left',fg='#808080')
        label.pack(side="top", fill="x")
        
        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack(side='left')
        button_next = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("Menu"))
        button_next.pack(side='right')
        button_back = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("Menu"))
        button_back.pack(side='left')

class Business_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Business News", font=60)
        label.pack(side="top", fill="x", pady=10)
        news = controller.news_section('business')
        newsfeed=''
        for lines in range(len(news)):
            newsfeed += str(lines+1)+ '. ' +news[lines]+'\n'
            
        label = tk.Label(self, text=newsfeed, font=40, justify='left',fg='#808080')
        label.pack(side="top", fill="x")
        
        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack(side='left')
        button_next = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("Business_page"))
        button_next.pack(side='right')
        button_back = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("Business_page"))
        button_back.pack(side='left')
        
        
if __name__ == "__main__":
    
    app = HinduInshorts()
    app.mainloop()

