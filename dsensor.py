from gpiozero import MCP3002
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import numpy as np
import RPi.GPIO as GPIO

def main():
    # 計算用の3.3V
    Vref = 3.3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    volVal = []

    # 初期化
    factory = PiGPIOFactory(host=)
    adc_ch0 = MCP3002(channel=1, max_voltage=Vref, pin_factory=factory)

    try:
        while True:
            # MCP3002からの出力値と電圧値を表示
            #print(f'value:{adc_ch0.value:.2f}, Volt:{adc_ch0.value * Vref:.2f}')
            volVal.append(adc_ch0.value * Vref)
            #print(adc_ch0.value)
            if len(volVal)==20:
                meanVolVal = np.array(volVal).mean()          
                print(meanVolVal)
                volVal =[]
                if 1.5 < meanVolVal < 1.7:
                    GPIO.output(17,1)
                else:
                    GPIO.output(17,0)
            sleep(0.1)

    except KeyboardInterrupt:
        GPIO.cleanup() 
    return


if __name__ == "__main__":
    main()
