import webbrowser
import time
total_breaks = 3
break_count = 0
print('bagaça rodando desde: '+time.ctime())
while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
    break_count = break_count + 1
print ('fim da bagça: ' +time.ctime())