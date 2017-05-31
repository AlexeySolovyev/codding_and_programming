import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Graphic extends JFrame {
	JButton b1, b2, b3, b4, b5, b6, b7, b8, b9 , b10, b11, b12, b13, b14, b15, b16, b17, b18, b19;
	JTextField text;
	double n1, n2;
	boolean addition, subtraction, multiplication, division;
	Listener listen = new Listener();

	public Graphic(String s) {
		super(s);
		setLayout(new FlowLayout());
		b1 = new JButton("1");
		b2 = new JButton("2");
		b3 = new JButton("3");
		b4 = new JButton("4");
		b5 = new JButton("5");
		b6 = new JButton("6");
		b7 = new JButton("7");
		b8 = new JButton("8");
		b9 = new JButton("9");
		b10 = new JButton("0");
		b11 = new JButton("<--");
		b12 = new JButton("CE");
		b13 = new JButton("±");
		b14 = new JButton("/");
		b15 = new JButton("*");
		b16 = new JButton("-");
		b17 = new JButton("+");
		b18 = new JButton("=");
		b19 = new JButton(".");

		text = new JTextField(16);

		add(text);
		add(b11);
		add(b12);
		add(b13);
		add(b7);
		add(b8);
		add(b9);
		add(b14);
		add(b4);
		add(b5);
		add(b6);
		add(b15);
		add(b1);
		add(b2);
		add(b3);
		add(b16);
		add(b10);
		add(b19);
		add(b17);
		add(b18);

		b1.addActionListener(listen);
		b2.addActionListener(listen);
		b3.addActionListener(listen);
		b4.addActionListener(listen);
		b5.addActionListener(listen);
		b6.addActionListener(listen);
		b7.addActionListener(listen);
		b8.addActionListener(listen);
		b9.addActionListener(listen);
		b10.addActionListener(listen);
		b11.addActionListener(listen);
		b12.addActionListener(listen);
		b13.addActionListener(listen);
		b14.addActionListener(listen);
		b15.addActionListener(listen);
		b16.addActionListener(listen);
		b17.addActionListener(listen);
		b18.addActionListener(listen);
		b19.addActionListener(listen);
	}

	public class Listener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			if (e.getSource() == b1) {
				text.setText(text.getText() + "1");
			}
			if (e.getSource() == b2) {
				text.setText(text.getText() + "2");
			}
			if (e.getSource() == b3) {
				text.setText(text.getText() + "3");
			}
			if (e.getSource() == b4) {
				text.setText(text.getText() + "4");
			}
			if (e.getSource() == b5) {
				text.setText(text.getText() + "5");
			}
			if (e.getSource() == b6) {
				text.setText(text.getText() + "6");
			}
			if (e.getSource() == b7) {
				text.setText(text.getText() + "7");
			}
			if (e.getSource() == b8) {
				text.setText(text.getText() + "8");
			}
			if (e.getSource() == b9) {
				text.setText(text.getText() + "9");
			}
			if (e.getSource() == b10) {
				text.setText(text.getText() + "0");
			}
			if (e.getSource() == b11) {
				try {
					text.setText(text.getText().substring(0, text.getText().length()-1));
				} catch (Exception ex) {
					
				}
			}
			if (e.getSource() == b12) {
				text.setText(null);
			}
			if (e.getSource() == b13) {
				if (!(text.getText().startsWith("-"))) {
					text.setText("-" + text.getText());
				}
				else {
					text.setText(text.getText().substring(1, text.getText().length()));
				}
			}
			if (e.getSource() == b14) {
				n1 = Double.valueOf(text.getText());
				text.setText(text.getText() + "/");
				division = true;
			}
			if (e.getSource() == b15) {
				n1 = Double.valueOf(text.getText());
				text.setText(text.getText() + "*");
				multiplication = true;
			}
			if (e.getSource() == b16) {
				n1 = Double.valueOf(text.getText());
				text.setText(text.getText() + "-");
				subtraction = true;
			}
			if (e.getSource() == b17) {
				n1 = Double.valueOf(text.getText());
				text.setText(text.getText() + "+");
				addition = true;
			}
			if (e.getSource() == b18) {
				if (division) {
					n2 = Double.valueOf(text.getText().substring(text.getText().indexOf("/") + 1, text.getText().length()));
					text.setText(Double.toString(n1 / n2));
					division = false;
				}
				else if (multiplication) {
					n2 = Double.valueOf(text.getText().substring(text.getText().indexOf("*") + 1, text.getText().length()));
					text.setText(Double.toString(n1 * n2));
					multiplication = false;
				}
				else if (subtraction) {
					n2 = Double.valueOf(text.getText().substring(text.getText().indexOf("-") + 1, text.getText().length()));
					text.setText(Double.toString(n1 - n2));
					subtraction = false;
				}
				else if (addition) {
					n2 = Double.valueOf(text.getText().substring(text.getText().indexOf("+") + 1, text.getText().length()));
					text.setText(Double.toString(n1 + n2));
					addition = false;
				}
				else {

				}
				
			}
			if (e.getSource() == b19) {
				text.setText(text.getText() + ".");
			}
		}
	}
}