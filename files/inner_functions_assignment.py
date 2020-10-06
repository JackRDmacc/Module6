def measurements(list):
    def area(a_list):
        return a_list[0] * a_list[1]

    def perimeter(a_list):
        return (a_list[0] * 2) + (a_list[1] * 2)

    return "Perimeter = " + str(perimeter(list)) + " Area = " + str(area(list))
