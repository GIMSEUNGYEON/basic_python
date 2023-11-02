package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	int com2 = 0;
	String answer = "";

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS08 frame = new MyS08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public MyS08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 272, 389);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞출수");
		lbl.setBounds(39, 39, 50, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(124, 36, 96, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		int com = (int)(Math.random()*99) +1;
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				answer = myClick(answer, com);
//				System.out.println(com);
//				System.out.println(answer);
//				ta.setText(answer);
				myClick();
			}
		});
		btn.setBounds(39, 79, 181, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(39, 112, 181, 218);
		contentPane.add(ta);
		
		setCom();
		
	}	
	
	void setCom() {
		com2 = (int)(Math.random()*99) + 1;
	}
	void myClick() {
		String mine = tf.getText();
		int imine = Integer.parseInt(mine);
		
		String txt = "";
		
		if(com2 > imine) {
			txt += imine + "UP\n";
		}else if( com2 < imine) {
			txt += imine + "DOWN\n";
		}else {
			txt += imine + "ANSWER\n";
			JOptionPane.showMessageDialog(null, "정답입니다!");
		}
		String str_old = ta.getText() + "\n";
		ta.setText(str_old + txt);
	}
	String myClick(String msg, int com) {
		int myNum = Integer.parseInt(tf.getText());
		if(myNum == com) {
			JOptionPane.showMessageDialog(null, "정답입니다!");
		}else if(myNum > com) {
			msg += myNum + "\tdown\n";
		}else if(myNum < com) {
			msg += myNum + "\tup\n";
		}
		return msg;
	}
}
