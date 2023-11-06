package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JLabel;

public class MyOmok01_1 extends JFrame {

	private JPanel contentPane;
	boolean flag_wb = true;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyOmok01_1 frame = new MyOmok01_1();
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
	public MyOmok01_1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 450);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("0,0");
		lblNewLabel.setIcon(new ImageIcon(MyOmok01_1.class.getResource("/day05/0.png")));
		lblNewLabel.setBounds(413, 28, 40, 40);
		contentPane.add(lblNewLabel);
			
		
		for(int i=0;i<10;i++){
			for(int j=0;j<10;j++){
				JLabel btn = new JLabel("");
				btn.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						myclick(e);
					}
				});
				btn.setIcon(new ImageIcon(MyOmok01.class.getResource("/day05/0.png")));
				btn.setBounds(i*40, j*40, 40, 40);
				contentPane.add(btn);
			}
		}




	}
	void myclick(MouseEvent e) {
		JLabel temp = (JLabel) e.getSource();
		if(flag_wb) {
			temp.setIcon(new ImageIcon(MyOmok01.class.getResource("/day05/1.png")));
		}else {
			temp.setIcon(new ImageIcon(MyOmok01.class.getResource("/day05/2.png")));
		}
		
		flag_wb =!flag_wb;
	}
}











