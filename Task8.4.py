class TV:
    def __init__(self, b , p , i, onf):
         self.brand = b 
         self.channel = 1
         self.price =p
         self.inches = i
         self.OnOFF_status =onf
         self.volume = 25 
    
    def increase_volume(self):
        if self.volume == 50:
            print("Volume is maxium")
        self.volume = self.volume+1
        print("Volme is increased and set to", self.volume)
    
    def decrease_volume(self):
        if self.volume == 0:
            print("Volume is minimum")
        self.volume = self.volume-1
        print("Volme is decreased and set to", self.volume)

    def set_Channel(self,channel):
        if self.channel < 0 or self.channel > 50:
            print("Invalid Channel number entered")
        self.channel = channel
        print("Channel is set to", self.channel)

    def reset_TV(self):
        #self.__init__(True)
        self.channel = 1
        self.volume = 25
        print("Channel Number after reset is:" , self.channel)
        print("Volume  after reset is:" , self.volume)
    
    def show_TVstatus(self):
        print("TV Brand is",  self.brand ,"TV Channel is",  self.channel , "TV Volume is",  self.volume)

################################ Plasma Inheriting TV class
class plasma(TV):
    def __init__(self,  screen_thickness, energy_usage , Lifespan , Refresh_rate, viewing_Angle , backlight, b , p , i, onf  ):
        ## calling super class constructor
        super().__init__(b , p , i, onf)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate = Refresh_rate
        self.viewing_Angle = viewing_Angle
        self.backlight = backlight 

    def show_viewingAngle(self):
        print("viewing Angle is", self.viewing_Angle ) 

    def show_backlight(self):
        print("Backlight is", self.backlight ) 


    def show_DisplayDetails(self):
        print("energy usage is",  self.energy_usage)
        print("screen thickness is",  self.screen_thickness)
        print("Lifespan is",  self.Lifespan)
        print("Refresh rate is",  self.Refresh_rate)
        print("Backlight is",  self.backlight)


################################ LED Inheriting TV class
class LED(TV):
    def __init__(self,  screen_thickness, energy_usage , Lifespan , Refresh_rate, viewing_Angle , backlight, b , p , i, onf  ):
        ## calling super class constructor
        super().__init__(b , p , i, onf)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate = Refresh_rate
        self.viewing_Angle = viewing_Angle
        self.backlight = backlight 

    def show_viewingAngle(self):
        print("viewing Angle is", self.viewing_Angle ) 

    def show_backlight(self):
        print("Backlight is", self.backlight ) 


    def show_DisplayDetails(self):
        print("energy usage is",  self.energy_usage)
        print("screen thickness is",  self.screen_thickness)
        print("Lifespan is",  self.Lifespan)
        print("Refresh rate is",  self.Refresh_rate)
        print("Backlight is",  self.backlight)

 
    
Tv1= TV( "lg" ,1000,32,"off")
Tv1.increase_volume()
Tv1.decrease_volume()
Tv1.set_Channel(44)
Tv1.show_TVstatus()
Tv1.reset_TV()
Tv1.show_TVstatus()
print("########### Plasma TV ######################")

plasma1 = plasma("20mm", "150W", "10 Years" , "120" , "180 degree", "Plasma", "SONY","75000","75 inch","ON")
plasma1.show_viewingAngle()
plasma1.show_backlight()
plasma1.show_DisplayDetails()
plasma1.show_TVstatus()

print("########## LED TV #######################")

LED1 = LED("40mm", "300W", "20 Years" , "240" , "180 degree", "LED", "SAMSUNG","150000","85 inch","ON")
LED1.show_viewingAngle()
LED1.show_backlight()
LED1.show_DisplayDetails()
LED1.show_TVstatus()




