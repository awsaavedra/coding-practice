package com.company;

/**
 * Created by awsaavedra on 12/18/16.
 */
public class VipCustomer {
    private String customerName;
    private double creditLimit;
    private String emailAddress;

    public VipCustomer(String customerName, double creditLimit, String emailAddress){
        this.customerName = customerName;
        this.creditLimit = creditLimit;
        this.emailAddress = emailAddress;
    }

    public VipCustomer(){
        this("Default name", 100.00, "default@1.com");
    }

    public VipCustomer(String customerName, double creditLimit){
        this(customerName, creditLimit, "default@email.com");
    }


    public String getCustomerName() {
        return customerName;
    }

    public double getCreditLimit() {
        return creditLimit;
    }

    public String getEmailAddress() {
        return emailAddress;
    }
}
