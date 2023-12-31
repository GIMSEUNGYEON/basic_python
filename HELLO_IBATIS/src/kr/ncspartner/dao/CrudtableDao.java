package kr.ncspartner.dao;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.ibatis.sqlmap.client.SqlMapClient;

import kr.ncspartner.ibatis.MySqlMapper;
import kr.ncspartner.model.Crudtable;

public class CrudtableDao {
	private static SqlMapClient sqlMapper;

	public CrudtableDao() {
		sqlMapper = MySqlMapper.getSqlMapper();
	}

	public List<Crudtable> selectList() throws SQLException {
		return sqlMapper.queryForList("selectList");
	}

	public Crudtable select(int crud_id) throws SQLException {
		return (Crudtable) sqlMapper.queryForObject("select", crud_id);
	}

	public int insert(Crudtable st) throws SQLException {
		return sqlMapper.update("insert", st);
	}

	public int update(Crudtable st) throws SQLException {
		return sqlMapper.update("update", st);
	}

	public int delete(String col1) throws SQLException {
		return sqlMapper.update("delete", col1);
	}

	public static void main(String[] args) throws SQLException {
		CrudtableDao dao = new CrudtableDao();
		
//		ArrayList<Crudtable> list = (ArrayList<Crudtable>) dao.selectList();
		
//		for(int i = 0; i < list.size(); i++) {
//			Crudtable temp = list.get(i);
//			System.out.print(temp.getCrud_id() + "	");
//			System.out.print(temp.getCrud_name() + "	");
//			System.out.println(temp.getMobile() + "	");
//			
//		}	
		//selectList
//		Crudtable ct = dao.select(1);
//		
//		System.out.println(ct.getCrud_id());
//		System.out.println(ct.getCrud_name());
//		System.out.println(ct.getMobile());
		//select 1개
		
//		Crudtable st = new Crudtable();		
//		st.setCrud_name("1");
//		st.setMobile("1");
//		int in = dao.insert(st);
		
//		System.out.println(in);
		// insert auto increasement가 설정되어 있어 id는 넣어주지 않아도 자동으로 들어감
		
//		Crudtable st2 = new Crudtable();
//		st.setCrud_id(1);
//		st2.setCrud_name("5");
//		st2.setMobile("5");
//		int up = dao.insert(st2);
//		
//		System.out.println(up);
		//update where절에 넣을 id가 필요함
		
		int del = dao.delete("1");
		System.out.println(del);
		//delete 삭제할 행을 입력
	}

}

