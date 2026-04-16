from services.vectors import VectorCalculated


import math

# (Tu clase va aquí tal cual)

def main():
    vc = VectorCalculated()

    # 🔢 Datos de prueba (puedes cambiarlos)
    forceOne = 200
    thetaOne = math.radians(0)  # IMPORTANTE: radianes
    forceTwo = 200
    thetaTwo = math.radians(120)

    print("=== DESCOMPOSICIÓN DE FUERZAS ===")
    vectors = vc.teoricVectorTwoForce(forceOne, thetaOne, forceTwo, thetaTwo)
    print(vectors)

    print("\n=== RESULTANTE ===")
    result = vc.resultForce()
    print(result)

    print("\n=== FUERZA EQUILIBRANTE ===")
    balancing = vc.balancingForce()
    print(balancing)

    print("\n=== MAGNITUD RESULTANTE ===")
    magnitude = vc.magnitudeForceResult()
    print(magnitude)

    print("\n=== ÁNGULO RESULTANTE ===")
    angle_result = vc.moduleResultForce()
    print(math.degrees(angle_result))  # lo paso a grados

    print("\n=== ÁNGULO EQUILIBRANTE ===")
    angle_balancing = vc.moduleBalancingForce()
    print(angle_balancing)

    print("\n=== DESCOMPOSICIÓN INDIVIDUAL ===")
    decomposition = vc.decompositionForce(200, math.radians(45))
    print(decomposition)


if __name__ == "__main__":
    main()