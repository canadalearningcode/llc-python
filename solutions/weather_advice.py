weather = "snowing"
temperature = -15
if weather == "snowing" and temperature < -40:
    print("Stay home")
if weather == "snowing" and temperature > -20 and temperature < -10:
    print("Wear long johns")
elif weather == "raining":
      print("Bring an umbrella")
else:
      print("Who knows?")
