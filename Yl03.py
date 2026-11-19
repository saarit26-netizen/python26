# Richard Saar 19.11.26

# Ülesanne 3.6: Python Turtle ruut
import turtle

kylje_pikkus = 100
nurk = 90
varv = "red"
edasi = kylje_pikkus

#esimene
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)

turtle.up()
edasi = edasi * 1.5
turtle.goto(edasi,0)
turtle.down()


#teine
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)

turtle.up()
edasi = edasi * 2
turtle.goto(edasi,0)
turtle.down()

#kolmas
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)

turtle.up()
turtle.goto(edasi,0)
turtle.down()


# Ülesanne 3.4: Lemmikraamat

raamatu_pealkiri = "Harry Potter and the Philosopher's Stone"
raamatu_autor = "J. K. Rowling"
raamat = raamatu_pealkiri+" "+raamatu_autor
lk = 300
skoor = 10.0
print("Minu lemmikraamat on "+raamat+" , mis on "+str(lk)+" lehekülge pikk ja mille ma hindan "+str(skoor)+" punktiga.")
#Ülesanne 3.2: Ostunimekiri
toode = "juust"
kogus = 50
hind = 15.50
print("Soovin "+toode+"porgandeid "+str(kogus)+", mille tüki hind on "+str(hind)+" eurot.")


