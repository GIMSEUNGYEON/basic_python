package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS05 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl1;
	private JLabel lbl2;
	private JLabel lbl3;
	private JLabel lbl4;
	private JLabel lbl5;
	private JLabel lbl6;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS05 frame = new MyS05();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyS05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		lbl1 = new JLabel("__");
		lbl1.setBounds(34, 31, 50, 15);
		contentPane.add(lbl1);

		lbl2 = new JLabel("__");
		lbl2.setBounds(75, 31, 50, 15);
		contentPane.add(lbl2);

		lbl3 = new JLabel("__");
		lbl3.setBounds(117, 31, 50, 15);
		contentPane.add(lbl3);

		lbl4 = new JLabel("__");
		lbl4.setBounds(221, 31, 50, 15);
		contentPane.add(lbl4);

		lbl5 = new JLabel("__");
		lbl5.setBounds(283, 31, 50, 15);
		contentPane.add(lbl5);

		lbl6 = new JLabel("__");
		lbl6.setBounds(345, 31, 50, 15);
		contentPane.add(lbl6);

		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto();
			}
		});
		btn.setBounds(34, 84, 335, 23);
		contentPane.add(btn);
	}

	void lotto() {
		int[] lotto = new int[6];

		for (int i = 0; i < lotto.length; i++) {
			int num = (int) (Math.random() * 45) + 1;
			lotto[i] = num;
			for (int j = 0; j < i; j++) {
				if (lotto[i] == lotto[j]) {
					i--;
					break;
				}
			}
		}

		lbl1.setText(lotto[0] + "");
		lbl2.setText(lotto[1] + "");
		lbl3.setText(lotto[2] + "");
		lbl4.setText(lotto[3] + "");
		lbl5.setText(lotto[4] + "");
		lbl6.setText(lotto[5] + "");
	}
}
