package ru.pavetranquil;

import java.util.ArrayList;
import java.util.Random;

public class NewCode {
	private static ArrayList<Mobile> mobiles = new ArrayList<Mobile>();
	private static Random r = new Random();

	public static void main(String[] args) {
		for (int i = 0; i<100; i++) {
			mobiles.add(new Mobile(r.nextInt(9999999), "IPhone"));
		}
		for (Mobile m: mobiles) {
			System.out.println(m.getName() + "  " + m.getNumber());
		}
	}

}
