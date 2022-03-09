def person(age):
    print("I am a person")
    
    def student(major):
        print("I like learning")
        
        def vacation(place):
            print("But I need to take breaks")
            print(age, "|", major, "|", place)
        return vacation
    return student


person(29)("CS")("SouthKorea")
person(23)("Law")("NorthKorea")
