def crear_nodo(dato):
    return {"dato": dato, "izquierdo": None, "derecho": None, "_padre": None}


def enlazar_hijo(padre, hijo, lado):
    if padre is None or hijo is None:
        raise ValueError("El padre y el hijo deben existir.")
    if not isinstance(padre, dict) or not isinstance(hijo, dict):
        raise ValueError("Los nodos deben ser diccionarios.")
    if lado not in ("izquierdo", "derecho"):
        raise ValueError("El lado debe ser 'izquierdo' o 'derecho'.")
    if padre is hijo:
        raise ValueError("Un nodo no puede ser hijo de sí mismo.")
    if padre.get(lado) is not None:
        raise ValueError(f"El nodo {padre['dato']} ya tiene un hijo en {lado}.")
    if hijo.get("_padre") is not None and hijo["_padre"] is not padre:
        raise ValueError("El hijo ya pertenece a otro padre.")
    if padre.get("_padre") is hijo:
        raise ValueError("No se puede crear un ciclo de referencia.")

    hijo["_padre"] = padre
    padre[lado] = hijo


def recorrer_preorden(raiz):
    if raiz is None:
        return []
    return [raiz["dato"]] + recorrer_preorden(raiz["izquierdo"]) + recorrer_preorden(raiz["derecho"])


def identificar_hojas(raiz):
    if raiz is None:
        return []
    if raiz["izquierdo"] is None and raiz["derecho"] is None:
        return [raiz["dato"]]

    hojas = []
    if raiz["izquierdo"] is not None:
        hojas.extend(identificar_hojas(raiz["izquierdo"]))
    if raiz["derecho"] is not None:
        hojas.extend(identificar_hojas(raiz["derecho"]))
    return hojas


def identificar_nodos_internos(raiz):
    if raiz is None:
        return []

    internos = []
    if raiz["izquierdo"] is not None or raiz["derecho"] is not None:
        internos.append(raiz["dato"])
    if raiz["izquierdo"] is not None:
        internos.extend(identificar_nodos_internos(raiz["izquierdo"]))
    if raiz["derecho"] is not None:
        internos.extend(identificar_nodos_internos(raiz["derecho"]))
    return internos


def obtener_relaciones(raiz):
    if raiz is None:
        return []

    relaciones = []
    if raiz["izquierdo"] is not None:
        relaciones.append((raiz["dato"], "izquierdo", raiz["izquierdo"]["dato"]))
    if raiz["derecho"] is not None:
        relaciones.append((raiz["dato"], "derecho", raiz["derecho"]["dato"]))
    if raiz["izquierdo"] is not None:
        relaciones.extend(obtener_relaciones(raiz["izquierdo"]))
    if raiz["derecho"] is not None:
        relaciones.extend(obtener_relaciones(raiz["derecho"]))
    return relaciones


def altura_arbol(raiz):
    if raiz is None:
        return -1
    return 1 + max(altura_arbol(raiz["izquierdo"]), altura_arbol(raiz["derecho"]))


def mostrar_arbol(raiz):
    if raiz is None:
        print("Árbol vacío: raiz = None")
        return

    print(raiz["dato"])

    def mostrar_hijos(nodo, prefijo):
        hijos = []
        if nodo["izquierdo"] is not None:
            hijos.append(("izquierdo", nodo["izquierdo"]))
        if nodo["derecho"] is not None:
            hijos.append(("derecho", nodo["derecho"]))

        for indice, (lado, hijo) in enumerate(hijos):
            es_ultimo = indice == len(hijos) - 1
            conector = "└── " if es_ultimo else "├── "
            print(f"{prefijo}{conector}{lado}: {hijo['dato']}")
            nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
            mostrar_hijos(hijo, nuevo_prefijo)

    mostrar_hijos(raiz, "")


def construir_ejemplo():
    raiz = crear_nodo("A")
    b = crear_nodo("B")
    c = crear_nodo("C")
    d = crear_nodo("D")
    e = crear_nodo("E")
    f = crear_nodo("F")
    g = crear_nodo("G")

    enlazar_hijo(raiz, b, "izquierdo")
    enlazar_hijo(raiz, c, "derecho")
    enlazar_hijo(b, d, "izquierdo")
    enlazar_hijo(b, e, "derecho")
    enlazar_hijo(c, f, "derecho")
    enlazar_hijo(f, g, "izquierdo")
    return raiz


def ejecutar_demo():
    raiz = construir_ejemplo()
    print("Preorden:", recorrer_preorden(raiz))
    print("Hojas:", identificar_hojas(raiz))
    print("Altura:", altura_arbol(raiz))
    print("Relaciones:", obtener_relaciones(raiz))
    mostrar_arbol(raiz)


if __name__ == "__main__":
    ejecutar_demo()
