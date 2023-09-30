from tkinter import *
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt
import numpy as np
from numpy import log
from PIL import Image,ImageTk

from tkinter.font import Font
import ttkbootstrap as tb
import webbrowser
current_frame = None
current_frames=None
current_1frames=None

root = tb.Window(themename="superhero")
root.title("Radar Calculator")
root.geometry("{}x{}+0+0". format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.config(bg='#053B50')
root.iconbitmap(r'C:\RadarCalculator\new_drdo_logo_3-removebg-preview.ico')


#Fuction to calculate los

def calculatelos():
    lead = Toplevel();
    lead.title('LOS calculator')
    lead.geometry("{}x{}+0+0".format(lead.winfo_screenwidth(), lead.winfo_screenheight()))
    lead.config(bg='#053B50')
    lead.iconbitmap(r'C:\RadarCalculator\new_drdo_logo_3-removebg-preview.ico')

    R=6371
    f=123

    #Fucntion for unit
    def unit(r):

        if r == '0.001':
            u = 'm'
        elif r == '0.0003048':
            u = 'Feet'
        else:
            u = 'Km'
        return u

    #Function to calculate los
    def loscalc():
        ans1 = tb.Label(lead, text='\t\t\t\t').grid(row=1, column=0, pady=370,padx=650,sticky='NW')
        htt = float(ht.get()) * float(r1.get())
        hrr = float(hr.get()) * float(r2.get())
        los = ((2 * R * htt + (htt ** 2)) ** 0.5 + (2 * R * hrr + (hrr ** 2)) ** 0.5)
        ans1 = tb.Label(lead, text='\t\t\t\t',foreground='#EEEEEE',background='#053B50',font=("Latha",15),anchor="center").grid(row=1, column=0, pady=370,padx=650,sticky='NW')
        ans1 = tb.Label(lead, text=' ' + str(round(los / float(r12.get()), 3)) + " " + unit(r12.get()) + ' ',foreground='#EEEEEE',background='#053B50',font=("Latha",15),anchor="center").grid(row=1, column=0, pady=370,padx=650,sticky='NW')

    #Labels
    Title = tb.Label(lead,text="LOS Calculator",foreground='#64CCC5',background='#053B50',font=("Broadway",50))
    Title.grid(sticky='NW',row=0,column=0,padx=650)

    lostitle=tb.Label(lead,text="Line of sight calculation",foreground='#EEEEEE',background='#053B50',font=("Broadway",18))
    lostitle.grid(row=1, column=0,padx=150,pady=50,sticky='NW')

    heighttitle=tb.Label(lead,text="Height of Antenna Calculation",foreground='#EEEEEE',background='#053B50',font=("Broadway",15))
    heighttitle.grid(row=1,column=0,padx=150,pady=450,sticky='NW')

    th1 = tb.Label(lead, text="Transmitter Antenna Height:",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    th1.grid(row=1, column=0,padx=150,pady=140,sticky='NW')

    rh1 = tb.Label(lead, text="Reciever Antenna Height:",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    rh1.grid(row=1, column=0,padx=150,pady=220,sticky='NW',ipadx=20)

    selectunit = tb.Label(lead, text='Select unit for LOS value:',foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    selectunit.grid(row=1, column=0,padx=150,pady=300,sticky='NW',ipadx=20)

    givelos= tb.Label(lead,text="Line of sight value",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    givelos.grid(row=1,column=0,padx=150,pady=520,sticky='NW',ipadx=20)

    heightavailable= tb.Label(lead,text="Is height of one antenna available?",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    heightavailable.grid(row=1,column=0,padx=150,pady=600,sticky='NW',ipadx=20)

    selectunittwo= tb.Label(lead,text="Select the unit for required antenna height",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    selectunittwo.grid(row=1,column=0,padx=150,pady=750,sticky='NW')

    #Variables
    ht = StringVar()
    hr = StringVar()
    los = StringVar()
    #Entry
    then = tb.Entry(lead, textvariable=ht)
    then.grid(row=1, column=0, padx=550,pady=140,sticky='NW',ipadx=30)

    rhen = tb.Entry(lead, textvariable=hr)
    rhen.grid(row=1, column=0, padx=550,pady=220,sticky='NW',ipadx=30)

    losentry=tb.Entry(lead,textvariable=los)
    losentry.grid(row=1,column=0,padx=550,pady=520,sticky='NW',ipadx=30)


    #function for combobox
    def with_at_frame():

        frame = tb.Frame(lead)
        frame.grid(row=1, column=0, padx=150, pady=670, sticky='NW')
        global at
        global r4
        r4 = tb.StringVar()
        r4.set('1')
        fourthm = tb.Radiobutton(frame, text="Metres", variable=r4, value='0.001')
        fourthm.grid(row=1, column=2, padx=110, pady=0, sticky='NW')
        fourthfeet = tb.Radiobutton(frame, text="Feet", variable=r4, value='0.0003048')
        fourthfeet.grid(row=1, column=3, padx=130, pady=0, sticky='NW')
        fourthkm = tb.Radiobutton(frame, text="Kilometres", variable=r4, value='1')
        fourthkm.grid(row=1, column=4, padx=150, pady=0, sticky='NW')

        antheight = tb.Label(frame, text="Antenna Height 1:", foreground='#EEEEEE',background='#176B87', font=("Latha", 15), anchor="center")
        antheight.grid(row=1, column=0, padx=20, pady=10, sticky='NW')
        at = tb.StringVar()
        att = tb.Entry(frame, textvariable=at).grid(row=1, column=1, padx=50, pady=0, sticky='NW', ipadx=30, ipady=5)

        return frame

    def without_at_frame():
        frame = tb.Frame(lead)
        frame.grid(row=1, column=0, padx=150, pady=670, sticky='NW')

        tb.Label(frame, text="\t\t").grid(row=1, column=0, padx=0, pady=0, sticky='NW')
        tb.Label(frame, text=" Taking Height of Both Antennas as equal", foreground='#EEEEEE',background='#176B87',font=("Latha", 15), anchor="center").grid(row=1, column=0, padx=150, pady=0,
                                                                               sticky='NW')

        return frame

    def selected(event):
        global current_frame

        if my_combo.get() == "Yes":
            if current_frame:
                current_frame.grid_forget()
            current_frame = with_at_frame()
        else:
            if current_frame:
                current_frame.grid_forget()
            current_frame = without_at_frame()

    options = ["No", "Yes"]

    my_combo = tb.Combobox(lead, values=options)
    my_combo.grid(row=1, column=0, padx=600, pady=600, sticky='NW')
    my_combo.current(1)
    my_combo.bind("<<ComboboxSelected>>", selected)


    #Radiobuttons
    r1 = StringVar()
    r1.set('1')
    firstm= tb.Radiobutton(lead, text="Metres", variable=r1, value='0.001').grid(row=1, column=0, padx=950,pady=140,sticky='NW',ipadx=30)
    firstfeet= tb.Radiobutton(lead, text="Feet", variable=r1, value='0.0003048').grid(row=1, column=0, padx=950,pady=140,sticky='NE',ipadx=30)
    firstkm= tb.Radiobutton(lead, text="Kilometres", variable=r1, value='1').grid(row=1, column=0, padx=1150,pady=140,sticky='NE',ipadx=30)

    r2 = StringVar()
    r2.set('1')
    secondm= tb.Radiobutton(lead, text="Metres", variable=r2, value='0.001').grid(row=1, column=0, padx=950,pady=220,sticky='NW',ipadx=30)
    secondfeet=tb.Radiobutton(lead, text="Feet", variable=r2, value='0.0003048').grid(row=1, column=0, padx=950,pady=220,sticky='NE',ipadx=30)
    secondkm=tb.Radiobutton(lead, text="Kilometres", variable=r2, value='1').grid(row=1, column=0, padx=1150,pady=220,sticky='NE',ipadx=30)

    r12 = StringVar()
    r12.set('1')
    thirdm=tb.Radiobutton(lead, text="Metres", variable=r12, value='0.001').grid(row=1, column=0, padx=550,pady=310,sticky='NW',ipadx=30)
    thirdfeet=tb.Radiobutton(lead, text="Feet", variable=r12, value='0.0003048').grid(row=1, column=0, padx=1000,pady=310,sticky='NW',ipadx=30)
    thirdkm=tb.Radiobutton(lead, text="Kilometres", variable=r12, value='1').grid(row=1, column=0, padx=750,pady=310,sticky='NW',ipadx=30)

    r3 = StringVar()
    r3.set('1')
    thirdm=tb.Radiobutton(lead, text="Metres", variable=r3, value='0.001').grid(row=1, column=0, padx=950,pady=520,sticky='NW',ipadx=30)
    thirdfeet=tb.Radiobutton(lead, text="Feet", variable=r3, value='0.0003048').grid(row=1, column=0, padx=950,pady=520,sticky='NE',ipadx=30)
    thirdkm=tb.Radiobutton(lead, text="Kilometres", variable=r3, value='1').grid(row=1, column=0, padx=1150,pady=520,sticky='NE',ipadx=30)

    r34 = StringVar()
    r34.set('1')
    thirdm=tb.Radiobutton(lead, text="Metres", variable=r34, value='0.001').grid(row=1, column=0, padx=950,pady=750,sticky='NW',ipadx=30)
    thirdfeet=tb.Radiobutton(lead, text="Feet", variable=r34, value='0.0003048').grid(row=1, column=0, padx=950,pady=750,sticky='NE',ipadx=30)
    thirdkm=tb.Radiobutton(lead, text="Kilometres", variable=r34, value='1').grid(row=1, column=0, padx=1150,pady=750,sticky='NE',ipadx=30)

    #function to calculate height
    def height():
        ans = tb.Label(lead, text='\t\t\t\t')
        ans.grid(row=1, column=0, padx=650,pady=800,sticky='NW',ipadx=20)
        L = float(los.get()) * float(r3.get())
        if my_combo.get() == 'Yes':
            h1 = float(at.get()) * float(r4.get())
            a1 = (2 * R * h1 + h1 ** 2) ** 0.5
            a2 = L - a1
            h = -R + (R ** 2 + a2 ** 2) ** 0.5
        else:
            h = (-R + ((4 * (R ** 2) + L ** 2) ** 0.5) / 2)
        u = unit(r34.get())
        ans =tb.Label(lead, text='\t\t\t\t',foreground='#EEEEEE',background='#053B50',font=("Latha",15),anchor="center")
        ans.grid(row=1, column=0, padx=650,pady=800,sticky='NW',ipadx=20)
        ans1 =tb.Label(lead, text=str(round((h / float(r34.get())), 3)) + " " + u,foreground='#EEEEEE',background='#053B50',font=("Latha",15),anchor="center")
        ans1.grid(row=1, column=0, padx=650,pady=800,sticky='NW',ipadx=20)

    #Button
    calcbutton=tb.Button(lead,text="Calculate",command=loscalc)
    calcbutton.grid(row=1,column=0,padx=350,pady=370,ipadx=20,ipady=0,sticky='NW')

    calheight = tb.Button(lead, text="Calcuate Height", command=height)
    calheight.grid(row=1, column=0, padx=350, pady=800, sticky='NW', ipadx=20)

    def callback():
        webbrowser.open_new("https://www.scadacore.com/tools/rf-path/rf-line-of-sight/")

    #tk.Label(root, text=" You can plot LOS by clicking this button!").grid(row=12, column=1, pady=30)
    hy = tb.Button(lead, text="Plot Los Online", bootstyle="light-link", command=callback)
    hy.grid(row=1,column=0,padx=700,pady=810,sticky='NE')


#Function to calculate snr
def calculatesnr():
    master = Toplevel();
    master.title('SNR Calculator')
    master.geometry("{}x{}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    master.config(bg='#053B50')
    master.iconbitmap(r'C:\RadarCalculator\new_drdo_logo_3-removebg-preview.ico')

#Single Value
    #snrcalc function
    def snrcalc():
        pd_value= pdval.get()

        pulse_value = pulse.get()

        if my_combosnr2.get()=="10^-3":
            pfa_value=0.001
        elif my_combosnr2.get()=="10^4":
            pfa_value=0.0001
        elif my_combosnr2.get()=="10^-5":
            pfa_value=0.00001
        elif my_combosnr2.get()=="10^-6":
            pfa_value=0.000001
        elif my_combosnr2.get()=="10^-7":
            pfa_value=0.0000001
        elif my_combosnr2.get()=="10^-8":
            pfa_value=0.00000001
        elif my_combosnr2.get()=="10^-9":
            pfa_value=0.000000001
        else:
            pfa_value=0.0000000001
        global c1
        global c2

        if pulse_value==40 or pulse_value<40:
            a=0
        else:
            a=1/4

        mu=np.sqrt(-0.8*log(4*pfa_value*(1-pfa_value)))+(pd_value-0.5)*np.sqrt(-0.8*log(4*pd_value*(1-pd_value)))
        snr0=mu*(mu+(2*np.sqrt(pulse_value/2+(a-(1/4)))))



        if my_combosnr.get()=="1":

            k=1
        elif my_combosnr.get()=="2":
            k=pulse_value
        elif my_combosnr.get()=="3":
            k=2
        else:
            k=2*pulse_value

        c1=1/k*(((17.7006*pd_value-18.4496)*pd_value + 14.5339)*pd_value-3.525)
        c2=1/k*(np.e**(27.31*pd_value-25.14)+(pd_value-0.8)*(0.7*np.log((10**-5)/pfa_value)+(2*pulse_value-20)/80))

        if pd_value>=0.1 or pd_value<=0.87:
            cdb=c1
        elif pd_value>=0.87 or pd_value<=0.99:
            cdb=c1+c2

        c=10**(cdb/10)
        snrmin=10*np.log10(c*snr0/pulse_value)


        #A = np.log(0.62 / pfa_value)
        #B = np.log(pd_value / (1 - pd_value))

        #snr = 10 * np.log10(A + 0.12 * A * B + 1.7 * B)
        snrans=tb.Label(master,text="SNR: "+ str(round(snrmin,3)),foreground='White',background='#053B50',font=("Ubuntu",15))
        snrans.grid(row=1,column=0,pady=420,padx=900,ipadx=10,ipady=10,sticky='NW')

    # Combobox
    option = ["1", "2", "3", "4"]

    my_combosnr = tb.Combobox(master, values=option,style='TCombobox',font=(18))
    my_combosnr.grid(row=1, column=0, pady=310, padx=1200, sticky='NW')
    my_combosnr.current(1)


    #Combobox
    ops = ["10^-3", "10^-4", "10^-5", "10^-6","10^-7","10^-8","10^-9","10^-10"]
    my_combosnr2 = tb.Combobox(master, values=ops, style='TCombobox',font=(18))
    my_combosnr2.grid(row=1,column=0,sticky='NW',pady=190,padx=1200,ipadx=10,ipady=0)
    my_combosnr2.current(1)



    #Labels
    mainlabel= tb.Label(master,text="SNR Calculator", foreground='#64CCC5',background='#053B50',font=("Broadway",50))
    mainlabel.grid(row=0,column=0,sticky='NW', padx=650)

    #singlevalue= tb.Label(master,text="For Single Value",foreground='#64CCC5',background='#053B50',font=("Ubuntu",20,'bold'))
    #singlevalue.grid(row=1,column=0, sticky='NW',pady=100,padx=100,ipadx=10,ipady=10)

    PdLabel=tb.Label(master,text="Enter Pd value",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    PdLabel.grid(row=1, column=0,sticky='NW',pady=190,padx=350,ipadx=10,ipady=10)

    pfaLabel=tb.Label(master,text="Enter Pfa value",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    pfaLabel.grid(row=1, column=0,sticky='NW',pady=190,padx=950,ipadx=10,ipady=10)

    noofpulses=tb.Label(master,text="Number of Pulses",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    noofpulses.grid(row=1, column=0,sticky='NW',pady=310,padx=350,ipadx=10,ipady=10)

    swerlingcase=tb.Label(master,text="Swerling case",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    swerlingcase.grid(row=1, column=0,sticky='NW',pady=310,padx=950,ipadx=10,ipady=10)

    #Variable
    pdval = DoubleVar()

    pulse= IntVar()

    #style
    entry_style=tb.Style()
    entry_style.configure('info.TEntry',foreground='White',font=("Latha",15))

    button_style=tb.Style()
    button_style.configure('primary.Outline.TButton',font=("Ubuntu",15),width=12)
    #Entry
    pdentry=tb.Entry(master, textvariable=pdval,font=("Latha",12),style='info.TEntry',)
    pdentry.grid(row=1, column=0,sticky='NW',pady=190,padx=600,ipadx=10,ipady=10)

    #pfaentry = tb.Entry(master,textvariable=pfaval,font=("Latha",12),style='info.TEntry',bootstyle='primary-outline')
    #pfaentry.grid(row=1,column=0,sticky='NW',pady=190,padx=1200,ipadx=10,ipady=10)

    pulseentry= tb.Entry(master,textvariable=pulse,font=("Latha",12),style='info.TEntry',bootstyle='primary-outline')
    pulseentry.grid(row=1,column=0,sticky='NW',pady=310,padx=600,ipadx=10,ipady=10)

    #Button

    caculatesnrButton= tb.Button(master,text="Calculate",command=snrcalc,style='primary.TButton')
    caculatesnrButton.grid(row=1,column=0,sticky='NW',pady=420,padx=650,ipadx=20,ipady=10)

    def callback1():
        webbrowser.open_new("https://in.mathworks.com/help/phased/ref/shnidman.html#d126e254937")

    #tk.Label(root, text=" You can plot LOS by clicking this button!").grid(row=12, column=1, pady=30)
    hy1 = tb.Button(master, text="Plot snr Online", bootstyle="light-link", command=callback1)
    hy1.grid(row=1,column=0,padx=850,pady=770,sticky='NW')

#Function to change window
def calculaterange():
    top = Toplevel()
    top.title('Range Calculator')
    top.geometry("{}x{}+0+0".format(top.winfo_screenwidth(), top.winfo_screenheight()))
    top.config(bg='#053B50')
    top.iconbitmap(r'C:\RadarCalculator\new_drdo_logo_3-removebg-preview.ico')
    #Labels
    centerlabel = tb.Label(top,text="Range Calculator",foreground='#64CCC5',background='#053B50',font=("Broadway",50))
    centerlabel.grid(row=0,column=0,sticky='NW', padx=550)

    antennatype=tb.Label(top, text="Select Transmitting Antenna Height",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    antennatype.grid(row=1,column=0,sticky='NW',padx=130,pady=50)

    opfreq=tb.Label(top,text="Operating frequency",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    opfreq.grid(row=1,column=0,sticky='NW',padx=890,pady=50)

    eff=tb.Label(top,text="Efficiency of receiver antenna",foreground='#EEEEEE',background='#176B87',font=("Latha",15),anchor="center")
    eff.grid(row=1,column=0,sticky='NW',padx=130,pady=220)



    #Radiobuttons

    r11=StringVar()
    r11.set('1')

    ghz=tb.Radiobutton(top,text="GHz",variable=r11,value='1')
    ghz.grid(row=1,column=0,sticky='NW',padx=1450,pady=55)

    mhz=tb.Radiobutton(top,text="MHz",variable=r11,value='2')
    mhz.grid(row=1,column=0,sticky='NW',padx=1600,pady=55)

    #Variable
    opfreq_value= StringVar()
    eff_value=StringVar()
    length_value1=StringVar()
    breath_value1=StringVar()
    length_value = StringVar()
    breath_value = StringVar()
    radius_value = StringVar()
    reff_value =StringVar()
    global wlen
    #Entry
    opfreqentry=tb.Entry(top,textvariable=opfreq_value,font=("Latha",12),style='info.TEntry')
    opfreqentry.grid(row=1,column=0,sticky='NW',padx=1180,pady=50)

    effentry=tb.Entry(top,textvariable=eff_value,font=("Latha",12),style='info.TEntry')
    effentry.grid(row=1,column=0,sticky='NW',padx=520,pady=220)

    #Fuction and Combobox for Transmitting antenna
    def parabola_frame():

        frame = tb.Frame(top,height=50,width=50)
        frame.grid(row=1, column=0, padx=150, pady=100, sticky='NW')

        global r4
        global diameter_value
        r4=StringVar()
        diameter_value= tb.StringVar()
        r4.set('1')
        firstmeter = tb.Radiobutton(frame, text="Metres", variable=r4, value='1')
        firstmeter.grid(row=1, column=2, padx=110, pady=10, sticky='NW')
        firstcenti = tb.Radiobutton(frame, text="Centimeter", variable=r4, value='0.01')
        firstcenti.grid(row=1, column=3, padx=130, pady=10, sticky='NW')
        firstinch = tb.Radiobutton(frame, text="inches", variable=r4, value='0.0254')
        firstinch.grid(row=1, column=4, padx=150, pady=10, sticky='NW')

        diameter = tb.Label(frame, text="Enter Diameter", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        diameter.grid(row=1, column=0, padx=20, pady=10, sticky='NW')
        diameterentry = tb.StringVar()
        diameterentry = tb.Entry(frame, textvariable=diameter_value).grid(row=1, column=1, padx=50, pady=0, sticky='NW', ipadx=30, ipady=5)

        return frame

    def circle_frame():

        frame = tb.Frame(top, height=50, width=50)
        frame.grid(row=1, column=0, padx=150, pady=100, sticky='NW')

        global r41


        r41 = StringVar()
        radius_value =StringVar()
        r41.set('1')
        secondmeter = tb.Radiobutton(frame, text="Metres", variable=r41, value='1')
        secondmeter.grid(row=1, column=2, padx=110, pady=10, sticky='NW')
        secondcenti = tb.Radiobutton(frame, text="Centimeter", variable=r41, value='0.01')
        secondcenti.grid(row=1, column=3, padx=130, pady=10, sticky='NW')
        secondinch = tb.Radiobutton(frame, text="inches", variable=r41, value='0.0254')
        secondinch.grid(row=1, column=4, padx=150, pady=10, sticky='NW')

        radius = tb.Label(frame, text="Enter Radius", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        radius.grid(row=1, column=0, padx=20, pady=10, sticky='NW')
        radiusentry = StringVar()
        radiusentry = tb.Entry(frame, textvariable=radius_value).grid(row=1, column=1, padx=50, pady=0, sticky='NW',ipadx=30, ipady=5)

        return frame

    def rectangle_frame():

        frame = tb.Frame(top, height=50, width=50)
        frame.grid(row=1, column=0, padx=150, pady=100, sticky='NW')

        global r42,r43

        r42 = StringVar()

        r42.set('1')

        r43 = StringVar()
        r43.set('1')

        ffirstmeter = tb.Radiobutton(frame, text="Metres", variable=r43, value='1')
        ffirstmeter.grid(row=2, column=2, padx=110, pady=10, sticky='NW')
        ffirstcenti = tb.Radiobutton(frame, text="Centimeter", variable=r43, value='0.01')
        ffirstcenti.grid(row=2, column=3, padx=130, pady=10, sticky='NW')
        ffirstinch = tb.Radiobutton(frame, text="inches", variable=r43, value='0.0254')
        ffirstinch.grid(row=2, column=4, padx=150, pady=10, sticky='NW')


        firstmeter = tb.Radiobutton(frame, text="Metres", variable=r42, value='1')
        firstmeter.grid(row=1, column=2, padx=110, pady=10, sticky='NW')
        firstcenti = tb.Radiobutton(frame, text="Centimeter", variable=r42, value='0.01')
        firstcenti.grid(row=1, column=3, padx=130, pady=10, sticky='NW')
        firstinch = tb.Radiobutton(frame, text="inches", variable=r42, value='0.0254')
        firstinch.grid(row=1, column=4, padx=150, pady=10, sticky='NW')

        length = tb.Label(frame, text="Enter Length", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        length.grid(row=1, column=0, padx=20, pady=10, sticky='NW')

        breadth=tb.Label(frame,text="Enter Breadth", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        breadth.grid(row=2, column=0, padx=20, pady=10, sticky='NW')

        lengthentry = tb.StringVar()
        lengthentry = tb.Entry(frame, textvariable=length_value).grid(row=1, column=1, padx=50, pady=0, sticky='NW',ipadx=30, ipady=5)

        breadthentry=tb.Entry(frame,textvariable=breath_value).grid(row=2, column=1, padx=50, pady=0, sticky='NW',ipadx=30, ipady=5)

        return frame
    #Combobox
    def selecting(event):
        global current_frames

        if my_comborange.get() == "Parabola":
            if current_frames:
                current_frames.grid_forget()
            current_frames = parabola_frame()
        elif my_comborange.get()=="Circle":
            if current_frames:
                current_frames.grid_forget()
            current_frames = circle_frame()
        else:
            if current_frames:
                current_frames.grid_forget()
            current_frames = rectangle_frame()

    options = ["Parabola","Circle","Rectangle"]

    my_comborange = tb.Combobox(top, values=options)
    my_comborange.grid(row=1, column=0, padx=580, pady=50, sticky='NW')
    my_comborange.current(1)
    my_comborange.bind("<<ComboboxSelected>>", selecting)

    #Function to calculate Transmitting Gain
    def calc_gt():
        global gt, wlen

        length_value_str=length_value.get()
        breath_value_str=breath_value.get()
        radius_value_str=radius_value.get()
        # wavelength
        if r11.get() == '2':
            freq = float(opfreq_value.get()) * (10 ** 6)
        else:
            freq = float(opfreq_value.get()) * (10 ** 9)
        c = 3 * (10 ** 8)
        wlen = c / freq
        # area trans
        if my_comborange.get() == "Circle":
            r = float(radius_value_str) * float(r41.get())
            ar = np.pi * (r ** 2)
        elif my_comborange.get() == "Parabola":
            di = float(diameter_value.get()) * float(r4.get())
            ar = np.pi * (di ** 2) / 4
        else:
            l = float(length_value_str) * float(r42.get())
            b = float(breath_value_str) * float(r43.get())
            ar = l * b
        # effective aperature tran
        aet = float(eff_value.get()) * ar
        # Transmitter Gain
        gt = 4 * np.pi * aet / (wlen) ** 2
        # linear to db
        gt_dB = 10 * np.log10(gt)
        tgain = tb.Label(top, text="Transmitter Gain : ", foreground='#EEEEEE', background='#053B50', font=("Latha", 15),anchor="center")
        tgain.grid(row=1, column=0, sticky='NW', padx=1150, pady=220)
        gtans=tb.Label(top, text=str(round(gt_dB, 2)) + ' dB', foreground='#EEEEEE', background='#053B50', font=("Latha", 15),anchor="center")
        gtans.grid(row=1, column=0,sticky='NW',padx=1450,pady=220)

    bu1 =tb.Button(top, text="Calculate Transmitter Gain", command=calc_gt).grid(row=1,column=0,sticky='NW',padx=900,pady=220)

    #Function and Combobox for Receiving antenna

    antennatype2 = tb.Label(top, text="Select Receiving Antenna Height", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    antennatype2.grid(row=1, column=0, sticky='NW', padx=130, pady=290)



    def parabola_1frame():

        frame1 = tb.Frame(top,height=50,width=50)
        frame1.grid(row=1, column=0, padx=150, pady=340, sticky='NW')

        global r46
        global diameter_value1
        r46=StringVar()
        diameter_value1= tb.StringVar()
        r46.set('1')
        firstmeter1 = tb.Radiobutton(frame1, text="Metres", variable=r46, value='1')
        firstmeter1.grid(row=1, column=2, padx=110, pady=5, sticky='WN')
        firstcenti1 = tb.Radiobutton(frame1, text="Centimeter", variable=r46, value='0.01')
        firstcenti1.grid(row=1, column=3, padx=130, pady=5, sticky='NW')
        firstinch1= tb.Radiobutton(frame1, text="inches", variable=r46, value='0.0254')
        firstinch1.grid(row=1, column=4, padx=150, pady=5, sticky='NW')

        diameter1 = tb.Label(frame1, text="Enter Diameter", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        diameter1.grid(row=1, column=0, padx=20, pady=5, sticky='WN')
        diameter1entry = tb.StringVar()
        diameter1entry = tb.Entry(frame1, textvariable=diameter_value1).grid(row=1, column=1, padx=50, pady=5, sticky='NW',ipadx=30, ipady=5)

        return frame1

    def circle_1frame():

        frame1 = tb.Frame(top, height=50, width=50)
        frame1.grid(row=1, column=0, padx=150, pady=340, sticky='NW')

        global r47
        global radius_value1

        r47 = StringVar()
        radius_value1 = tb.StringVar()
        r47.set('1')
        secondmeter = tb.Radiobutton(frame1, text="Metres", variable=r47, value='1')
        secondmeter.grid(row=1, column=2, padx=110, pady=5, sticky='WN')
        secondcenti = tb.Radiobutton(frame1, text="Centimeter", variable=r47, value='0.01')
        secondcenti.grid(row=1, column=3, padx=130, pady=5, sticky='WN')
        secondinch = tb.Radiobutton(frame1, text="inches", variable=r47, value='0.0254')
        secondinch.grid(row=1, column=4, padx=150, pady=5, sticky='WN')

        radius1 = tb.Label(frame1, text="Enter Radius", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        radius1.grid(row=1, column=0, padx=20, pady=0, sticky='NW')
        radiusentry1 = StringVar()
        radiusentry1 = tb.Entry(frame1, textvariable=radius_value1).grid(row=1, column=1, padx=50, pady=5, sticky='NW',ipadx=30, ipady=5)

        return frame1

    def rectangle_1frame():

        frame = tb.Frame(top, height=50, width=50)
        frame.grid(row=1, column=0, padx=150, pady=340, sticky='NW')

        global r42,r43
        r42 = StringVar()

        r42.set('1')

        r43 = StringVar()
        r43.set('1')

        ffirstmeter = tb.Radiobutton(frame, text="Metres", variable=r43, value='1')
        ffirstmeter.grid(row=2, column=2, padx=110, pady=5, sticky='NW')
        ffirstcenti = tb.Radiobutton(frame, text="Centimeter", variable=r43, value='0.01')
        ffirstcenti.grid(row=2, column=3, padx=130, pady=5, sticky='NW')
        ffirstinch = tb.Radiobutton(frame, text="inches", variable=r43, value='0.0254')
        ffirstinch.grid(row=2, column=4, padx=150, pady=5, sticky='NW')


        firstmeter = tb.Radiobutton(frame, text="Metres", variable=r42, value='1')
        firstmeter.grid(row=1, column=2, padx=110, pady=5, sticky='NW')
        firstcenti = tb.Radiobutton(frame, text="Centimeter", variable=r42, value='0.01')
        firstcenti.grid(row=1, column=3, padx=130, pady=5, sticky='NW')
        firstinch = tb.Radiobutton(frame, text="inches", variable=r42, value='0.0254')
        firstinch.grid(row=1, column=4, padx=150, pady=5, sticky='NW')

        length = tb.Label(frame, text="Enter Length", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        length.grid(row=1, column=0, padx=20, pady=5, sticky='NW')

        breadth=tb.Label(frame,text="Enter Breadth", foreground='#EEEEEE', font=("Latha", 12), anchor="center")
        breadth.grid(row=2, column=0, padx=20, pady=5, sticky='NW')

        lengthentry = tb.StringVar()
        lengthentry = tb.Entry(frame, textvariable=length_value1).grid(row=1, column=1, padx=50, pady=5, sticky='NW',ipadx=30, ipady=5)

        breadthentry=tb.Entry(frame,textvariable=breath_value1).grid(row=2, column=1, padx=50, pady=5, sticky='NW',ipadx=30, ipady=5)

        return frame
    #Combobox
    def selectingagain(event):
        global current_1frames

        if my_combo2range.get() == "Parabola":
            if current_1frames:
                current_1frames.grid_forget()
            current_1frames = parabola_1frame()
        elif my_combo2range.get()=="Circle":
            if current_1frames:
                current_1frames.grid_forget()
            current_1frames = circle_1frame()
        else:
            if current_1frames:
                current_1frames.grid_forget()
            current_1frames = rectangle_1frame()

    options1 = ["Parabola","Circle","Rectangle"]

    my_combo2range = tb.Combobox(top, values=options1)
    my_combo2range.grid(row=1, column=0, sticky='NW', padx=550, pady=290)
    my_combo2range.current(1)
    my_combo2range.bind("<<ComboboxSelected>>", selectingagain)

    #Efficiency of reciever
    reff=tb.Label(top,text="Efficiency of Receiver Antenna", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    reff.grid(row=1,column=0,padx=130,pady=470,sticky='NW')

    reffentry = tb.Entry(top, textvariable=reff_value)
    reffentry.grid(row=1, column=0, padx=520, pady=470, sticky='NW', ipadx=30, ipady=3)

    def calc_gr():
        global gr

        length_value1_str=length_value1.get()
        breath_value1_str=breath_value1.get()
        reff_value_str=reff_value.get()
        # area rec
        if my_combo2range.get() == "Circle":
            r1 = float(radius_value1.get()) * float(r47.get())
            ar1 = np.pi * (r1 ** 2)
        elif my_combo2range.get() == "Parabola":
            di1 = float(diameter_value1.get()) * float(r46.get())
            ar1 = np.pi * (di1 ** 2) / 4
        else:
            l1 = float(length_value1_str) * float(r42.get())
            b1 = float(breath_value1_str) * float(r43.get())
            ar1 = l1 * b1
        # effective aperature rec
        aer = float(reff_value.get()) * ar1
        # Transmitter Gain
        gr = 4 * np.pi * aer / (wlen) ** 2
        # linear to db
        gr_dB = 10 * np.log10(gr)
        rgainlabel=tb.Label(top,text="Receiver Gain :", foreground='#EEEEEE', background='#053B50', font=("Latha", 15),anchor="center")
        rgainlabel.grid(row=1,column=0,sticky='NW',padx=1150,pady=470)
        grans=tb.Label(top, text=str(round(gr_dB, 2)) + ' dB', foreground='#EEEEEE', background='#053B50', font=("Latha", 15),anchor="center")
        grans.grid(row=1,column=0,sticky='NW',padx=1350,pady=470)



    #Button to calculate reciever gain
    rgain=tb.Button(top,text="Calculate Receiver Gain",command=calc_gr)
    rgain.grid(row=1,column=0,sticky='NW',padx=900,pady=470)


    #Power

    pulsepower=tb.Label(top, text="Pulse Peak Power", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    pulsepower.grid(row=1,column=0,sticky='NW',padx=130,pady=530)
    pt = StringVar()
    pulsepowerentry=tb.Entry(top, textvariable=pt,font=("Latha",12),style='info.TEntry')
    pulsepowerentry.grid(row=1,column=0,sticky='NW',padx=400,pady=530)
    r51 = StringVar()
    r51.set('1')
    rb1=tb.Radiobutton(top, text="KW", variable=r51, value='2').grid(row=1,column=0,sticky='NW',padx=670,pady=540,ipadx=10)
    rb2=tb.Radiobutton(top, text="W", variable=r51, value='1').grid(row=1,column=0,sticky='NW',padx=760,pady=540,ipadx=10)
    rb3=tb.Radiobutton(top, text="dBm", variable=r51, value='3').grid(row=1,column=0,sticky='NW',padx=850,pady=540,ipadx=10)

    # Temperature
    ttemp=tb.Label(top, text="Operating Temperature", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    ttemp.grid(row=1,column=0,sticky='NW',padx=1050,pady=530,ipadx=0)
    tem = StringVar()
    tempentry=tb.Entry(top, textvariable=tem,font=("Latha",12),style='info.TEntry').grid(row=1,column=0,sticky='NW',padx=1350,pady=530,ipadx=0)
    r7 = StringVar()
    r7.set('0')
    rb4=tb.Radiobutton(top, text="Kelvin", variable=r7, value='0').grid(row=1,column=0,sticky='NW',padx=1650,pady=540,ipadx=0)
    rb5=tb.Radiobutton(top, text="Celcius", variable=r7, value='273.15').grid(row=1,column=0,sticky='NW',padx=1750,pady=540,ipadx=0)

    # RCS
    rcslabel=tb.Label(top, text="Radar Cross sectional area", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    rcslabel.grid(row=1,column=0,sticky='NW',padx=130,pady=590)
    rcs = StringVar()
    rcsentry=tb.Entry(top, textvariable=rcs,font=("Latha",12),style='info.TEntry').grid(row=1,column=0,sticky='NW',padx=460,pady=590)
    r67 = StringVar()
    r67.set('1')
    rb31=tb.Radiobutton(top, text="Sq m", variable=r67, value='1').grid(row=1,column=0,sticky='NW',padx=710,pady=595,ipadx=5)
    rb32=tb.Radiobutton(top, text="Sq cm", variable=r67, value='0.0001').grid(row=1,column=0,sticky='NW',padx=800,pady=595)
    rb33=tb.Radiobutton(top, text="Sq inch", variable=r67, value='0.00064516').grid(row=1,column=0,sticky='NW',padx=890,pady=595)

    # Bandwidth
    bandlabel=tb.Label(top, text="Bandwidth", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center").grid(row=1,column=0,sticky='NW',padx=1050,pady=590,ipadx=20)
    bw = StringVar()
    bandentry=tb.Entry(top, textvariable=bw).grid(row=1,column=0,sticky='NW',padx=1350,pady=590,ipadx=20)
    r8 = StringVar()
    r8.set('1')
    rb81=tb.Radiobutton(top, text="MHz", variable=r8, value='1').grid(row=1,column=0,sticky='NW',padx=1650,pady=595,ipadx=0)
    rb82=tb.Radiobutton(top, text="GHz", variable=r8, value='2').grid(row=1,column=0,sticky='NW',padx=1750,pady=595,ipadx=0)

    # Noise Figure
    noiselabel=tb.Label(top, text="Noise Figure", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    noiselabel.grid(row=1,column=0,sticky='NW',padx=130,pady=650,ipadx=10)
    nf = StringVar()
    noiseentry=tb.Entry(top, textvariable=nf).grid(row=1,column=0,sticky='NW',padx=370,pady=650)
    noiseunit=tb.Label(top, text="dB").grid(row=1,column=0,sticky='NW',padx=580,pady=655)

    # Losses
    losslabel=tb.Label(top, text="System Losses", foreground='#EEEEEE', background='#176B87',font=("Latha", 15), anchor="center")
    losslabel.grid(row=1,column=0,sticky='NW',padx=1050,pady=650,ipadx=10)
    lo = StringVar()
    lossentry=tb.Entry(top, textvariable=lo).grid(row=1,column=0,sticky='NW',padx=1350,pady=650,ipadx=20)
    lossunit=tb.Label(top, text="dBm").grid(row=1,column=0,sticky='NW',padx=1650,pady=650,ipadx=0)


    #function to calculate range
    def calc_range():
        k = 1.38 * (10 ** (-13))
        ans = Label(top, text='\t\t\t').grid(row=17, column=1)

        # freq and wavelen
        if r11.get() == '2':
            freq = float(opfreq_value.get()) * (10 ** 6)
        else:
            freq = float(opfreq_value.get()) * (10 ** 9)
        c = 3 * (10 ** 8)
        wlen = c / freq
        # power
        if r51.get() == '3':
            power = 10 ** ((float(pt.get()) - 30) / 10)

        elif r51.get() == '2':
            power = float(pt.get()) * 1000

        else:
            power = float(pt.get())
        # rcs
        sigma = float(rcs.get()) * float(r67.get())
        # temp
        temp = float(tem.get()) + float(r7.get())
        # bandwidth
        if r8.get() == '1':
            ban = float(bw.get()) * (10 ** 6)
        else:
            ban = float(bw.get()) * (10 ** 9)
        # Noise Figure
        nf1 = 10 * np.log10(float(nf.get()))

        # loss
        loss = 10 ** ((float(lo.get()) - 30) / 10)

        num = power * gt * gr * (wlen ** 2) * sigma
        denom = ((4 * np.pi) ** 3) * k * temp * ban * nf1 * loss
        Range = (num / denom) ** 0.25
        rangeans=tb.Label(top, text="Range :", foreground='#EEEEEE', background='#053B50',font=("Latha", 15), anchor="center")
        rangeans.grid(row=1,column=0,sticky='NW',padx=750,pady=770,ipadx=0)
        ans =tb.Label(top, text=str(round(Range, 2)) + ' m', foreground='#EEEEEE', background='#053B50',font=("Latha", 15), anchor="center")
        ans.grid(row=1,column=0,sticky='NW',padx=850,pady=770,ipadx=0)


    rangecalcbutton = tb.Button(top, text="Calculate Range", command=calc_range)
    rangecalcbutton.grid(row=1,column=0,sticky='NW',padx=550,pady=770,ipadx=0)

    def callback2():
        webbrowser.open_new("https://www.translatorscafe.com/unit-converter/en-US/calculator/radar-max-range/")

    #tk.Label(root, text=" You can plot LOS by clicking this button!").grid(row=12, column=1, pady=30)
    hy1 = tb.Button(top, text="Plot Range Online", bootstyle="light-link", command=callback2)
    hy1.grid(row=1,column=0,padx=1590,pady=810,sticky='NW')


#First window/ Welcome page

#Labels
center = tb.Label(text="Welcome",foreground='#64CCC5',background='#053B50',font=("Broadway",100))
center.pack(pady=40)

question = tb.Label(text="What do you want to calculate?",foreground='#EEEEEE',background='#053B50',font=("Ubuntu",25))
question.pack()

#buttons and style
my_style= tb.Style()
my_style.configure('info.Outline.TButton', font=("Terminal",28),background='#053B50',foreground='#64CCC5')

rangebutton = tb.Button(text="Range",bootstyle="info-outline",style="info.Outline.TButton", command=calculaterange)
rangebutton.pack(side=LEFT,padx=250,ipady=30,ipadx=30)

los= tb.Button(text="Los",style="info.Outline.TButton",command=calculatelos)
los.pack(side=LEFT,padx=100,ipady=30,ipadx=30)

snr = tb.Button(text="Snr",style="info.Outline.TButton",command=calculatesnr)
snr.pack(side=LEFT,padx=250,ipady=30,ipadx=30)


root.mainloop()
