# translator.py
from lexer import lexer
from parser import parser


# Generación de Código C
def generate_c_code(node):
    if isinstance(node, list):
        return "\n".join(generate_c_code(stmt) for stmt in node)
    elif node[0] == 'NUM':
        return str(node[1])
    elif node[0] == 'ID':
        return node[1]
    elif node[0] in ('ADD', 'PLUS'):
        return f"({generate_c_code(node[1])} + {generate_c_code(node[2])})"
    elif node[0] in ('SUB', 'MINUS'):
        return f"({generate_c_code(node[1])} - {generate_c_code(node[2])})"
    elif node[0] in ('MUL', 'TIMES'):
        return f"({generate_c_code(node[1])} * {generate_c_code(node[2])})"
    elif node[0] in ('DIV', 'DIVIDE'):
        return f"({generate_c_code(node[1])} / {generate_c_code(node[2])})"
    elif node[0] == 'POW':
        return f"pow({generate_c_code(node[1])}, {generate_c_code(node[2])})"
    elif node[0] == 'MOD':
        return f"({generate_c_code(node[1])} % {generate_c_code(node[2])})"
    elif node[0] == 'GT':
        return f"({generate_c_code(node[1])} > {generate_c_code(node[2])})"
    elif node[0] == 'LT':
        return f"({generate_c_code(node[1])} < {generate_c_code(node[2])})"
    elif node[0] == 'GE':
        return f"({generate_c_code(node[1])} >= {generate_c_code(node[2])})"
    elif node[0] == 'LE':
        return f"({generate_c_code(node[1])} <= {generate_c_code(node[2])})"
    elif node[0] == 'EQ':
        return f"({generate_c_code(node[1])} == {generate_c_code(node[2])})"
    elif node[0] == 'NE':
        return f"({generate_c_code(node[1])} != {generate_c_code(node[2])})"
    elif node[0] == 'ASSIGN':
        return f"{node[1]} = {generate_c_code(node[2])};"
    elif node[0] == 'PRINT':
        return f'printf("%d\\n", {generate_c_code(node[1])});'
    elif node[0] == 'IF':
        return f"if ({generate_c_code(node[1])}) {{\n{generate_c_code(node[2])}\n}}"
    elif node[0] == 'IF_ELSE':
        return f"if ({generate_c_code(node[1])}) {{\n{generate_c_code(node[2])}\n}} else {{\n{generate_c_code(node[3])}\n}}"
    elif node[0] == 'WHILE':
        return f"while ({generate_c_code(node[1])}) {{\n{generate_c_code(node[2])}\n}}"
    elif node[0] == 'FOR':
        return f"for (int {node[1]} = 0; {node[1]} < {generate_c_code(node[2])}; {node[1]}++) {{\n{generate_c_code(node[3])}\n}}"
    elif node[0] == 'LIST':
        return f"{{{', '.join(generate_c_code(elem) for elem in node[1])}}}"
    else:
        raise ValueError(f"Unknown node type: {node[0]}")


# Función principal para traducir
def translate_to_c(python_code):
    try:
        # Parsear el código Python
        ast = parser.parse(python_code, lexer=lexer)
        # Generar código C
        c_code = generate_c_code(ast)
        return c_code
    except SyntaxError as e:
        return f"Error de sintaxis: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"


# Función para leer el código de Python desde la consola
def read_python_code():
    print("Ingresa tu código de Python (presiona Enter dos veces para finalizar):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


# Ejemplo de uso
if __name__ == "__main__":
    # Leer el código de Python desde la consola
    python_code = read_python_code()

    # Traducir el código a C
    c_code = translate_to_c(python_code)

    # Mostrar el código generado en C
    print("\nCódigo generado en C:\n")
    print(c_code)