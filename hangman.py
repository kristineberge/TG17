name = raw_input("Hva heter du? \n")

print "Hello, " + name + ", begynn aa gjette!"

print " "

# ordet som skal gjettes/losningsordet
word = "pannekaker"

# lager en String-variabel med tom verdi
guesses = ''

# definerer hvor mange ganger de skal faa gjette
turns = 10

# While-lokke
# sjekke om de har flere turns igjen/turns storre enn 0
while turns > 0:

    # lage en teller som begynner med 0
    failed = 0

    # for hvert tegn i det hemmelige ordet vaart/word
    for char in word:

    # se om tegnet er likt som noe vi har gjettet
        if char in guesses:

        # i saa fall printer vi ut tegnet
            print char,

        else:

        # hvis tegnet ikke er gjettet enda printes en understrek
            print "_",

        # og vi oeker feil-telleren vaar
            failed += 1

    # hvis den kan sjekke alle tegnene uten at noen er gjemt/ understrek skrives ikke ut = har altsaa gjettet alle tegn riktig!

    # i saa fall skrives det ut beskjed om at personen har vunnet!
    if failed == 0:
    	# \n betyr "new line", lager linjeskift for utskriften
        print "\nDu vant!!"

    # da er ogsaa scriptet ferdig..
        break

    print

    # her spor vi brukeren om input
    guess = raw_input("guess a character:")

    # legger til det de gjetter i guesses-variablen
    guesses += guess


    # hvis det de akkurat gjettet ikke finnes i det hemmelige ordet 
    if guess not in word:

     # reduseres antall turns med 1
        turns -= 1

    # og vi skriver ut at de har gjettet feil
        print "Feil!"

    # skriver ogsaa ut hvor mange gjett/turns de har igjen
        print "Du har ", + turns, ' ganger aa gjette igjen!'

    # hvis turns blir 0 saa har de ingen flere gjett igjen
        if turns == 0:

        # da skrives det ut at man har tapt
            print "Du tapte!"
