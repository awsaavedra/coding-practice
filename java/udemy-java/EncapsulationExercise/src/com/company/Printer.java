package com.company;

/**
 * Created by awsaavedra on 12/28/16.
 */
public class Printer {
    private int tonerLevel = 100; //default
    private int pagesPrinted = 0; //default
    private boolean duplexPrinter = false;

    public Printer(int tonerLevel, int pagesPrinted, boolean duplexPrinter) {
        if(tonerLevel >= 0 && tonerLevel <= 100){
            this.tonerLevel = tonerLevel;
        }
        if(pagesPrinted >= 0){
            this.pagesPrinted = pagesPrinted;
        }
        this.duplexPrinter = duplexPrinter;
    }

    public void printPages(String words, int numberOfPages){
        if( words.length() >= 100 ){
            tonerLevel -= 1;
        }
        if(duplexPrinter == false){
            this.pagesPrinted += numberOfPages;
        }else{
            this.pagesPrinted += numberOfPages / 2;
            System.out.println("You are printing from a duplex printer");
        }

        for(int i = 0; i < numberOfPages; i++){
            System.out.println(words);
        }
    }

    public void fillToner(int refillToner){
        if( tonerLevel + refillToner <= 100){
            tonerLevel += refillToner;
        }else{
            tonerLevel = 100; //only fill up to 100%
        }
    }

    public int getTonerLevel() {
        return tonerLevel;
    }

    public int getPagesPrinted() {
        return pagesPrinted;
    }
}
