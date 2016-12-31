package com.company;

public class Main {

    public static void main(String[] args) {
//	// write your code here
//        BankAccount stevesAccount = new BankAccount(124,0.0, "Steve brown", "abc@123.com", 12445);
//        System.out.println(stevesAccount.getCustomerName());
//        System.out.println(stevesAccount.getPhoneNumber());
//        BankAccount emptyPersonAccount = new BankAccount();
//        //constructors

//        BankAccount alexAccount = new BankAccount("Alex", "blah@1.com", "1245");
//        System.out.println(alexAccount.getPhoneNumber() + " name "+ alexAccount.getCustomerName());

        VipCustomer person1 = new VipCustomer();
        person1.getCustomerName();

        VipCustomer person2 = new VipCustomer("Alex", 2400.00);
        System.out.println(person2.getCustomerName());

        VipCustomer person3 = new VipCustomer("Tim", 100.00, "tim@tim.com");
        System.out.println(person3.getCustomerName());
    }
}
