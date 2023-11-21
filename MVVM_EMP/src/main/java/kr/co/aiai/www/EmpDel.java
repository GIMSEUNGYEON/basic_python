package kr.co.aiai.www;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.util.AjaxUtil;
import kr.co.aiai.vo.EmpVO;

@WebServlet("/emp_del")
public class EmpDel extends HttpServlet {
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		EmpDao dao = new EmpDao();
		String e_id = request.getParameter("e_id");
		try {
			int cnt = dao.delete(e_id);
			AjaxUtil.responseJson(response, cnt + "");
		}catch (Exception e) {
			e.printStackTrace();
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
