import geocoder

def getLocation():
    g = geocoder.ip('me')
    return f"This is - {g.latlng}"

print(getLocation())