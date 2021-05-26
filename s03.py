import eel
import desktop
import search

app_name ="html"
end_point ="index.html"
size = (700,600)

# JSに関数登録
@ eel.expose
def s03_search(word, csv_name):
    search.s03_search(word, csv_name)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

