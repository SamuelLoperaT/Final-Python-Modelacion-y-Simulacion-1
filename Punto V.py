import random as rd

precio = 1.5
venta = 2.5
reemb = 0.5
dias = 30
i = 40
j = 0.0
while(i <= 70):
    print('periodicos comprados = ', i)
    utilidad = 0
    for j in range(dias):
        per_vendidos = rd.randint(40, 70)
        if (i-per_vendidos) <= 0:
            utilidad_diaria = per_vendidos*venta - i*precio
            utilidad += utilidad_diaria
        else:
            utilidad_diaria = per_vendidos*venta - i*precio + (i-per_vendidos)*0.5
            utilidad += utilidad_diaria
    print('utilidad con ',i ,'periodicos: ', utilidad,'$')
    
    i += 5
