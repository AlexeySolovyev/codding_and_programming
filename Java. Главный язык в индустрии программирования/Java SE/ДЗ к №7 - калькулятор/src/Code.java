import javax.swing.JFrame;

class Code {
	public static void main(String[] args) {
		Graphic g = new Graphic("Калькулятор");
		g.setVisible(true);
		g.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		g.setSize(200, 225);
		g.setResizable(false);
		g.setLocationRelativeTo(null);
	}
}