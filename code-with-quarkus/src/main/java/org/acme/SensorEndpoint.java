package org.acme;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import Sensors.SensorManager;
/*
    Test class to extract values(String here) from URL
*/
@Path("/Sensor")
public class SensorEndpoint {
    //Goto
    //http://192.168.0.12:8080/Sensor/Haj
    //or
    //http://0.0.0.0:8080/Sensor/Haj

    @GET
    @Path("{ID}")
    @Consumes(MediaType.TEXT_PLAIN)
    @Produces(MediaType.TEXT_PLAIN)
    public String getSensor(@PathParam("ID") String id){
        SensorManager s = new SensorManager(); // Should use singleton instance thingy...
        return s.getID(id);
    }

}