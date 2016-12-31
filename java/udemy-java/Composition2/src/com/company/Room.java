package com.company;

/**
 * Created by awsaavedra on 12/19/16.
 */
public class Room {
    private roomHeater heater;
    private Radio stereo;
    private roomDimensions size;

    public Room(roomHeater heater, Radio stereo) {
        this.heater = heater;
        this.stereo = stereo;
    }

    public roomHeater getHeater() {
        return heater;
    }

    public Radio getStereo() {
        return stereo;
    }

    private roomDimensions roomSize(){
        return size;
    }
}
