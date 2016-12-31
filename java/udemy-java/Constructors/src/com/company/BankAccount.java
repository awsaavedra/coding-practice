package com.company;

/**
 * Created by awsaavedra on 12/12/16.
 */
public class BankAccount {
    private int accountNumber;
    private double accountBalance;
    private String customerName;
    private String customerEmailAddress;
    private int customerPhoneNumber;

    //constructor has to have same name as class (BankAccount)
    public BankAccount(){
        //a little weird usage of 'this' keyword...calling constructor below this one
        this(124,0.0, "default name", "abc@123.com", 12445);
        System.out.println("Empty constructor is called");
    }

    public BankAccount(String customerName, String customerEmailAddress, int customerPhoneNumber) {
        this(9999, 100.55, customerName, customerEmailAddress, customerPhoneNumber);
        this.customerName = customerName;
        this.customerEmailAddress = customerEmailAddress;
        this.customerPhoneNumber = customerPhoneNumber;
    }

    //general rule of thumb: don't call other methods besides constructors in constructors
    public BankAccount(int accountNumber, double accountBalance, String customerName, String customerEmailAddress,
                       int customerPhoneNumber){
        System.out.println("Account constructor with parameters called");
        this.accountNumber = accountNumber; //DON'T do: setAccountNumber(accountNumber);
        this.accountBalance = accountBalance;
        this.customerName = customerName;
        this.customerEmailAddress = customerEmailAddress;
        this.customerPhoneNumber = customerPhoneNumber;
    }





    //setters
    public void setAccountNumber( int accountNumber){
        this.accountNumber = accountNumber;
    }

    public void setAccountBalance(double accountBalance){
        this.accountBalance = accountBalance;
    }

    public void setCustomerName(String customerName){
        customerName.toLowerCase();
        if(customerName.matches("[a-z]+")){
            this.customerName = customerName;
        }else{
            System.out.println("Invalid customer name");
        }
    }
    public void setPhoneNumber(int customerPhoneNumber){
        if( customerPhoneNumber >= 1 && customerPhoneNumber <= 999_9999){
            this.customerPhoneNumber = customerPhoneNumber;
        }else{
            System.out.println("Invalid phone number");
        }
    }

    //getters
    public int getAccountNumber(){
        return this.accountNumber;
    }

    public double getAccountBalance(){
        return this.accountBalance;
    }

    public String getCustomerName(){
        return this.customerName;
    }
    public int getPhoneNumber(){
        return this.customerPhoneNumber;
    }


    //depositFunds
    public void depositFunds(double deposit){
        if(deposit >= 0.0){
            this.accountBalance += deposit;
            System.out.println("Account deposit of " + deposit + " Account balance: " + this.accountBalance);
        }else{
            System.out.println("Invalid deposit, add over a cent yo! Account balance:" + this.accountBalance);
        }
    }
    public void withdrawFunds(double withdrawal){

        if( this.accountBalance - withdrawal >= 0.0){
            this.accountBalance -= withdrawal;
            System.out.println("Account balance: " + this.accountBalance + " Withdrawal amount: " + withdrawal);
        }else {
            System.out.println("Invalid withdrawal, remove over a cent yo!");

        }

    }
}
