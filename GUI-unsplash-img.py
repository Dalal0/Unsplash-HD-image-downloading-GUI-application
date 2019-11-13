try:
    from tkinter import *
    from tkinter import Tk
except ImportError:
    from tkinter import Tk

import requests, platform
import os
from threading import *
from urllib.request import urlretrieve



class Gui(Tk):
    def __init__(self):
        self.do_splash_call = False
        Tk.__init__(self)
        self.title('Free image download')
        self.geometry('900x500')
        # main canvas
        main = Canvas(self, bg='#0099e6')
        main.place(relx=0, rely=0, relwidth=1, relheight=1)

        # frame1 for upper left
        name_frame = Frame(main)
        name_frame.place(relx=.1, rely=.1)
        # name input and label
        name_label = Label(name_frame, text='Image Name:')
        name_label.pack(side=LEFT, pady=3)
        self.name = Entry(name_frame, bd=0, font=1, width=23)
        self.name.pack(side=RIGHT, pady=3)

        # frame2 for upper right
        page_frame = Frame(main)
        page_frame.place(relx=.5, rely=.1, relwidth=.3)
        # landing page
        Label(page_frame, text='Landing page:').pack(side=LEFT, pady=3)
        self.page = Spinbox(page_frame, from_=1, to=27, width=30)
        self.page.pack(side=RIGHT, pady=3)

        # frame3 for down left
        size_frame = Frame(main)
        size_frame.place(relx=.1, rely=.2)
        # name input and label
        size_label = Label(size_frame, text='Android, pc, tablet:')
        size_label.pack(side=LEFT, pady=3)
        self.size = Entry(size_frame, bd=0, font=1)
        self.size.pack(side=RIGHT, pady=3)

        # button
        download = Button(main, bd=1, font=4, text='Download', width=10, command=lambda :self.splash())
        download.place(relx=.6, rely=.2)

        # output
        self.output = Text(main, bd=2)
        self.output.place(relx=0, rely=.5, relheight=1, relwidth=1)

        # path to save images
        save_frame = Frame(main)
        save_frame.place(relx=.1, rely=.3, relwidth=.7)
        Label(save_frame, text='Save:').pack(side=LEFT, padx=5)
        self.path = Entry(save_frame, bd=1)
        self.path.place(relx=.1, relwidth=1)

        # insert path for save images
        # Check system info
        if platform.system()=='Linux':
            self.path.insert(0, '/home/rohit/Desktop/img')
        else:
            self.path.insert(0, 'c:\\users\\PC-Name\\Desktop\\photos')



    def check_image_path(self):
        if os.path.exists(self.path.get()):
            os.chdir(self.path.get())
        else:
            os.mkdir(self.path.get())
            os.chdir(self.path.get())

    def splash(self):
        self.do_splash_call = True
        image_name = self.name.get()
        pages = self.page.get()
        size = self.size.get()

        thread = Thread(target=self.call_splash, args=(image_name, pages, size))
        thread.start()

    def call_splash(self, image_name, pages, size):
        if self.do_splash_call:
            # set the size of photos
            if size in ('pc', 'desktop'):
                size = 1080
                orientation = 'landscape'
            elif size in ('hd', 'full hd', 'clear', 'normal', 'HD'):
                size = 1500
                orientation = 'landscape'
            elif size in ('android', 'mini', 'mobile'):
                size = 400
                orientation = 'portrait'
            else:
                size = 1500
                orientation = 'landscape'

            try:
                api = f'https://api.unsplash.com/search/photos?query={image_name}&resolution={size}&client_id=71fab1070168597fcfd2bf922067b1b266a00074285460c4fa4e1967dff36384&page={pages}&w=1500&dpi=2'
                res = requests.get(api).json()

                if not 'errors' in res:
                    try:
                        for i in range(10):
                            url = res['results'][i]['urls']['full']

                            name_of_image = str(res['results'][i]['alt_description'])
                            img_name = '_'.join(name_of_image[:40].split(' '))


                            # create folder for download images
                            self.check_image_path()


                            # print current images downloading
                            self.output.insert(INSERT, 'Downloading Image %s ====>> %s.png\n' % (str(i+1),img_name))
                            self.output.tag_add('fine', '0.0', '3.0')
                            self.output.tag_config('fine', background='lightGreen', foreground='#196619')
                            # Downloading image in pc
                            urlretrieve(url, '%s.jpg' % img_name)
                    except KeyError:
                        self.output.insert(INSERT, 'Invalid Tree!')
                else:
                    self.output.insert(INSERT, 'API invalid!')



            except Exception as e:
                self.output.insert(INSERT, e)
                self.output.tag_add('error', '1.0', '1.9')
                self.output.tag_config('error', background='#ff4d4d', foreground='black')
                print(e)

            self.do_splash_call = False

if __name__ == '__main__':
    app = Gui()
    app.mainloop()

