package ru.pavetranquil;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import java.util.Random;
import javax.swing.*;

public class Code extends JFrame implements Runnable{
	static private Socket connection;
	static private ObjectOutputStream output;
	static private ObjectInputStream input;
	static private Random r = new Random();
	static public int port = r.nextInt(9999);
	//run(), sendData(object), Code(name)
	
	public static void main(String[] args) {
		new Thread(new Code("Test")).start();
		new Thread(new Server()).start();
	}
	
	public Code(String name) {
		super(name);
		setLayout(new FlowLayout());
		setSize(300, 300);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
		setLocationRelativeTo(null);
		
		final JTextField t1 = new JTextField(10);
		final JButton b1 = new JButton("Отправить");
		b1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				if (arg0.getSource() == b1) {
					sendData(t1.getText());
				}
			}
		});
		add(t1);
		add(b1);
	}
	
	public void run() {
		try {
			while (true) {
				connection = new Socket(InetAddress.getByName("127.0.0.1"), port);
				output = new ObjectOutputStream(connection.getOutputStream());
				input = new ObjectInputStream(connection.getInputStream());
				JOptionPane.showMessageDialog(null, (String)input.readObject());
			}
		} catch (UnknownHostException e) {
		} catch (IOException e) {
		} catch (HeadlessException e) {
		} catch (ClassNotFoundException e) {}
	}
	
	private static void sendData(Object obj) {
		try {
			output.flush();
			output.writeObject(obj);
		} catch (IOException e) {}
		
	}

}
