import javax.swing.JFrame;

class Code {
	public static void main(String[] args) {
		Graphic g = new Graphic("Умножить два числа на 3");
		g.setVisible(true);
		g.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		g.setSize(275, 150);
		g.setResizable(false);
		g.setLocationRelativeTo(null);
	}
}