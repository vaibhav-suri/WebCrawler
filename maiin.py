from urllib import  request

def csv_maker(url) :
    comehere=request.urlopen(url)
    csv= comehere.read()
    csv_str = str(csv)
    lines=csv_str.split("\\n")
    dest_url= "datacollected.csv"
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()

csv_maker("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv")

