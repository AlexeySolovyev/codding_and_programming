package ru.pavetranquil;

import java.awt.*;
import java.io.*;
import java.net.*;

public class Server implements Runnable {
	static private ServerSocket server;
	static private Socket connection;
	static private ObjectOutputStream output;
	static private ObjectInputStream input;
	//run()

	public static void main(String[] args) {
		

	}

	public void run() {
		try {
			server = new ServerSocket(Code.port, 10);
			while (true) {
				connection = server.accept();
				output = new ObjectOutputStream(connection.getOutputStream());
				input = new ObjectInputStream(connection.getInputStream());
				output.writeObject("Вы прислали: " + input.readObject());
			}
		} catch (UnknownHostException e) {
		} catch (IOException e) {
		} catch (HeadlessException e) {
		} catch (ClassNotFoundException e) {}
		
	}

}
