import javax.swing.JOptionPane;

class Graphic {
	int i, k;
	//Input(), Show()

	public void Input() {
		i = Integer.parseInt(JOptionPane.showInputDialog("������� ������ �����: "));
		k = Integer.parseInt(JOptionPane.showInputDialog("������� ������ �����: "));
	}

	public void Show(int a, int b) {
		JOptionPane.showMessageDialog(null, "������ ���� ������ ����� = " + a + ".");
		JOptionPane.showMessageDialog(null, "������ ���� ������ ����� = " + b + ".");
	}
}