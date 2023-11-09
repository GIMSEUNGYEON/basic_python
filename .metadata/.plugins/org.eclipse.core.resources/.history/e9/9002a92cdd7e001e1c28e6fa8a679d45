package kr.co.aiai.www;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.model.Emp;

@WebServlet("/emp_list")
public class EmpList extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RequestDispatcher rd = request.getRequestDispatcher("emp_list.jsp");
		
		String a = "홍길동";
		request.setCharacterEncoding("UTF-8");
		request.setAttribute("이름", a);
				
		ArrayList<Emp> list = new ArrayList<Emp>();
		
		EmpDao dao = new Empdao();
		
		list.add(new Emp("1","1","1","1"));
		list.add(new Emp("2","2","2","2"));
		
		request.setAttribute("list", list);

		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
