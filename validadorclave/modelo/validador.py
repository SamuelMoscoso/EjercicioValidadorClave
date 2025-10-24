from abc import ABC, abstractmethod

# ======================
#  CLASE ABSTRACTA BASE
# ======================

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        """Método abstracto que debe implementar cada regla"""
        pass



# ================================
#  CLASE: Validación Ganímedes
# ================================

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)  # longitud esperada: más de 8

    def _contiene_caracter_especial(self, clave: str) -> bool:
        especiales = "@_#$%&"
        return any(c in especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise Exception("ReglaValidacionGanimedes: La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise Exception("ReglaValidacionGanimedes: La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise Exception("ReglaValidacionGanimedes: La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise Exception("ReglaValidacionGanimedes: La clave debe contener al menos un número")
        if not self._contiene_caracter_especial(clave):
            raise Exception("ReglaValidacionGanimedes: La clave debe contener al menos un carácter especial (@, _, #, $, %, &)")
        return True


