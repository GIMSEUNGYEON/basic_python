package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JButton btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btn_call;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS09 frame = new MyS09();
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
	public MyS09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 407, 347);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField("");
		tf.setBounds(46, 22, 317, 53);
		contentPane.add(tf);
		tf.setColumns(10);
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		//전화번호가 입력될 때 오른쪽 정렬
		
		btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton imsi = (JButton) e.getSource(); //오브젝트 타입을 JButton타입으로 캐스팅
//				System.out.println(imsi.getText());    
//				System.out.println(e.getComponent()); //오브젝트 반환
				myClick(e);
			}
		});
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				inputTest(btn1);
			}
		});
		btn1.setBounds(46, 99, 91, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn2);			
			}
		});
		btn2.setBounds(158, 99, 91, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn3);			
			}
		});
		
		btn3.setBounds(272, 99, 91, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn4);			
			}
		});
		btn4.setBounds(46, 149, 91, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn5);			
			}
		});
		btn5.setBounds(158, 149, 91, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn6);			
			}
		});
		btn6.setBounds(272, 149, 91, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn7);			

			}
		});
		btn7.setBounds(46, 198, 91, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn8);			

			}
		});
		btn8.setBounds(158, 198, 91, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn9);			

			}
		});
		btn9.setBounds(272, 198, 91, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				inputTest(btn0);			
			}
		});
		btn0.setBounds(46, 242, 91, 23);
		contentPane.add(btn0);
		
		btn_call = new JButton("☎");
		btn_call.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				JOptionPane.showMessageDialog(null, tf.getText() + "에게 전화를 겁니다.");
				myCall();
			}
		});
		
		btn_call.setBounds(158, 242, 205, 23);
		contentPane.add(btn_call);
		
		//버튼을 누르면 텍스트필드에 번호가 들어가도록(누적)
		//전화버튼을 누르면 확인창을 띄우도록
	}
	
	void inputTest(JButton btn) {
		int num = Integer.parseInt(btn.getText());
		String pNum = tf.getText();
		pNum += num;
		tf.setText(pNum);
	}
	
	void myClick(MouseEvent e) {
		JButton temp = (JButton) e.getComponent();
		
		String str_new = temp.getText();
		System.out.println(str_new);
		String str_old = tf.getText();
		
		tf.setText(str_old + str_new);
	}
	
	void myCall() {
		JOptionPane.showMessageDialog(null, "calling...\n" + tf.getText());
		
	}
}
