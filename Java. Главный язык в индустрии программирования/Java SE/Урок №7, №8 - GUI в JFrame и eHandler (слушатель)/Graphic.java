import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Graphic extends JFrame {
	JButton b1, b2;
	JLabel l1, l2, l3, l4;
	JTextField t1, t2;
	int i, k;
	Listener listen = new Listener();
	//Listener - class, Graphic();

	public Graphic(String s) {
		super(s);
		setLayout(new FlowLayout());
		b1 = new JButton("��������");
		b2 = new JButton("���������");

		l1 = new JLabel("������� ������ �����: ");
		l2 = new JLabel("������� ������ �����: ");

		l3 = new JLabel();
		l4 = new JLabel();

		t1 = new JTextField(10);
		t2 = new JTextField(10);
		

		add(l1);
		add(t1);
		add(l2);
		add(t2);
		add(b2);
		add(b1);
		add(l3);
		add(l4);
		b2.addActionListener(listen);
		b1.addActionListener(listen);
	}

	public class Listener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			try {
				if (e.getSource() == b2) {
					i = Integer.parseInt(t1.getText());
					k = Integer.parseInt(t2.getText());
					i *= 3;
					k *= 3;
					l3.setText("1-� �����: " + i);
					l4.setText("2-� �����: " + k);
				}
			} catch (Exception ex) {
				JOptionPane.showMessageDialog(null, "� ���� ����� �������� ������ �����!");
				t1.setText(null);
				t2.setText(null);
			}
			if (e.getSource() == b1) {
				t1.setText(null);
				t2.setText(null);
				l3.setText(null);
				l4.setText(null);
			}
		}
	}
}