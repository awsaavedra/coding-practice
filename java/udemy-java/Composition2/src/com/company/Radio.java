package com.company;

/**
 * Created by awsaavedra on 12/19/16.
 */
public class Radio {
    private String loudness;

    public Radio( String loudness) {
        this.loudness = loudness;
    }

    public void playMusic(){
        System.out.println("Music is playing at " + loudness);
    }
}
