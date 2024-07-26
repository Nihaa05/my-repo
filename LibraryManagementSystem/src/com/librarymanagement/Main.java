package com.librarymanagement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class Main {
    public static void main(String[] args) {
    	 try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/Library", "root", "root")) {
             if (conn != null) {
                 System.out.println("Connected to the database!");
             } else {
                 System.out.println("Failed to make connection!");
             }
         } catch (SQLException e) {
             e.printStackTrace();
         }
    	   	
    	//Data to be added in 'members' and 'books' tables
    	 //add and list books
        BookManager bookManager = new BookManager();
        bookManager.addBook("The Path", "Nicholas Sparks", "Novel");
        bookManager.listBooks();
         //add and list members
        MemberManager memberManager = new MemberManager();
        memberManager.addMember("Niha ", "niha@example.com");
        memberManager.listMembers();
    }
}


