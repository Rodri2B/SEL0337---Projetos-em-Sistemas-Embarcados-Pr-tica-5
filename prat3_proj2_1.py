import RPi.GPIO as GPIO
from time import sleep


if __name__ == '__main__':

    try:
        GPIO.setmode(GPIO.BCM) #configurando o modo do gpio

        pwm_pin  = 12 #definindo pino de pwm

        GPIO.setup(pwm_pin , GPIO.OUT) #configurando o pino 12 como saida

        pwm = GPIO.PWM(pwm_pin , 100) #configuando o pwm no pino 12
        pwm.start (0) #inicializando pwm com duty cycle 0


        pwm.ChangeDutyCycle(10) #configurando o duty cycle para 10%
        
        #loop para previnir o programa de fechar
        while True:
            sleep(1)
    
    except KeyboardInterrupt: # interrupção do teclado (Ctrl+C).
        print("Processo interrompido.")
    finally:
        GPIO.cleanup() # Limpa a configuração dos pinos GPIO ao encerrar o script.
