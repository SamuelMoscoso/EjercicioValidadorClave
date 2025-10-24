from validadorclave.modelo.validador import (
    ReglaValidacionGanimedes,
    ReglaValidacionCalisto,
    Validador
)

def validar_clave(clave: str, reglas: list):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para {regla.__class__.__name__}")
        except Exception as e:
            print(f"Error: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    reglas = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]
    clave = input("Ingrese una clave para validar: ")
    validar_clave(clave, reglas)
