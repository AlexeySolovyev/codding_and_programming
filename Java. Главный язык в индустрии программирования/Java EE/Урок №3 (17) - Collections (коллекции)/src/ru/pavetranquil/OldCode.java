package ru.pavetranquil;

public class OldCode {
	private static String[][] phones = {
			{"IPhone", "+79123456789"},
			{"Samsung", "+79876543210"},
			{"Xiaomi", "+79012345678"}
	};

	public static void main(String[] args) {
		for (int i = 0; i<phones.length; i++){
			for (int ii = 0; ii<phones[i].length; ii++){
				System.out.print(phones[i][ii] + "  ");
			}
			System.out.println();
		}
	}

}
