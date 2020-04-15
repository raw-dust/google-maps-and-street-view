import urllib.request

addresses = [ "Mady's Diner Jacksonville FL","3302 Hendricks Ave Jacksonville FL 32207","4378 Ocean St #3, Atlantic Beach, FL 32233","Hangar Bay, Atlantic Beach, FL 32233","219 N Hogan St, Jacksonville, FL 32202","6514 Norwood Ave, Jacksonville, FL 32208","7645 Merrill Rd UNIT 201, Jacksonville, FL 32277","1406 Hendricks Ave, Jacksonville, FL 32207","834 Kingsley Ave, Orange Park, FL 32073","6061 Merrill Rd, Jacksonville, FL 32277"]
apikey = "YOUR_API_KEY"

 
path = r"C:\FOLDER\TO\SAVE\PHOTOS"
mapsapiaddress = "http://maps.googleapis.com/maps/api/staticmap?"
streetviewapiaddress = "http://maps.googleapis.com/maps/api/streetview?"


for address in addresses:
    #maps
    data = urllib.parse.urlencode({"size":"600x400", "zoom":"13","key":apikey, "markers":address })
    with urllib.request.urlopen(mapsapiaddress+data) as response, open(path+"\\"+address+"_map.jpg", 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

    #street view
    data = urllib.parse.urlencode({"size":"600x400", "key":apikey, "location":address})    
    with urllib.request.urlopen(streetviewapiaddress+data) as response, open(path+"\\"+address+".jpg", 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

print("Done")
