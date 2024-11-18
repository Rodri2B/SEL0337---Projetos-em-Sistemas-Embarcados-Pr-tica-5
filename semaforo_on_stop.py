import RPi.GPIO as GPIO
import time

red_pin=9 #define o pino do led vermelho
green_pin=10 #define o pino do led verde
blue_pin=11 #define o pino do led azul


if __name__ == '__main__':

    try:
        GPIO.cleanup() # Limpa a configuração dos pinos GPIO      
 
        GPIO.setmode(GPIO.BCM) #configurando o modo do gpio

        GPIO.setup(red_pin , GPIO.OUT) #configurando o pino do led vermelho como saida
        GPIO.setup(green_pin , GPIO.OUT) #configurando o pino do led verde como saida
        GPIO.setup(blue_pin , GPIO.OUT) #configurando o pino do led azul como saida


        GPIO.output(red_pin , GPIO.LOW) #desligando led vermelho
        GPIO.output(red_pin , GPIO.LOW) #desligando led verde
        GPIO.output(red_pin , GPIO.LOW) #desligando led azul

        #loop para implementar a função do semaforo
        while (True):
            #liagndo luz vermelha
            GPIO.output(red_pin , GPIO.HIGH) #ligando led vermelho
            GPIO.output(green_pin , GPIO.LOW) #desligando led verde
            time.sleep(1)
            #ligando luz amarela
            GPIO.output(green_pin , GPIO.HIGH) #ligando led verde
            time.sleep(1)
            #ligando luz verde
            GPIO.output(red_pin , GPIO.LOW) #desligando led vermelho
            time.sleep(1)
        
    
    except KeyboardInterrupt: # interrupção do teclado (Ctrl+C).
        print("Processo interrompido.")
    finally:
        GPIO.cleanup() # Limpa a configuração dos pinos GPIO ao encerrar o script.

