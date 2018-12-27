def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is a magician")


def make_great(magicians):
    number = len(magicians) - 1
    while number >= 0:
        magicians[number] = "the Great " + magicians[number]
        number -= 1
    return magicians


magicians = ['one', 'two', 'three']
show_magicians(magicians)
magicians_1=make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_1)
