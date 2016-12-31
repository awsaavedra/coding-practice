package com.company;

public class Main {

    public static void main(String[] args) {
//	// write your code here
//        Printer binaPrinter = new Printer(100,0,false);
//
//        binaPrinter.printPages("Printing this line", 2);
//        binaPrinter.printPages("//////////", 2);
//        System.out.println(binaPrinter.getPagesPrinted());
//
//        Printer duplexPrinter = new Printer(100, 0, true);
//        duplexPrinter.printPages("Printing this line", 2);
//        duplexPrinter.printPages("////////////////", 2);
//        System.out.println(duplexPrinter.getPagesPrinted());

        //general solution
        TimPrinter printer = new TimPrinter(50, false);
        System.out.println("initial page count = " + printer.getPagesPrinted());
        int pagesPrinted = printer.printPages(4);
        System.out.println("Pages printed was..." + pagesPrinted +
                " new total print count for printer = " + printer.getPagesPrinted());
        pagesPrinted = printer.printPages(2);
        System.out.println("Pages printed was..." + pagesPrinted +
                " new total print count for printer = " + printer.getPagesPrinted());

    }
}
