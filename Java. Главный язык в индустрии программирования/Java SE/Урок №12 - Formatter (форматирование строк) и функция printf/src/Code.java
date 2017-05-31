import java.util.Scanner;
import java.util.Formatter;

class Formating {

	static Scanner scn;
	static Formatter frmt;

	public static void main(String args[]) {
		try {
			scn = new Scanner(System.in);
			frmt = new Formatter("readFile.txt");
			System.out.println("Как вас зовут?");
			String name = scn.next();
			name = new String(name.getBytes("Cp1251"),"Cp866"); //КОНВЕРТАЦИЯ ИЗ WIN-1251 (JAVA-КОДИРОВКИ) В WIN-866 (КОДИРОВКИ CMD)
			System.out.println("Сколько вам лет?");
			int years = scn.nextInt();
			System.out.println("Где вы живёте?");
			String live = scn.next();
			live = new String(live.getBytes("Cp1251"),"Cp866"); //КОНВЕРТАЦИЯ ИЗ WIN-1251 (JAVA-КОДИРОВКИ) В WIN-866 (КОДИРОВКИ CMD)

			System.out.printf("%s - %d лет, из города %s.", name, years, live);
			frmt.format("%s - %d лет, из города %s.", name, years, live);
			frmt.close();
		} catch (Exception e) {};
	}
}