<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <h1>Tabla de Datos</h1>

    <table border="1">
        <tr>
            <th>Nombre</th>
            <th>Apellido</th>
        </tr>

        <?php
            $archivo = fopen("../datos.dat", "r");

            // Lee el resto de las líneas y muestra los datos en la tabla
            while (!feof($archivo)) {
                $linea = fgets($archivo);
                $datos = explode(" ", $linea); //Dividirá la cadena linea en una lista de palabras cada vez que encuentre un espacio en blanco.

                echo "<tr>";
                foreach ($datos as $dato) {
                    echo "<td>$dato</td>";
                }
                echo "</tr>";
            }

            fclose($archivo);
        ?>

    </table>
    <a href="../index.php"><button type="button" class="btn btn-dark">Volver al inicio</button></a>
</body>
</html>
