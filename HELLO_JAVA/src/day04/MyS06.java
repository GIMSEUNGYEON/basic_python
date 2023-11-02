package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionEvent;

public class MyS06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS06 frame = new MyS06();
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
	public MyS06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 309, 244);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl_mine = new JLabel("나 : ");
		lbl_mine.setBounds(36, 30, 50, 15);
		contentPane.add(lbl_mine);

		JLabel lbl_com = new JLabel("com : ");
		lbl_com.setBounds(36, 81, 50, 15);
		contentPane.add(lbl_com);

		JLabel lbl_result = new JLabel("결과 : ");
		lbl_result.setBounds(36, 132, 50, 15);
		contentPane.add(lbl_result);

		tf_mine = new JTextField();
		tf_mine.setBounds(128, 27, 96, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);

		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(128, 81, 96, 21);
		contentPane.add(tf_com);

		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(128, 129, 96, 21);
		contentPane.add(tf_result);

		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(92, 174, 91, 23);
		contentPane.add(btn);
	}

	void myClick() {

		double rnd = Math.random();
		if (rnd > 0.5) {
			tf_com.setText("홀");
		} else {
			tf_com.setText("짝");
		}
		
		if (tf_mine.getText().equals(tf_com.getText())) {
			tf_result.setText("win");
		} else {
			tf_result.setText("lose");

		}
	}
}
