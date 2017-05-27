import javax.swing.JOptionPane;

class Graphic {
	int i, k;
	//Input(), Show()

	public void Input() {
		i = Integer.parseInt(JOptionPane.showInputDialog("Введите первое число: "));
		k = Integer.parseInt(JOptionPane.showInputDialog("Введите второе число: "));
	}

	public void Show(int a, int b) {
		JOptionPane.showMessageDialog(null, "Теперь ваше первое число = " + a + ".");
		JOptionPane.showMessageDialog(null, "Теперь ваше второе число = " + b + ".");
	}
}