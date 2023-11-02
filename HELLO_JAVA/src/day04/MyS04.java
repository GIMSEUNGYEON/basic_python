package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS04 frame = new MyS04();
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
	public MyS04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 254, 465);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력 단수");
		lbl.setBounds(37, 38, 83, 68);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(114, 62, 96, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				multiplication();
			}
		});
		btn.setBounds(37, 93, 171, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(37, 126, 173, 261);
		contentPane.add(ta);
	}
	
	void multiplication() {
		int dan = Integer.parseInt(tf.getText());
		
		String gugudan = "";
		
		for(int i = 1; i < 10; i++) {
			gugudan += dan + " * " + i + " = " + (dan*i) + "\n"; 
		}
		System.out.println(gugudan);
		ta.setText(gugudan);
	
	}
}
