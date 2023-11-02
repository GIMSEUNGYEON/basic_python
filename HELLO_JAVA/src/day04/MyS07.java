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

public class MyS07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS07 frame = new MyS07();
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
	public MyS07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 310, 445);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수 : ");
		lbl_first.setBounds(47, 39, 90, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝별수 : ");
		lbl_last.setBounds(47, 100, 90, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(131, 36, 96, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(131, 97, 96, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별 그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				myClick();
				myClick2();
			}
		});
		btn.setBounds(47, 134, 180, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(47, 180, 180, 201);
		contentPane.add(ta);
	}
	
	void myClick() {
		int first = Integer.parseInt(tf_first.getText());
		int last = Integer.parseInt(tf_last.getText());
		System.out.println("첫별수 : " + first + " 끝별수 : " + last);
		String answer = "";
		for(int i = 0; i < last - first + 1; i++) {
			for(int j = 0; j <= i+first; j++) {
				answer += "*";
			}
			answer+="\n";
		}
		ta.setText(answer);
	}
	
	public String getStar(int cnt) {
		String ret = "";
		for(int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret+="\n";
		return ret;
		
	}
	
	void myClick2() {
		String f = tf_first.getText();
		String l = tf_last.getText();
		
		int ff = Integer.parseInt(f);
		int ll = Integer.parseInt(l);
	
		String txt = "";
		
		for(int i = ff; i < ll + 1; i++) {			
			txt+=getStar(i);
		}
		
		ta.setText(txt);
	}
}
