package kr.co.aiai.dao;

import java.sql.SQLException;
import java.util.List;

import com.ibatis.sqlmap.client.SqlMapClient;

import kr.co.aiai.ibatis.MySqlMapper;
import kr.co.aiai.model.Emp;

public class EmpDao {
	private static SqlMapClient sqlMapper;

	public EmpDao() {
		sqlMapper = MySqlMapper.getSqlMapper();
	}

	public Emp select(int e_id) throws SQLException {
		return (Emp) sqlMapper.queryForObject("select", e_id);
	}
	
	public List<Emp> selectList() throws SQLException {
		return sqlMapper.queryForList("selectList");
	}
	
	public int insert(Emp vo) throws SQLException {
		return sqlMapper.update("insert", vo);
	}
	
	public int update(Emp vo) throws SQLException {
		return sqlMapper.update("update", vo);
	}
	
	public int delete(String e_id) throws SQLException {
		return sqlMapper.update("delete", e_id);
	}

	public static void main(String[] args) throws SQLException {
		EmpDao dao = new EmpDao();
		
		Emp e = dao.select(1);
		
		System.out.print(e.getE_id() + "\t");
		System.out.print(e.getE_name() + "\t");
		System.out.print(e.getGen() + "\t");
		System.out.println(e.getAddr());

//		List<Emp> list = dao.selectList();
		
//		for(int i = 0; i < list.size(); i++) {
//			Emp vo = list.get(i);
//			System.out.print(vo.getE_id() + "\t");
//			System.out.print(vo.getE_name() + "\t");
//			System.out.print(vo.getGen() + "\t");
//			System.out.println(vo.getAddr());
//		}
//		
//		Emp e2 = new Emp();
//		
//		e2.setE_id("6");
//		e2.setE_name("6");
//		e2.setGen("7");
//		e2.setAddr("7");
//		
//		int ins = dao.insert(e2);
//		
//		System.out.println("insert : " + ins);
//		
//		Emp e3 = new Emp();
//		
//		e3.setE_id("6");
//		e3.setE_name("6"); //만약 파라미터 하나를 비워두면 null 값이 들어가는 채로 업데이트됨
//		e3.setGen("6");
//		e3.setAddr("6");
//		
//		int upd = dao.update(e3);
//		
//		System.out.println("update : " + upd);
		
		int del = dao.delete("5");
		
		System.out.println("delete : " + del);
	}

}

