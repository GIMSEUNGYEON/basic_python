package kr.co.aiai.dao;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.ibatis.sqlmap.client.SqlMapClient;

import kr.co.aiai.ibatis.MySqlMapper;
import kr.co.aiai.vo.EmpVO;

public class EmpDao {
	private static SqlMapClient sqlMapper;

	public EmpDao() {
		sqlMapper = MySqlMapper.getSqlMapper();
	}

	public EmpVO select(String e_id) throws SQLException {
		return (EmpVO) sqlMapper.queryForObject("select", e_id);
	}
	
	public List<EmpVO> selectList() throws SQLException {
		return sqlMapper.queryForList("selectList");
	}
	
	public int insert(EmpVO vo) throws SQLException {
		return sqlMapper.update("insert", vo);
	}
	
	public int update(EmpVO vo) throws SQLException {
		return sqlMapper.update("update", vo);
	}
	
	public int delete(String e_id) throws SQLException {
		return sqlMapper.update("delete", e_id);
	}

	public static void main(String[] args) throws SQLException {
		EmpDao dao = new EmpDao();
		
		EmpVO e = dao.select("1");

		ArrayList<EmpVO> list = (ArrayList<EmpVO>)dao.selectList();
		
		System.out.println(list.size());
	}

}

