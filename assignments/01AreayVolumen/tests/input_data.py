# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["5"],
        # Outputs
        ["Dame radio: ", "Área: 314.1592653589793", "Volumen: 523.5987755982989"],
        # Error message
        "Revisa los acentos. Revisa la prioridad de operadores. Revisa los espacios entre palabras "
    ),
    (
        # Inputs
        ["20"],
        # Outputs
        ["Dame radio: ", "Área: 5026.548245743669", "Volumen: 33510.32163829113"],
        # Error message
        "Revisa los acentos. Revisa la prioridad de operadores. Revisa los espacios entre palabras "
    ),
    (
        # Inputs
        ["0"],
        # Outputs
        ["Dame radio: ", "Área: 0.0", "Volumen: 0.0"],
        # Error message
        "Revisa los acentos. Revisa la prioridad de operadores. Revisa los espacios entre palabras "
    )
]