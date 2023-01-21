from pytube import YouTube

root = Tk()
root.geometry('450x200')
root.resizable(0,0)
root.title("youtube video downloader")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()



link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 55,textvariable = link).place(x = 32, y = 90)
#function to download video

Label(root,text = 'copyright | made in india | no ads | secure ', font ='arial 5 bold').pack()

def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
