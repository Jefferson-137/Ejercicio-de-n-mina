% Base de datos de empleados: nombre y horas trabajadas.
empleado(juan, 40). % Juan trabajó 40 horas.
empleado(ana, 35). % Ana trabajó 35 horas.
empleado(carlos, 45). % Carlos trabajó 45 horas.

% Tarifa por hora fija en pesos colombianos.
tarifa_hora(5652).

% Regla para calcular el salario en base a las horas trabajadas.
salario(Nombre, Salario) :-
    empleado(Nombre, Horas),
    tarifa_hora(Tarifa),
    Salario is Horas * Tarifa.
