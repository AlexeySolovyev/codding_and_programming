class Sleeping {
	public static void main(String[] args) {
		String x = "Hello, World!";
		for (int i = 0; i<x.length(); i++) {
			System.out.print(x.charAt(i));
			try {                   //��� ����� ���� �������� ������ ������, ������� �����
				Thread.sleep(150);  //���� ����� ��� ���������� ������� ���� ���
			}catch (Exception e) {} //����� ������� ��������� ������� (�������� �������).
		}                           
	}
}