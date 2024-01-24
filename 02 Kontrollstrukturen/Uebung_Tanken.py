priceGasoline=1.90
priceDiesel=1.80
tankVolume=int(input ("Tankmenge eingeben: "))
tankType=int(input ("Bitte Tanksorte eingeben (1=Benzin, 2= Diesel): "))

price=0
if(tankType == 1):
    price=priceGasoline
else: 
    price=priceDiesel

if(tankVolume >= 100):
    price=price*0.95

costs=price*tankVolume
print("Der Tankvorgang kostet: " + str(costs))
