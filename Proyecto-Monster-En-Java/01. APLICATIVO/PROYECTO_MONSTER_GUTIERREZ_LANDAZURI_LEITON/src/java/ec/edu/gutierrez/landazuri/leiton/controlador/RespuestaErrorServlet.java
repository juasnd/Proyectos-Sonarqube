package ec.edu.gutierrez.landazuri.leiton.controlador;

import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletResponse;

final class RespuestaErrorServlet {
    private RespuestaErrorServlet() {
    }

    static void manejar(HttpServlet servlet, HttpServletResponse response, Exception error) {
        servlet.log("No se pudo completar la solicitud.", error);
        if (!response.isCommitted()) {
            response.resetBuffer();
            response.setHeader("Location", null);
            response.setHeader("Content-Length", null);
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
    }
}
