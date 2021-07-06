# def mi_funcion(nS:int, nM:int, nW:int, wS:int, oS:int):
#     wS_perc = (wS/nS)*100
#     r_wSperc = round(wS_perc, 1)
#     oS_perc = (oS/nS)*100
#     r_oSperc = round(oS_perc, 1)
#     women_perc = (nW/nS)*100
#     r_wperc = round(women_perc, 1)
#     men_perc = (nM/nS)*100
#     r_mperc = round(men_perc, 1)
#     return(f"Porcentaje de estudiantes que trabajan: {wS_perc}, Porcentaje de estudiantes que solo estudian: {oS_perc}, Porcentaje de mujeres es: {women_perc}, Porcentaje de hombres: {men_perc}")
# print(mi_funcion(8,4,4,3,5))

# nS = int(input("Ingrese la cantidad de estudiantes de su grupo: "))
# nM = int(input("Del total, ¿cuántos son hombres?: "))
# nW = int(input("Del total, ¿cuántas son mujeres?: "))
# wS = int(input("Del total, ¿cuántos estudian y trabajan?: "))
# oS = int(input("Del total, ¿cuántos estudian solamente?: "))
# def mi_funcion(nS:int, nM:int, nW:int, wS:int, oS:int):
#     wS_perc = (wS/nS)*100
#     r_wSperc = round(wS_perc, 1)
#     oS_perc = (oS/nS)*100
#     r_oSperc = round(oS_perc, 1)
#     women_perc = (nW/nS)*100
#     r_wperc = round(women_perc, 1)
#     men_perc = (nM/nS)*100
#     r_mperc = round(men_perc, 1)
#     return(f"Porcentaje de estudiantes que trabajan: {wS_perc}, Porcentaje de estudiantes que solo estudian: {oS_perc}, Porcentaje de mujeres es: {women_perc}, Porcentaje de hombres: {men_perc}")
# print(mi_funcion(nS, nM, nW, wS, oS))

#Reto 1 grupo 85

def reto_1(F1:float, d:int, C1:float) -> str:
    R1 = (d/2)/100
    A1 = round((3.14*R1**2), 4)
    P1 = round((2*3.14*R1), 3)
    A2 = round(3.14*((R1*C1)**2), 4)
    F2 = (A2/A1)*F1
    F1 = f'F1 = {F1:.1F} N'
    A1 = f'A1 = {A1} m2'
    R1 = f'r1 = {R1} m2'
    P1 = f'P1 = {P1} m2'
    F2 = f'F2 = {F2:.1F} N'
    A2 = f'A2 = {A2} m2'
    return F1, A1, R1, P1, F2, A2

print(reto_1(-235, 345, 1/8))

# def  calculadoraRectangulo(ancho:float,largo:float)->str:
#     perimeter = 2*(ancho+ largo)
#     area = (ancho*largo)
#     return(f"El cuadrado tiene un perimetro de: {perimeter} y un área de: {area}")

# print(calculadoraRectangulo(5.5, 3.5))