package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.ImageIcon;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class MyOmok02_1 extends JFrame {

	private JPanel contentPane;
	boolean flag_wb = true;
	boolean flag_ing = true;
	int[][] arr2D = { 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 }, 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 }, 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 }, 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 },

			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 }, 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 }, 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 }, 
			{ 0, 0, 0, 0, 0, 	0, 0, 0, 0, 0 } 
		};

	JLabel[][] lbl2D = new JLabel[10][10];

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyOmok02_1 frame = new MyOmok02_1();
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
	public MyOmok02_1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 450);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl_reset = new JLabel("reset");
		lbl_reset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myReset();
			}
		});
		lbl_reset.setBounds(410, 25, 40, 40);
		contentPane.add(lbl_reset);

		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				JLabel lbl = new JLabel("");
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						myclick(e);
					}
				});
				lbl.setIcon(new ImageIcon(MyOmok02.class.getResource("/day05/0.png")));
				lbl.setBounds(j * 40, i * 40, 40, 40);
				lbl.setText(i + "," + j);
				contentPane.add(lbl);
				lbl2D[i][j] = lbl;
			}
		}

		myrender();
	}

	void myrender() {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (arr2D[i][j] == 0) {
					lbl2D[i][j].setIcon(new ImageIcon(MyOmok02.class.getResource("/day05/0.png")));
				}
				if (arr2D[i][j] == 1) {
					lbl2D[i][j].setIcon(new ImageIcon(MyOmok02.class.getResource("/day05/2.png")));
				}
				if (arr2D[i][j] == 2) {
					lbl2D[i][j].setIcon(new ImageIcon(MyOmok02.class.getResource("/day05/1.png")));
				}
			}
		}
	}
	
	int getUP(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				i--;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getDW(int i, int j, int stone) {
		int cnt = 0;
		try {			
			while(true) {
				i++;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getLE(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				j--;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getRI(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				j++;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getUR(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				i--;
				j++;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getUL(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				i--;
				j--;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getDR(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				i++;
				j++;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	int getDL(int i, int j, int stone) {
		int cnt = 0;
		try {
			while(true) {
				i++;
				j--;
				if(arr2D[i][j] == stone) {
					cnt++;
				}else {
					return cnt;				
				}
			}
		} catch (Exception e) {
			return cnt;
		}
	}
	
	
	void myclick(MouseEvent e) {
		if(!flag_ing) {
			return;
		}
//		System.out.println(e.getComponent()); //panel안에 있는 모든 요소를 리스트로 관리 
//		System.out.println(e.getSource()); // 클릭 이벤트가 발생한 대상 객체를 관리
		JLabel temp = (JLabel) e.getSource();
//		System.out.println(temp.getText());
		String[] arr_ij = temp.getText().split(",");

		int i = Integer.parseInt(arr_ij[0]);
		int j = Integer.parseInt(arr_ij[1]);

		if(arr2D[i][j] > 0)	return;
		
		int stone = 0;
		
		if (flag_wb) {
			arr2D[i][j] = 1;
			
		} else {
			arr2D[i][j] = 2;
		}
		stone = arr2D[i][j];
		
		int up = getUP(i, j, stone);
		int dw = getDW(i, j, stone);
		int le = getLE(i, j, stone);
		int ri = getRI(i, j, stone);
		int ur = getUR(i, j, stone);
		int ul = getUL(i, j, stone);
		int dr = getDR(i, j, stone);
		int dl = getDL(i, j, stone);
	
		int d1 = up + dw + 1;
		int d2 = ur + dl + 1;
		int d3 = ri + le + 1;
		int d4 = ul + dr + 1;
		
		String tmp = "";
		
		myrender();

		if(d1 == 5 || d2 == 5 || d3 == 5 || d4 == 5) {
			if(flag_wb) {
				tmp = "흑";
			}else {
				tmp = "백";				
			}
			JOptionPane.showMessageDialog(null, tmp + "돌 승리");
			flag_ing = false;
		}

		flag_wb = !flag_wb;

//		System.out.println("up : " + up);
//		System.out.println("down : " + dw);
//		System.out.println("left : " + le);
//		System.out.println("right : " + ri);
//		System.out.println("rightUp : " + ur);
//		System.out.println("leftUp : " + ul);
//		System.out.println("rightDown : " + dr);
//		System.out.println("leftDown : " + dl);
//		System.out.println("----------------");
		
	}
	
	void myReset() {
		for(int i = 0; i < arr2D.length; i++) {
			for(int j = 0; j < arr2D[0].length; j++) {
				arr2D[i][j] = 0;
			}
		}
		myrender();
		flag_wb = true;
		flag_ing = true;
	}
}
