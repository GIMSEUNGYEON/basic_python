package day05;

import java.awt.EventQueue;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyOmok02 extends JFrame {

	private JPanel contentPane;
	JLabel[][] btn = new JLabel[10][10];
	JLabel btn1;
//	int cnt = 0;
	boolean flag_bw = true;
	int[][] arr2D = {
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
		
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0},
			{0,0,0,0,0,	0,0,0,0,0}
	};
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyOmok02 frame = new MyOmok02();
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
	public MyOmok02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 430, 450);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				btn[i][j] = new JLabel("");
				btn[i][j].setBounds(j*40, i*40, 40, 40);
				contentPane.add(btn[i][j]);
				btn[i][j].setIcon(new ImageIcon(MyOmok01_1.class.getResource("/day05/0.png")));
				
				btn[i][j].addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						myClick((JLabel)e.getComponent());
					}
				});
			}
		}
		btn1 = new JLabel("");
		btn1.setIcon(new ImageIcon(MyOmok01_1.class.getResource("/day05/0.png")));
		
		myRender();
	}
	
	void myClick(JLabel btn) {
		
//		System.out.println(btn.getIcon());
//		System.out.println(btn1.getIcon());
//		System.out.println(btn.getIcon());
//		if(!btn.getIcon().equals(btn1.getIcon())) {
//			return;
//		}
//		if(!btn.isEnabled()) {
//			return;
//		}
		
		if (!((ImageIcon)btn.getIcon()).getDescription().equals(((ImageIcon) btn1.getIcon()).getDescription())) {
		    return;
		}
		
//		cnt++;
		
		if(flag_bw) {
			btn.setIcon(new ImageIcon("C:\\workspace_python\\HELLO_JAVA\\src\\day05\\2.png"));
		} else {
			btn.setIcon(new ImageIcon("C:\\workspace_python\\HELLO_JAVA\\src\\day05\\1.png"));
		}
		flag_bw = !flag_bw;	
//		btn.setEnabled(false);
	}
	
	//
	void myRender() {
		for(int i = 0; i < arr2D.length; i++) {
			for(int j = 0; j < arr2D[0].length; j++) {
				if(arr2D[i][j] == 1) {
					btn[i][j].setIcon(new ImageIcon("C:\\workspace_python\\HELLO_JAVA\\src\\day05\\1.png"));
				}else if(arr2D[i][j] == 2) {
					btn[i][j].setIcon(new ImageIcon("C:\\workspace_python\\HELLO_JAVA\\src\\day05\\2.png"));
				}
			}
		}
	}
}
