# Aplicación introductoria de árbol binario

Implementación en Python sin clases ni dependencias externas. Cada nodo se representa con un diccionario que contiene su dato y las referencias a los hijos izquierdo y derecho.

## Funcionalidades

- Crear nodos y enlazar hijos a la izquierda o a la derecha.
- Mostrar el árbol con una representación jerárquica.
- Identificar hojas y nodos internos.
- Obtener relaciones padre-hijo.
- Recorrer el árbol en preorden y calcular su altura.
- Probar árboles vacíos, de un nodo, con varios niveles y con un solo hijo.

## Diagrama del ejemplo

```text
A
├── izquierdo: B
│   ├── izquierdo: D
│   └── derecho: E
└── derecho: C
    └── derecho: F
        └── izquierdo: G
```

La raíz es `A`, los nodos internos son `A`, `B`, `C` y `F`, y las hojas son `D`, `E` y `G`. La altura es `3` contando las aristas del camino más largo desde la raíz hasta una hoja.

## Archivos

- `arbol_binario.py`: implementación y demostración del árbol.
- `test_arbol_binario.py`: pruebas de los casos requeridos.

## Ejecución

```bash
python arbol_binario.py
python test_arbol_binario.py
```

El segundo comando muestra `Todas las pruebas pasaron.` cuando todos los casos son correctos.
