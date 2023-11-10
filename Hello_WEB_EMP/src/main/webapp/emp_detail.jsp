<%@page import="kr.co.aiai.model.Emp"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%
	Emp vo = (Emp)request.getAttribute("vo");
%>
<style>
	th {		
		width: 50px;
	}
	
	td {
		width: 50px;
		text-align:center;
	}
	
</style>
<script>
	function fn_mod(){
		location.href="emp_mod?e_id=<%=vo.getE_id()%>";
	}
	function fn_del_act(){
		
		if(confirm("한번 지워진 데이터는 복구가 불가합니다. 정말 삭제하시겠습니까?")){			
			document.frm.submit();
		}else {
			return;
		}
	}
</script>
</head>
<body>
<form name="frm" action="emp_del_act" method="post">
<input type="hidden" name="e_id" value="<%=vo.getE_id()%>">
	<table border="1px solid black">
		<tr>
			<th>사번</th>
			<td><%=vo.getE_id()%></td>
		</tr>
		
		<tr>
			<th>이름</th>
			<td><%=vo.getE_name()%></td>
		</tr>
		
		<tr>
			<th>성별</th>
			<td><%=vo.getGen()%></td>
		</tr>
		
		<tr>
			<th>주소</th>
			<td><%=vo.getAddr()%></td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="button" value="수정" onclick="fn_mod()">
				<input type="button" value="삭제" onclick="fn_del_act()">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
