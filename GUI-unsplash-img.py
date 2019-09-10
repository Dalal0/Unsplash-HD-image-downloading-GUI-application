from tkinter import *
import requests
import os, pprint
from time import sleep
from threading import *
from urllib.request import urlretrieve


class Gui(Tk):
    def __init__(self):
        self.do_splash_call = False
        Tk.__init__(self)
        self.title('unsplash image download')
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
        self.page = Spinbox(page_frame, from_=1, to=50, width=30)
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
        self.save = Entry(save_frame, bd=1)
        self.save.place(relx=.1, relwidth=1)

        # insert path for save images
        self.save.insert(0, 'c:\\users\\abc\\Desktop\\photos')



    def path(self):
        if os.path.exists(self.save.get()):
            os.chdir(self.save.get())
        else:
            os.mkdir(self.save.get())
            os.chdir(self.save.get())
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
                api = f'https://api.unsplash.com/photos/search?query={image_name}&resolution={size}&orientation={orientation}&client_id=8c8b90902c54cea3f2f2cab40bdb8f20312086c3342fe83428f930c72e6e2219&page={pages}&w=1500&dpi=2'  # This is pixel size 1500, 1080,400,200
                res = requests.get(api).json()
                if 'error' in res: print(res['error'])
                for i in range(10):
                    url = res[i]['links']['download']

                    name_of_image = str(res[i]['alt_description'])
                    img_name = '_'.join(name_of_image[:40].split(' '))
                    # create folder for download images
                    self.path()


                    # print current images downloading
                    self.output.insert(INSERT, 'Downloading Image ====>> %s.png\n' % img_name)
                    self.output.tag_add('fine', '1.0', '1.9')
                    self.output.tag_config('fine', background='lightGreen', foreground='#196619')
                    # Downloading image in pc
                    urlretrieve(url, '%s.png' % img_name)
                    if i==9:
                        self.output.insert(INSERT, 'We are done.')
                        self.output.tag_add('wait', '1.0', '1.9')
                        self.output.tag_config('wait', background='Green', foreground='black')



            except Exception as e:
                self.output.insert(INSERT, e)
                self.output.tag_add('error', '1.0', '1.9')
                self.output.tag_config('error', background='#ff4d4d', foreground='black')
                print(e)

            self.do_splash_call = False

if __name__ == '__main__':
    app = Gui()
    app.mainloop()