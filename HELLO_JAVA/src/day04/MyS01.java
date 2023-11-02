package day04;

import java.awt.EventQueue;
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS01 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS01 frame = new MyS01();
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
	public MyS01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 627, 455);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl = new JLabel("Good Morning");
		lbl.setBounds(51, 51, 87, 60);
		contentPane.add(lbl);

		JButton btn = new JButton("Click");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				System.out.println("MyClick");
				if(lbl.getText().equals("Good Morning")) {
					lbl.setText("Good Evening");
				}else if(lbl.getText().equals("Good Evening")) {
					lbl.setText("Good Night");
				}else {
					lbl.setText("Good Morning");
					
				}
			}
		});
		btn.setBounds(225, 70, 91, 23);
		contentPane.add(btn);

//		btn.addActionListener(new ActionListener() {
//			int cnt = 0;
//
//			@Override
//			public void actionPerformed(ActionEvent e) {
//				cnt += 1;
//				if (cnt % 3 == 0) {
//					lbl.setText("Good Morning!");
//				} else if (cnt % 3 == 1) {
//					lbl.setText("Good Evening!");
//				} else {
//					lbl.setText("Good Night!");
//				}
//			}
//		});
	}
}
