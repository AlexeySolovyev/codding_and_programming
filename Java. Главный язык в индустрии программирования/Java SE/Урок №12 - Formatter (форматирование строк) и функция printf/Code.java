import java.util.Scanner;
import java.util.Formatter;

class Formating {

	static Scanner scn;
	static Formatter frmt;

	public static void main(String args[]) {
		try {
			scn = new Scanner(System.in);
			frmt = new Formatter("readFile.txt");
			System.out.println("��� ��� �����?");
			String name = scn.next();
			name = new String(name.getBytes("Cp1251"),"Cp866"); //����������� �� WIN-1251 (JAVA-���������) � WIN-866 (��������� CMD)
			System.out.println("������� ��� ���?");
			int years = scn.nextInt();
			System.out.println("��� �� �����?");
			String live = scn.next();
			live = new String(live.getBytes("Cp1251"),"Cp866"); //����������� �� WIN-1251 (JAVA-���������) � WIN-866 (��������� CMD)

			System.out.printf("%s - %d ���, �� ������ %s.", name, years, live);
			frmt.format("%s - %d ���, �� ������ %s.", name, years, live);
			frmt.close();
		} catch (Exception e) {};
	}
}