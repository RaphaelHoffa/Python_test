import time
import webbrowser

breaks = 3
c_breaks = 0

print ("Tempo para iniciou: " + time.ctime())
while (c_breaks < breaks):
    time.sleep(10) #Espera por x segundos
    webbrowser.open("https://www.youtube.com/watch?v=jRGrNDV2mKc")
    c_breaks = c_breaks + 1
