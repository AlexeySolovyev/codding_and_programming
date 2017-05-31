package ru.pavetranquil;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Code {

	private static ArrayList<Profile> profiles = new ArrayList<Profile>();
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		profiles = (ArrayList<Profile>) deSerData("profiles");
		Profile profile = new Profile();
		profile.setName(JOptionPane.showInputDialog(null, "Введите имя человека: "));
		profile.setSurname(JOptionPane.showInputDialog(null, "Введите фамилию человека: "));
		profiles.add(profile);
		for (Profile p : profiles) {
			System.out.println(p.getName() + " " + p.getSurname());
		}
		serData("profiles", profiles);
	}

	private static void serData(String file_name, Object obj) {
		try {
			FileOutputStream fileOut = new FileOutputStream(file_name + ".ser");
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			out.writeObject(obj);
			out.close();
			fileOut.close();
		} catch (FileNotFoundException e) {
			JOptionPane.showMessageDialog(null, "Файл не найден!");
			System.exit(1);
		} catch (IOException e) {
			JOptionPane.showMessageDialog(null, "Ошибка ввода/вывода!");
			System.exit(1);
		}
	}

	private static Object deSerData(String file_name) {
		Object retObject = null;
		try {
			FileInputStream fileIn = new FileInputStream(file_name + ".ser");
			ObjectInputStream in = new ObjectInputStream(fileIn);
			retObject = in.readObject();
			in.close();
			fileIn.close();
		} catch (FileNotFoundException e) {
			JOptionPane.showMessageDialog(null, "Файл не найден!");
			System.exit(1);
		} catch (IOException e) {
			JOptionPane.showMessageDialog(null, "Ошибка ввода/вывода!");
			System.exit(2);
		} catch (ClassNotFoundException e) {
			JOptionPane.showMessageDialog(null, "Класс не найден!");
			System.exit(3);
		return retObject;
		}
		return retObject;
	}

}