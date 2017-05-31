import java.util.Scanner;
import java.io.*;
import javax.swing.JOptionPane;

class ReadFromFiles {
	static String[][] m = new String[5][3];
	static Scanner scn;
	//openFile(), readFile(), out()
	
	public static void main(String[] args) {
		openFile();
		readFile();
		out();
	}

	private static void openFile() {
		try {
			scn = new Scanner(new File("readFile.txt"));
		} catch (Exception e) {
			JOptionPane.showMessageDialog(null, "Файл не найден");
		}
		
	}

	private static void readFile() {
		while (scn.hasNext()) {
			for (int i = 0; i < m.length; i++) {
				for (int ii = 0; ii < m[i].length; ii++) {
					m[i][ii] = scn.next();
				}
			}
		}
	}

	private static void out() {
		for (int i = 0; i < m.length; i++) {
			for (int ii = 0; ii < m[i].length; ii++) {
				System.out.print(m[i][ii] + "  ");
			}
		System.out.println();
		}
	}
}