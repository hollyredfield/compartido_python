<?php
require_once ('../modelo/gestion_datos.php');

include ("encabezado.php");

$datos = mostrar();
?>
<div style= "display: flex; align-items: center; justify-content: center; ">
    <table style="border: 1px solid #ddd; border-collapse: collapse;">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Apellido</th>
            </tr>
        </thead>
        <tbody style = "text-align: center;">
        <?php
            foreach ($datos as $fila) {
                echo "<tr>";                
                $datosFila = explode(';', $fila); // Explode para dividir la línea en nombre y apellido
                foreach ($datosFila as $valor) {
                    echo "<td>$valor</td>";
                }
                echo "</tr>";
            }
        ?>
        </tbody>
    </table>
</div>
<div style= "display: flex; align-items: center; justify-content: center;">
    <section id= 'vercontactos'>
            <a href="../index.php"><button>Volver</button></a>
    </section>
</div>
<?php
include ("pie.php");
?>