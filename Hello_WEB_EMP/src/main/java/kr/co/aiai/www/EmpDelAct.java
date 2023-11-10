package kr.co.aiai.www;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.model.Emp;

@WebServlet("/emp_del_act")
public class EmpDelAct extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		EmpDao dao = new EmpDao();
		
		String e_id = request.getParameter("e_id");
		
		int cnt = 0;
		
		try {
			cnt = dao.delete(e_id);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		request.setAttribute("cnt", cnt);
		RequestDispatcher rd = request.getRequestDispatcher("emp_del_act.jsp");
		
		rd.forward(request, response);
	}

}
