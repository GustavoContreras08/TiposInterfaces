<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $idUsuario = $_POST['idUsuario'];

        // Simulación de la lógica del servicio web
        if ($idUsuario == 123) {
            $nombre = "Juan Pérez";
            $email = "juan.perez@ejemplo.com";
        } else {
            $nombre = "Usuario no encontrado";
            $email = "";
        }

        // Construcción de la respuesta SOAP
        $respuestaSOAP = '
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:us="http://usuarios.ejemplo/">
       <soapenv:Header/>
       <soapenv:Body>
          <us:obtenerUsuarioResponse>
             <us:nombre>' . $nombre . '</us:nombre>
             <us:email>' . $email . '</us:email>
          </us:obtenerUsuarioResponse>
       </soapenv:Body>
    </soapenv:Envelope>
        ';

        // Redirección con la respuesta SOAP
        header('Location: index.html?respuesta=' . urlencode($respuestaSOAP));
        exit;
    }
    ?>