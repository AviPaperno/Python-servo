import serial


class DigitalServo:
    """
    It's class for connecting and mooving sigital servos TS-315 
    """
    #----------------------------------------------------------------------
    def __init__(self, port,baudrate = 9600):
        try:
            self.servo_channel = serial.Serial(port)
            self.servo_channel.baudrate = baudrate
        except:
            print('Exception. Serial connection not found')
        self.servo_count = 0
        
    def init_count(self):
        pass
    
    def set_mono_position(self,number_of_serv,position,timeout):
        '''
        Set one of servo to position, with time
        '''
        data = "#{}P{}T{}\r\n".format(number_of_serv,position,timeout)
        self.servo_channel.write(data.encode('utf-8'))
        
    def send_multi_position(self,Array_of_Servos,timeout):
        data = ""
        for i in Array_of_Servos:
            data+="#"+str(i[0])+"P"+str(i[1])
        data+="T"+str(timeout)+"\r\n"
        self.servo_channel.write(data.encode('utf-8'))
        
    def read_mono_position(self,Number_of_Servo):
        data="#{}PRAD\r\n".format(Number_of_Servo)
        self.servo_channel.write(data.encode('utf-8'))
        pos=self.servo_channel.readline().decode('utf-8')
        return pos.split('P')[1]
    
    def manual_mode_on(self,number_of_serv):
        data="#{}PULK\r\n".format(number_of_serv)
        self.servo_channel.write(data.encode('utf-8'))
    def manual_mode_off(self,number_of_serv):
        data="#{}PULR\r\n".format(number_of_serv)
        self.servo_channel.write(data.encode('utf-8'))    
    def hard_reset(self,number_of_serv):
        data="#{}PCLE0\r\n".format(number_of_serv)
        self.servo_channel.write(data.encode('utf-8'))      
    def lock(self,number_of_serv):
        data="#{}PDPT\r\n".format(number_of_serv)
        self.servo_channel.write(data.encode('utf-8'))     
    def unlock(self,number_of_serv):
        data="#{}PDCT\r\n".format(number_of_serv)
        self.servo_channel.write(data.encode('utf-8'))             
        
        

        
    
My = DigitalServo(port='/dev/tty.wchusbserial1410')
while 1:
    a = input()
    if (a == '0'):
        print (My.read_mono_position(1))
    elif (a == '1'):
        pos = input()
        My.set_mono_position(1,pos,500)
    elif(a =='2'):
        My.manual_mode_on(1)
    elif(a =='3'):
        My.manual_mode_off(1)  
    elif (a == '4'):
        My.lock(1)
    elif (a == '5'):
        My.unlock(1)
    else:
        break