from ckanapi import RemoteCKAN
import urllib
import easygui as gui
import sys
import os

# sourcs: name, download base, access url
sources = [
           (u"berlin","berlin.de","https://datenregister.berlin.de/"),\
           (u"karlsruhe","karlsruhe.de","https://transparenz.karlsruhe.de/"),\
           (u"bahn","deutschebahn.com","https://data.deutschebahn.com/"),\
           (u"offeneDaten","offenedaten.de/","https://offenedaten.de/"),\
           (u"muenchen","opengov-muenchen.de","https://www.opengov-muenchen.de"),\
           (u"meerbusch","meerbusch.de","https://opendata.meerbusch.de/"),\
           (u"bonn","bonn.de","https://opendata.bonn.de/"),\
           (u"jena","jena.de","https://opendata.jena.de/"),\
           (u"africa","africaopendata.org","https://africaopendata.org/")\
           ]

# file types we want to download
downs = (".csv",".json",".geojson",".gpx",".kmz",".xls",".xlx",".ods",".xlsx",".pdf")
download = True # Download file or not
excludext = True # exclude external resources or not. 


#########
def config():
    """ Ask user which file types to download"""
    choices = []
    for s in sources:
        choices.append(s[0])
           
    choice = gui.choicebox("Select CKAN origin",\
                               "Source select",\
                               choices)
    if choice != None:
           for c in range(len(sources)):
               if choice == sources[c][0]:
                   choice = c
                   print("Selected: ",choice)
                   break
    return choice

#########

def loadUrl(p,u):
    """ load file from url, print 404 error or raise"""
    f = filedir + "/" + p + "_" + u[u.rfind("/")+1:]
        
    try:
        urllib.request.urlretrieve(u,f)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print("URL not found: ",u)
        else:
            raise

#########

# prepare ...
agent = 'ckanapi/3.0 (+http://digital-codes.de)'
sel = config()

if sel == None:
    sys.exit(0)

filedir = "files-" + sources[sel][0]
if not os.path.exists(filedir):
    os.makedirs(filedir)
    
downloadBase = sources[sel][1]
ckanGet = RemoteCKAN(sources[sel][2],user_agent=agent)

# access
grps = ckanGet.action.group_list()
print("Groups:\n",grps)
##for g in grps:
##    print("Group: ",ckanGet.action.group_show(id=g))

pkgs = ckanGet.action.package_list()
print("Packages:\n",pkgs)

# reset our list of resource files
items = []

# iterate over packages and resources
for p in pkgs:
    try:
        pk = ckanGet.action.package_show(id=p)
    except ckanapi.errors.NotFound:
        print("Package not found: ",p)
        continue
    
    print("################")
    print("\n\nPackage ",p)
    gp = pk.get("groups")
    gpname = ""

    if gp != None:
        for g in gp:
            gpname = g.get("name")
            if gpname is None:
                gpname = g.get("title")
            if gpname is None:
                gpname = "no name"
                
            print("Group: ",gpname)

    #print("\nKeys in package ",p,": ",pk.keys())
    #for k in pk.keys():
    #    print(k,": ",pk.get(k))
    #print("\nTitle: ",pk.get("title"),", Notes: ",pk.get("notes"))
    
    u = pk.get("url")
    if None != u and u != "":
        print("Url:", u)
        
    r = pk.get("resources")
    if None != r:
        print("#########")
        for rr in r:
            #print("\nKeys in resource: ",rr.keys())
            ru = rr.get("url")
            print("\nResource: ",ru)
            # check and skip external urls
            try:
                if excludext and ru.find(downloadBase) < 0:
                    print("External url: ",ru)
                    continue

                if None != ru:
                    ri = []
                    for x in (p,gpname,pk.get("title"),pk.get("license_id"),pk.get("notes"),rr.get("name"),rr.get("description"),rr.get("last_modified"),ru):
                        if type(x) == str:
                            x = "\"" + x + "\""
                        else:
                            x = ""
                        ri.append(x.encode('utf-8').strip())
                    items.append(ri)
                    rf,re = os.path.splitext(ru)
                    #print("File: ",rf, ": ", re)
                    
                    if download and re.lower() in downs:
                        loadUrl(p,ru)

                        
            except urllib.error.URLError:
                print("url error")
                pass


# write resource description to csv
itemfile = open("items-"+sources[sel][0]+".csv", 'w')
# for some reason, we need a string join here ..
fieldnames = (u"\"package\"",u"\"group\"",u"\"title\"",u"\"license_id\"",u"\"notes\"",u"\"name\"",\
              u"\"description\"",u"\"last_modified\"",u"\"url\"")
itemfile.write(u",".join(fieldnames)+u"\n")

# and a byte join here
for i in items:
    itemfile.write((b",".join(i)+b"\n").decode("utf-8"))

itemfile.close()

    
