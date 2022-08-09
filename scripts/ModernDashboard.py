try:
    import tkxui
    import sv_ttk
    import random
    import tkinter
    import threading
    import darkdetect
    import tkinter.ttk as ttk
    from Management import Materials
    from typing_extensions import Self
    from typing import (Literal , Union , final)
    from customtkinter.widgets.ctk_frame import CTkFrame as Frame
    from customtkinter.widgets.ctk_button import CTkButton as Button
    
finally:
    ...
    



@final
class App:
    def __init__(self: Self) -> Union[Literal[None] , Self]:
        super(App , self).__init__()
        self.root = tkxui.Tk(display=tkxui.FRAMELESS , defaultBorder=True , isResizable=True)
        self.root.title(title='Modern Dashboard')
        self.root.geometry(newGeometry='1024x700')
        self.root.minsize(width=1024 , height=700)
        self.root.maxsize(width=1100 , height=700)
        self.root.resizable(width=True , height=True)
        self.root.configure(bg=Materials.Colors.dark2)
        self.root.resizer_bg(bg=Materials.Colors.dark2)
        self.root.center()
        self.root.config_border({
            'border': {
                'bg': [Materials.Colors.dark2 if darkdetect.isDark() else Materials.Colors.grey]
            } ,
            'maximize': {
                'fg': Materials.Colors.white ,
                'bg': [Materials.Colors.dark2 if darkdetect.isDark() else Materials.Colors.grey],
                'hoverfg': Materials.Colors.white ,
                'hoverbg': Materials.Colors.green ,
            } ,
            'minimize': {
                'fg': Materials.Colors.white ,
                'bg': [Materials.Colors.dark2 if darkdetect.isDark() else Materials.Colors.grey],
                'hoverfg': Materials.Colors.white ,
                'hoverbg': Materials.Colors.green ,
            } ,
            'close': {
                'fg': Materials.Colors.white ,
                'bg': [Materials.Colors.dark3 if darkdetect.isDark() else Materials.Colors.grey] ,
                'hoverfg': Materials.Colors.white ,
                'hoverbg': Materials.Colors.tomato ,
            }
        })
        
        # self.values = ['Default Theme' , 'Default Theme' ,'Blue Theme' ,'Purple Theme' ]
        
        self.newSubs = ['5,097' , '4,845' , '8,547' , '2,318' , '9,241']
        self.strms = ['47,403' , '87,238' , '12,983' , '55,632' , '36,749']
        self.engRate = ['25.81' , '21.32' , '11.53' , '60.89' , '46.95' , '82.64']
        self.avgwt = ['45,4 min' , '32,1 min' , '50,7 min' , '12,2 min' , '23.8 min']
        
        self.sbsPercent = ['+33.45%' , '+12.32%' , '+50.45%' , '+85.26%' , '+74.99%']
        self.strmsPercent = ['-112.45%' , '-150.26%' , '-80.12%' , '-64.38%' , '-32.67%' , '-200.39%']
        self.engPercent = ['+62.52%' , '+90.54%' , '+23.21%' , '+112.35%' , '+76.93%' , '+51.61%']
        self.agwtPercent = ['+4.46%' , '+9.15%' , '+40.65%' , '+26.94%' , '+2.12%']
        
        self.svIncome = ['$2,205' , '$1,400' , '$5,920' , '$3,780' , '$9,426' , '$1,258']
        self.svSpend = ['$1,402' , '$1,202' , '$1,453' , '$1,369' , '$1,571' , '$1,954']
        
        self.systemTheme = darkdetect.theme()
        self.svSelectThemes = tkinter.StringVar()
        
        @final
        def dynamicSubscribersValuesSetter() -> Literal[None]:
            self.newSubscribers.configure(text=random.choice(seq=self.newSubs))
            self.subsPercent.configure(text=random.choice(seq=self.sbsPercent))
            self.root.after(ms=1500 , func=dynamicSubscribersValuesSetter)
            
        @final
        def dynamicStreamsValuesSetter() -> Literal[None]:
            self.streams.configure(text=random.choice(seq=self.strms))
            self.streamsPercent.configure(text=random.choice(seq=self.strmsPercent))
            self.root.after(ms=2500 , func=dynamicStreamsValuesSetter)
            
        @final
        def dynamicEngagementRateValuesSetter() -> Literal[None]:
            self.engagementRate.configure(text=random.choice(seq=self.engRate))
            self.engagementPercent.configure(text=random.choice(seq=self.engPercent))
            self.root.after(ms=1000 , func=dynamicEngagementRateValuesSetter)
            
        @final
        def dynamicAvgWatchtimeValuesSetter() -> Literal[None]:
            self.avgWatchtime.configure(text=random.choice(seq=self.avgwt))
            self.avgWatchPercent.configure(text=random.choice(seq=self.agwtPercent))
            self.root.after(ms=3000 , func=dynamicAvgWatchtimeValuesSetter)
            
        @final
        def dynamicIncomeSpendValueSetter() -> Literal[None]:
            self.income.configure(text=random.choice(seq=self.svIncome))
            self.spend.configure(text=random.choice(seq=self.svSpend))
            self.root.after(ms=1200 , func=dynamicIncomeSpendValueSetter)
            
        # @final
        # def setApplicationThemeByUserSelection(choice) -> Literal[None]:
        #     if (choice == 'Default Theme'):
        #         pass
        #     elif (choice == 'Blue Theme'):
        #         self.btnProfilePic.configure(fg_color=Materials.Colors.belizehole)
        #         self.btnPlus.configure(fg_color=Materials.Colors.belizehole)
        #         self.btnPodcasts.configure(fg_color=Materials.Colors.belizehole)
            
        @final
        def startThreads():
            subs = threading.Thread(target=dynamicSubscribersValuesSetter)
            streams = threading.Thread(target=dynamicStreamsValuesSetter)
            engagementRate = threading.Thread(target=dynamicEngagementRateValuesSetter)
            avgWatchtime = threading.Thread(target=dynamicAvgWatchtimeValuesSetter)
            incomeSpend = threading.Thread(target=dynamicIncomeSpendValueSetter)
            
            subs.daemon = True
            streams.daemon = True
            engagementRate.daemon = True
            avgWatchtime.daemon = True
            incomeSpend.daemon = True
            
            subs.start()
            streams.start()
            engagementRate.start()
            avgWatchtime.start()
            incomeSpend.start()
        
        @final
        def setThemeByOperatingSystem() -> Literal[None]:
            if (self.systemTheme == Materials.Themes.dark):
                sv_ttk.set_theme(theme=Materials.Themes.dark.lower())
                self.btnInbox.configure(fg_color=Materials.Colors.dark4)
                self.btnAlert.configure(fg_color=Materials.Colors.dark4)
                self.btnEpisodes.configure(fg_color=Materials.Colors.dark4)
                self.btnMedia.configure(fg_color=Materials.Colors.dark4)
                self.btnMaterials.configure(fg_color=Materials.Colors.dark4)
                self.btnSubscribers.configure(fg_color=Materials.Colors.dark4)
                self.btnChannels.configure(fg_color=Materials.Colors.dark4)
                self.btnReports.configure(fg_color=Materials.Colors.dark4)
                self.btnLeftFrameInnerBottom.configure(fg_color=Materials.Colors.dark4)
                self.leftFrameInnerBottom.configure(fg_color=Materials.Colors.dark5)
                self.frame1.configure(fg_color=Materials.Colors.dark3)
                self.frame2.configure(fg_color=Materials.Colors.dark3)
                self.frame3.configure(fg_color=Materials.Colors.dark3)
            else:
                sv_ttk.set_theme(theme=Materials.Themes.light.lower())
                self.btnInbox.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnAlert.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnEpisodes.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnMedia.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnMaterials.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnSubscribers.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnChannels.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnReports.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.btnLeftFrameInnerBottom.configure(fg_color=Materials.Colors.lightgrey , hover_color=Materials.Colors.grey)
                self.leftFrameInnerBottom.configure(fg_color=Materials.Colors.grey2)
                self.frame1.configure(fg_color=Materials.Colors.dark3)
                self.frame2.configure(fg_color=Materials.Colors.dark3)
                self.frame3.configure(fg_color=Materials.Colors.dark3)
        
        self.tabControl = ttk.Notebook(master=self.root)
        self.tabMain = ttk.Frame(master=self.tabControl)
        self.tabStyle = ttk.Frame(master=self.tabControl)
        
        self.tabControl.add(child=self.tabMain , text='Main')
        self.tabControl.add(child=self.tabStyle , text='Style')
        
        self.tabControl.pack(expand=1 , fill=Materials.Alignments.both)
        
        self.leftFrame = Frame(
            master=self.tabMain ,
            corner_radius=8 ,
            width=290 ,
            height=650 ,
        )
        
        self.leftFrame.place(
            relx=0.14 ,
            rely=0.5 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnPlus = Button(
            master=self.leftFrame ,
            text='+' ,
            corner_radius=5 ,
            text_font=(Materials.FontWeight.bold , 20) ,
            fg_color=Materials.Colors.green ,
            hover=True ,
            hover_color=Materials.Colors.green2 ,
            width=50 ,
            height=25 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
        )
        
        self.btnPlus.place(
            relx=0.85 ,
            rely=0.07 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnProfilePic = Button(
            master=self.leftFrame ,
            text=' ' ,
            text_font=(Materials.FontWeight.bold , 3) ,
            fg_color=Materials.Colors.green ,
            corner_radius=20 ,
            width=5 ,
            height=45 ,
            state=Materials.States.active ,
            cursor=None ,
        )
        
        ttk.Label(master=self.leftFrame , text='SB' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Vani' , 15 , Materials.FontWeight.bold)).place(relx=0.12 , rely=0.07 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.leftFrame , text='Shervin Bandanara' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , font=('Vani' , 11 , Materials.FontWeight.bold)).place(relx=0.455 , rely=0.055 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.leftFrame , text='Programmer' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.3445 , rely=0.085 , anchor=Materials.Alignments.center)
        
        self.btnProfilePic.place(
            relx=0.12 ,
            rely=0.07 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnInbox = Button(
            master=self.leftFrame ,
            text='Inbox' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnInbox.place(
            relx=0.5 ,
            rely=0.18 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnAlert = Button(
            master=self.leftFrame ,
            text='Alerts' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnAlert.place(
            relx=0.5 ,
            rely=0.25 ,
            anchor=Materials.Alignments.center ,
        )
        
        Button(
            master=self.leftFrame ,
            text='2' ,
            corner_radius=4 ,
            width=3 ,
            height=3 ,
            fg_color=Materials.Colors.tomato ,
            state=Materials.States.active ,
        ).place(
            relx=0.63 ,
            rely=0.25 ,
            anchor=Materials.Alignments.center
        )
        
        self.btnOverview = Button(
            master=self.leftFrame ,
            text='Overview' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            fg_color=Materials.Colors.green ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.green2 ,
        )
        
        self.btnOverview.place(
            relx=0.5 ,
            rely=0.32 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.leftFrame , text='Podcasts' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.16 , rely=0.38 , anchor=Materials.Alignments.center)
        
        self.btnEpisodes = Button(
            master=self.leftFrame ,
            text='Episods' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnEpisodes.place(
            relx=0.5 ,
            rely=0.44 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnMedia = Button(
            master=self.leftFrame ,
            text='Media' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnMedia.place(
            relx=0.5 ,
            rely=0.51 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnMaterials = Button(
            master=self.leftFrame ,
            text='Materials' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnMaterials.place(
            relx=0.5 ,
            rely=0.58 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.leftFrame , text='Analytics' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.16 , rely=0.64 , anchor=Materials.Alignments.center)
        
        self.btnSubscribers = Button(
            master=self.leftFrame ,
            text='Subscribers' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnSubscribers.place(
            relx=0.5 ,
            rely=0.7 ,
            anchor=Materials.Alignments.center ,
        )
        
        Button(
            master=self.leftFrame ,
            text='56' ,
            corner_radius=4 ,
            width=3 ,
            height=3 ,
            fg_color=Materials.Colors.tomato ,
            state=Materials.States.active ,
        ).place(
            relx=0.73 ,
            rely=0.7 ,
            anchor=Materials.Alignments.center
        )
        
        self.btnChannels = Button(
            master=self.leftFrame ,
            text='Channels' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnChannels.place(
            relx=0.5 ,
            rely=0.77 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnReports = Button(
            master=self.leftFrame ,
            text='Subscribers' ,
            text_font=(Materials.FontWeight.bold , 13) ,
            corner_radius=10 ,
            width=250 ,
            height=35 ,
            state=Materials.States.normal ,
            hover=True ,
            compound='center' ,
            cursor=Materials.Cursors.hand ,
            hover_color=Materials.Colors.dark2 ,
        )
        
        self.btnReports.place(
            relx=0.5 ,
            rely=0.84 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.leftFrameInnerBottom = Frame(
            master=self.leftFrame ,
            width=290 ,
            height=69 ,
        )
        
        self.leftFrameInnerBottom.place(
            relx=0.5 ,
            rely=0.93 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.btnPodcasts = Button(
            master=self.leftFrameInnerBottom ,
            text=' ' ,
            text_font=(Materials.FontWeight.bold , 3) ,
            fg_color=Materials.Colors.green ,
            corner_radius=20 ,
            width=5 ,
            height=45 ,
            state=Materials.States.active ,
            cursor=None ,
        )
        
        self.btnPodcasts.place(
            relx=0.12 ,
            rely=0.5 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.leftFrameInnerBottom , text='PC' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Vani' , 15 , Materials.FontWeight.bold)).place(relx=0.12 , rely=0.5 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.leftFrameInnerBottom , text='Podcaster' , background=[Materials.Colors.dark5 if darkdetect.isDark() else Materials.Colors.grey2] , font=('Vani' , 11 , Materials.FontWeight.bold)).place(relx=0.35 , rely=0.35 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.leftFrameInnerBottom , text='ver. 0.234' , background=[Materials.Colors.dark5 if darkdetect.isDark() else Materials.Colors.grey2] , foreground=Materials.Colors.white , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.33 , rely=0.62 , anchor=Materials.Alignments.center)
        
        self.btnLeftFrameInnerBottom = Button(
            master=self.leftFrameInnerBottom ,
            text='•••' ,
            text_color=Materials.Colors.white ,
            text_font=(Materials.FontWeight.bold , 12) ,
            hover=True ,
            hover_color=Materials.Colors.dark3 ,
            corner_radius=8 ,
            width=10 ,
            height=8 ,
            cursor=Materials.Cursors.hand ,
        )
        
        self.btnLeftFrameInnerBottom.place(
            relx=0.88 ,
            rely=0.5 ,
            anchor=Materials.Alignments.center ,
        )
        
        self.upperFrame = Frame(
            master=self.tabMain ,
            corner_radius=8 ,
            width=690 ,
            height=110 ,
        )
        
        self.upperFrame.place(
            relx=0.652 ,
            rely=0.115 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.upperFrame , background=[Materials.Colors.dark3 if darkdetect.isDark() else Materials.Colors.darkgrey] , width=0.3).place(relx=0.215 + 0.045 , rely=0.5 , height=50 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.upperFrame , background=[Materials.Colors.dark3 if darkdetect.isDark() else Materials.Colors.darkgrey] , width=0.3).place(relx=0.460 + 0.045 , rely=0.5 , height=50 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.upperFrame , background=[Materials.Colors.dark3 if darkdetect.isDark() else Materials.Colors.darkgrey] , width=0.3).place(relx=0.690 + 0.045 , rely=0.5 , height=50 , anchor=Materials.Alignments.center)
        
        ttk.Label(master=self.upperFrame , text='New Subscribers' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.1 , rely=0.2 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.upperFrame , text='Streams' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.33 , rely=0.2 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.upperFrame , text='Engagement Rate' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.6 , rely=0.2 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.upperFrame , text='Avg. watch time' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.835 , rely=0.2 , anchor=Materials.Alignments.center)
        
        self.newSubscribers = ttk.Label(master=self.upperFrame , text='5,097' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 20 , Materials.FontWeight.bold));self.newSubscribers.place(relx=0.08 , rely=0.5 , anchor=Materials.Alignments.center)
        self.streams = ttk.Label(master=self.upperFrame , text='47,403' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 20 , Materials.FontWeight.bold));self.streams.place(relx=0.35 , rely=0.5 , anchor=Materials.Alignments.center)
        self.engagementRate = ttk.Label(master=self.upperFrame , text='25.81' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 20 , Materials.FontWeight.bold));self.engagementRate.place(relx=0.575 , rely=0.5 , anchor=Materials.Alignments.center)
        self.avgWatchtime = ttk.Label(master=self.upperFrame , text='45,4 min' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 20 , Materials.FontWeight.bold));self.avgWatchtime.place(relx=0.85 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.subsPercent = ttk.Label(master=self.upperFrame , text='+33.45%' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Poplar Std' , 11 , Materials.FontWeight.normal));self.subsPercent.place(relx=0.073 , rely=0.77 , anchor=Materials.Alignments.center)
        self.streamsPercent = ttk.Label(master=self.upperFrame , text='-112.45%' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.red , font=('Poplar Std' , 11 , Materials.FontWeight.normal));self.streamsPercent.place(relx=0.335 , rely=0.77 , anchor=Materials.Alignments.center)
        self.engagementPercent = ttk.Label(master=self.upperFrame , text='+62.52%' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Poplar Std' , 11 , Materials.FontWeight.normal));self.engagementPercent.place(relx=0.565 , rely=0.77 , anchor=Materials.Alignments.center)
        self.avgWatchPercent = ttk.Label(master=self.upperFrame , text='+4.46%' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Poplar Std' , 11 , Materials.FontWeight.normal));self.avgWatchPercent.place(relx=0.805 , rely=0.77 , anchor=Materials.Alignments.center)
        
        self.firstMiddleLeftFrame = Frame(
            master=self.tabMain ,
            corner_radius=8 ,
            width=430 ,
            height=255 ,
        )
        
        self.firstMiddleLeftFrame.place(
            relx=0.5241 ,
            rely=0.432 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.firstMiddleLeftFrame , text='Visa Card' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 20 , Materials.FontWeight.bold)).place(relx=0.5 , rely=0.11 , anchor=Materials.Alignments.center)
        
        self.card = Frame(
            master=self.firstMiddleLeftFrame ,
            corner_radius=10 ,
            fg_color=Materials.Colors.green ,
            width=330 ,
            height=170 ,
            border_width=0 ,
        )
        
        self.card.place(
            relx=0.5 ,
            rely=0.56 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.firstMiddleLeftFrame , text='Visa' , background=Materials.Colors.green, foreground=Materials.Colors.white , font=('Courier' , 15 , [Materials.FontWeight.bold , Materials.FontWeight.italic])).place(relx=0.25 , rely=0.4 , anchor=Materials.Alignments.center)
        self.cardNumber = ttk.Label(master=self.firstMiddleLeftFrame , text='****  ****  ****  1715' , background=Materials.Colors.green, foreground=Materials.Colors.white , font=('Vani' , 22 , Materials.FontWeight.bold));self.cardNumber.place(relx=0.5 , rely=0.6 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.firstMiddleLeftFrame , text='Shervin Badanara' , background=Materials.Colors.green, foreground=Materials.Colors.white , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.315 , rely=0.8 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.firstMiddleLeftFrame , text='07/02' , background=Materials.Colors.green, foreground=Materials.Colors.white , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.739 , rely=0.8 , anchor=Materials.Alignments.center)
        
        self.secondMiddleLeftFrame = Frame(
            master=self.tabMain ,
            corner_radius=8 ,
            width=430 ,
            height=195 ,
        )
        
        self.secondMiddleLeftFrame.place(
            relx=0.5241 ,
            rely=0.815 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.secondMiddleLeftFrame , text='Popular episods' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 11 , Materials.FontWeight.normal)).place(relx=0.18 , rely=0.12 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='See all' , cursor=Materials.Cursors.hand , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Vani' , 11 , Materials.FontWeight.normal)).place(relx=0.88 , rely=0.12 , anchor=Materials.Alignments.center)
        
        self.frame1 = Frame(
            master=self.secondMiddleLeftFrame ,
            corner_radius=5 ,
            width=45 ,
            height=28 ,
        )
        
        self.frame1.place(
            relx=0.115 ,
            rely=0.35 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.frame1 , text='1' , background=Materials.Colors.dark3 , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.46 , rely=0.5 , anchor=Materials.Alignments.center)
        
        ttk.Label(master=self.secondMiddleLeftFrame , text='Kuji Podcast 33: Live' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , font=('Vani' , 12 , Materials.FontWeight.bold)).place(relx=0.38 , rely=0.29 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='Guest: Nurlan Saburov' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.34 , rely=0.4 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='1,99m' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.8 , rely=0.335 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='Live' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.9 , rely=0.333 , anchor=Materials.Alignments.center)
        
        self.frame2 = Frame(
            master=self.secondMiddleLeftFrame ,
            corner_radius=5 ,
            width=45 ,
            height=28 ,
        )
        
        self.frame2.place(
            relx=0.115 ,
            rely=0.6 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.frame2 , text='2' , background=Materials.Colors.dark3 , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.46 , rely=0.5 , anchor=Materials.Alignments.center)
        
        ttk.Label(master=self.secondMiddleLeftFrame , text='Kuji Podcast 33: Live' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , font=('Vani' , 12 , Materials.FontWeight.bold)).place(relx=0.38 , rely=0.55 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='Guest: Nurlan Saburov' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.34 , rely=0.655 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='1,54m' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.8 , rely=0.581 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='Live' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.9 , rely=0.579 , anchor=Materials.Alignments.center)
        
        self.frame3 = Frame(
            master=self.secondMiddleLeftFrame ,
            corner_radius=5 ,
            width=45 ,
            height=28 ,
        )
        
        self.frame3.place(
            relx=0.115 ,
            rely=0.85 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.frame3 , text='3' , background=Materials.Colors.dark3 , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.46 , rely=0.5 , anchor=Materials.Alignments.center)
        
        ttk.Label(master=self.secondMiddleLeftFrame , text='Kuji Podcast 33: Live' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , font=('Vani' , 12 , Materials.FontWeight.bold)).place(relx=0.38 , rely=0.8 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='Guest: Nurlan Saburov' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.34 , rely=0.9 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='1,04m' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.8 , rely=0.83 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleLeftFrame , text='Live' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green2 , font=('Vani' , 10 , Materials.FontWeight.normal)).place(relx=0.9 , rely=0.825 , anchor=Materials.Alignments.center)
        
        self.firstMiddleRightFrame = Frame(
            master=self.tabMain ,
            corner_radius=8 ,
            width=249 ,
            height=190 ,
        )
        
        self.firstMiddleRightFrame.place(
            relx=0.867 ,
            rely=0.38 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.firstMiddleRightFrame , text='Current Balace' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 20 , Materials.FontWeight.bold)).place(relx=0.5 , rely=0.15 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.firstMiddleRightFrame , text='$' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green , font=('Poplar Std' , 30 , Materials.FontWeight.bold)).place(relx=0.23 , rely=0.5 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.firstMiddleRightFrame , text='75,533' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=[Materials.Colors.white if darkdetect.isDark() else Materials.Colors.black] , font=('Poplar Std' , 30 , Materials.FontWeight.bold)).place(relx=0.53 , rely=0.5 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.firstMiddleRightFrame , text='Income:' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.15 + 0.04 , rely=0.85 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.firstMiddleRightFrame , text='Spend:' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.grey , font=('Vani' , 9 , Materials.FontWeight.normal)).place(relx=0.6  + 0.04, rely=0.85 , anchor=Materials.Alignments.center)
        self.income = ttk.Label(master=self.firstMiddleRightFrame , text='$2,205' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.green , font=('Vani' , 9 , Materials.FontWeight.normal));self.income.place(relx=0.33 + 0.05 , rely=0.85 , anchor=Materials.Alignments.center)
        self.spend = ttk.Label(master=self.firstMiddleRightFrame , text='$1,402' , background=[Materials.Colors.dark4 if darkdetect.isDark() else Materials.Colors.lightgrey] , foreground=Materials.Colors.red , font=('Vani' , 9 , Materials.FontWeight.normal));self.spend.place(relx=0.77 + 0.05 , rely=0.85 , anchor=Materials.Alignments.center)
        
        self.secondMiddleRightFrame = Frame(
            master=self.tabMain ,
            corner_radius=8 ,
            fg_color=Materials.Colors.green ,
            width=249 ,
            height=261 ,
        )
        
        self.secondMiddleRightFrame.place(
            relx=0.867 ,
            rely=0.76 ,
            anchor=Materials.Alignments.center ,
        )
        
        ttk.Label(master=self.secondMiddleRightFrame , text='Webinars' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 11 , Materials.FontWeight.bold)).place(relx=0.25 , rely=0.12 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text='Learn How to' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 17 , Materials.FontWeight.bold)).place(relx=0.4 , rely=0.28 - 0.011, anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text='can earn more then' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 17 , Materials.FontWeight.bold)).place(relx=0.535 , rely=0.4 - 0.011, anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text=r'20% each month!' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 17 , Materials.FontWeight.bold)).place(relx=0.485 , rely=0.52 - 0.011, anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text='join our webinar and learn how' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 9 , Materials.FontWeight.normal)).place(relx=0.445 , rely=0.64 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text='to increase more then 20%' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 9 , Materials.FontWeight.normal)).place(relx=0.41 , rely=0.7 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text='your monthly income.' , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 9 , Materials.FontWeight.normal)).place(relx=0.35 , rely=0.76 , anchor=Materials.Alignments.center)
        ttk.Label(master=self.secondMiddleRightFrame , text='Learn more' , cursor=Materials.Cursors.hand , background=Materials.Colors.green , foreground=Materials.Colors.white , font=('Poplar Std' , 11 , Materials.FontWeight.bold)).place(relx=0.275 , rely=0.9 , anchor=Materials.Alignments.center)
        
        self.btnSecondMiddleRight = Button(
            master=self.secondMiddleRightFrame ,
            text='•••' ,
            fg_color=Materials.Colors.green3 ,
            text_color=Materials.Colors.white ,
            text_font=(Materials.FontWeight.bold , 12) ,
            hover=True ,
            hover_color=Materials.Colors.green2 ,
            corner_radius=8 ,
            width=10 ,
            height=8 ,
            cursor=Materials.Cursors.hand ,
        )
        
        self.btnSecondMiddleRight.place(
            relx=0.82 ,
            rely=0.12 ,
            anchor=Materials.Alignments.center ,
        )
        
        # self.options = ttk.OptionMenu(
        #     self.tabStyle ,
        #     self.svSelectThemes ,
        #     command=setApplicationThemeByUserSelection ,
        #     *self.values ,
        # )
        
        # self.options.place(
        #     relx=0.5 ,
        #     rely=0.5 ,
        #     anchor=Materials.Alignments.center ,
        # )
        
        # self.svSelectThemes.set(value=self.values[0])
        
        startThreads()
        setThemeByOperatingSystem()
        
        self.root.mainloop()
        




def main() -> Literal[None]:
    App()
    
    


if (__name__ == '__main__' and __package__ is None):
    main()